/*!
 * engine.js – InstaCode Core Typing Engine  (Steps 3 & 4)
 *
 * Responsibilities:
 *   • Initialize Monaco Editor (read-only, ghost-text theme)
 *   • Apply progressive char-level decorations (correct / error / cursor)
 *   • Intercept keystrokes globally and route through the typing state machine
 *   • Auto-indent: Enter auto-skips leading whitespace on the next line
 *   • Modes:  Forced  – wrong key flashes red, input ignored, must retype
 *             Natural – wrong key advances + marks error; Backspace undoes
 *   • Real-time WPM & Accuracy; post-game modal + stats API call
 *   • Thin stubs for buildKeyboard / highlightNextKey (filled in Step 5)
 */
(function () {
  'use strict';

  // ── 1. Monaco CDN loader config ─────────────────────────────────────────
  require.config({
    paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs' }
  });

  // ── 2. Inject decoration CSS ────────────────────────────────────────────
  //   Monaco renders its own syntax highlighting; we override with these
  //   inlineClassName decorations to drive the ghost-text typing experience.
  (function injectStyles() {
    const s = document.createElement('style');
    s.textContent = `
      /* Correctly-typed characters → bright green */
      .monaco-editor .ic-correct {
        color: #86efac !important;
      }
      /* Error character (Natural mode) → red tint */
      .monaco-editor .ic-error {
        color: #fca5a5 !important;
        background: rgba(239, 68, 68, .22) !important;
        border-radius: 2px;
      }
      /* Auto-skipped indentation → very dim green */
      .monaco-editor .ic-autoskip {
        color: #166534 !important;
      }
      /* Current character to type → highlighted block */
      .monaco-editor .ic-cursor {
        background: rgba(255, 255, 255, .12) !important;
        border-bottom: 2px solid #10b981 !important;
        color: #ffffff !important;
        border-radius: 2px;
      }
      /* Newline cursor ↵ injected text */
      .monaco-editor .ic-cursor-eol {
        color: #10b981 !important;
        font-style: normal !important;
        opacity: .85;
      }
    `;
    document.head.appendChild(s);
  })();

  // ── 3. State ────────────────────────────────────────────────────────────
  let editor          = null;
  let model           = null;
  let decorCollection = null;   // Monaco IDecorationsCollection

  let currentIndex  = 0;   // index into APP.code the user must type next
  let errors        = 0;   // wrong keystrokes (natural: wrong presses; forced: 0)
  let totalKS       = 0;   // total counted keystrokes (excludes ignored forced-wrong)
  let startTime     = null;
  let isRunning     = false;
  let timerInterval = null;
  let autoScroll    = true; // whether editor follows the cursor

  // Sets of character indices
  const errorSet    = new Set();  // positions with uncorrected errors (natural)
  const autoSkipSet = new Set();  // positions auto-skipped as indentation

  const code = APP.code;

  // Auto-skip characters that cannot be typed on a standard keyboard:
  // box-drawing chars, arrows, emoji, math symbols, etc. (codepoint > 126).
  // They are added to autoSkipSet so they render as "already typed" / neutral.
  function skipNonTypeable() {
    while (currentIndex < code.length) {
      const cp = code.codePointAt(currentIndex);
      if (cp > 126 || (cp < 32 && cp !== 10 && cp !== 9)) {
        autoSkipSet.add(currentIndex);
        currentIndex++;
      } else {
        break;
      }
    }
  }

  // ── 4. DOM refs ─────────────────────────────────────────────────────────
  const elTimer  = document.getElementById('metric-timer');
  const elWpm    = document.getElementById('metric-wpm');
  const elAcc    = document.getElementById('metric-acc');
  const resetBtn = document.getElementById('reset-btn');
  const flashEl  = document.getElementById('flash-overlay');
  const modal    = document.getElementById('results-modal');
  const retryBtn = document.getElementById('modal-retry-btn');

  // ── 5. Monaco initialisation ────────────────────────────────────────────
  require(['vs/editor/editor.main'], function () {

    // All token colours set to the same dim purple-grey so every character
    // looks like "ghost text" until the user types over it.
    monaco.editor.defineTheme('ic-dark', {
      base:    'vs-dark',
      inherit: false,
      rules: [
        { token: '',           foreground: '3d3d5c' },
        { token: 'keyword',    foreground: '3d3d5c' },
        { token: 'string',     foreground: '3d3d5c' },
        { token: 'comment',    foreground: '2a2a42' },
        { token: 'number',     foreground: '3d3d5c' },
        { token: 'type',       foreground: '3d3d5c' },
        { token: 'function',   foreground: '3d3d5c' },
        { token: 'identifier', foreground: '3d3d5c' },
        { token: 'operator',   foreground: '3d3d5c' },
        { token: 'delimiter',  foreground: '3d3d5c' },
      ],
      colors: {
        'editor.background':                 '#0d0d1a',
        'editor.foreground':                 '#3d3d5c',
        'editorLineNumber.foreground':       '#1e1e38',
        'editorLineNumber.activeForeground': '#3a3a5c',
        'editor.lineHighlightBackground':    '#00000000',
        'editor.selectionBackground':        '#00000000',
        'editorCursor.foreground':           '#00000000',  // hide Monaco cursor
        'editorWhitespace.foreground':       '#1a1a2e',
        'editorIndentGuide.background':      '#1a1a2e',
        'editorIndentGuide.activeBackground':'#222236',
      }
    });

    editor = monaco.editor.create(
      document.getElementById('monaco-container'),
      {
        value:                      code,
        language:                   'python',
        theme:                      'ic-dark',
        readOnly:                   true,
        readOnlyMessage:            { value: '' },
        fontSize:                   14,
        fontFamily:                 '"Fira Code","Cascadia Code",Consolas,monospace',
        fontLigatures:              true,
        lineNumbers:                'on',
        minimap:                    { enabled: false },
        scrollBeyondLastLine:       false,
        wordWrap:                   'off',
        renderWhitespace:           'boundary',
        smoothScrolling:            true,
        contextmenu:                false,
        quickSuggestions:           false,
        parameterHints:             { enabled: false },
        suggestOnTriggerCharacters: false,
        acceptSuggestionOnEnter:    'off',
        tabCompletion:              'off',
        wordBasedSuggestions:       'off',
        scrollbar: { useShadows: false, verticalScrollbarSize: 6, horizontalScrollbarSize: 6 },
      }
    );

    model           = editor.getModel();
    decorCollection = editor.createDecorationsCollection([]);

    skipNonTypeable();
    applyDecorations();
    _buildKb(getLayout());
    _highlightKey(currentChar());

    // Rebuild keyboard when layout dropdown changes
    document.getElementById('kb-layout-select').addEventListener('change', () => {
      _buildKb(getLayout());
      _highlightKey(currentChar());
    });
  });

  // ── 6. Helpers ──────────────────────────────────────────────────────────
  const currentChar = () => code[currentIndex] ?? '';
  const getMode     = () => document.getElementById('typing-mode-select').value;
  const getLayout   = () => document.getElementById('kb-layout-select').value;

  /** Safe wrappers for virtual-keyboard functions defined in Step 5 */
  function _buildKb(layout)  { if (typeof buildKeyboard    === 'function') buildKeyboard(layout);    }
  function _highlightKey(ch) { if (typeof highlightNextKey === 'function') highlightNextKey(ch);     }

  // ── 7. Decoration engine ────────────────────────────────────────────────
  /**
   * Convert a 0-based string offset into a Monaco Range covering exactly one character.
   * Handles the last character and newlines by clamping the end offset.
   */
  function rangeForIndex(idx) {
    const start = model.getPositionAt(idx);
    const end   = model.getPositionAt(Math.min(idx + 1, code.length));
    return new monaco.Range(start.lineNumber, start.column, end.lineNumber, end.column);
  }

  /**
   * Rebuild all Monaco decorations from scratch based on current state.
   * Called after every state mutation (keypress / backspace / reset).
   *
   * Decoration layers (later entries override earlier via !important CSS):
   *   1. ic-correct  – single range [0, currentIndex) — one efficient range
   *   2. ic-error    – individual character overrides for error positions
   *   3. ic-autoskip – auto-skipped indentation chars
   *   4. ic-cursor   – the char the user must type next  (or ↵ for newline)
   */
  function applyDecorations() {
    if (!decorCollection) return;

    const decors = [];

    // 1. Correct range — single Monaco range is far more efficient than N chars
    if (currentIndex > 0) {
      const s = model.getPositionAt(0);
      const e = model.getPositionAt(currentIndex);
      decors.push({
        range:   new monaco.Range(s.lineNumber, s.column, e.lineNumber, e.column),
        options: { inlineClassName: 'ic-correct' },
      });
    }

    // 2. Error overrides (natural mode chars typed wrong; sit inside correct range)
    for (const idx of errorSet) {
      if (idx < currentIndex) {
        decors.push({ range: rangeForIndex(idx), options: { inlineClassName: 'ic-error' } });
      }
    }

    // 3. Auto-skipped indentation (dim green; user never pressed these)
    for (const idx of autoSkipSet) {
      decors.push({ range: rangeForIndex(idx), options: { inlineClassName: 'ic-autoskip' } });
    }

    // 4. Cursor — show what the user must press next
    if (currentIndex < code.length) {
      if (code[currentIndex] === '\n') {
        // Inject a visible ↵ glyph at end of the current line
        const pos = model.getPositionAt(currentIndex);
        decors.push({
          range:   new monaco.Range(pos.lineNumber, pos.column, pos.lineNumber, pos.column),
          options: { after: { content: ' ↵', inlineClassName: 'ic-cursor-eol' } },
        });
      } else {
        decors.push({
          range:   rangeForIndex(currentIndex),
          options: { inlineClassName: 'ic-cursor' },
        });
      }
    }

    decorCollection.set(decors);

    // Keep the current typing position visible (only when auto-scroll is on)
    if (autoScroll && currentIndex < code.length && editor) {
      editor.revealPositionInCenter(
        model.getPositionAt(currentIndex),
        monaco.editor.ScrollType.Smooth
      );
    }
  }

  // ── 8. Timer & live metrics ─────────────────────────────────────────────
  function startTimer() {
    if (isRunning) return;
    isRunning = true;
    startTime = Date.now();
    timerInterval = setInterval(updateMetrics, 500);
  }

  function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
    isRunning = false;
  }

  function updateMetrics() {
    if (!startTime) return;

    const secs  = (Date.now() - startTime) / 1000;
    const mins  = secs / 60;

    // WPM — standard formula: valid keystrokes / 5 / minutes
    // valid = total counted keystrokes minus errors
    const valid = Math.max(0, totalKS - errors);
    const wpm   = mins > 0.001 ? Math.round(valid / 5 / mins) : 0;

    // Accuracy — errors reduce it; forced mode always 100% (errors=0)
    const acc = totalKS > 0
      ? ((totalKS - errors) / totalKS * 100)
      : 100;

    const mm = Math.floor(secs / 60);
    const ss = Math.floor(secs % 60);
    elTimer.textContent = `${mm}:${ss.toString().padStart(2, '0')}`;
    elWpm.textContent   = wpm;
    elAcc.textContent   = `${acc.toFixed(1)}%`;
  }

  // ── 9. Keystroke interception ───────────────────────────────────────────
  document.addEventListener('keydown', handleKeydown);

  function handleKeydown(e) {
    // Never steal focus from UI controls (dropdowns, inputs).
    // Allow Monaco's own internal textarea (.inputarea) — that's the editor being clicked.
    const el  = document.activeElement;
    const tag = el?.tagName;
    const isMonacoInput = el?.classList.contains('inputarea');
    if (tag === 'SELECT' || tag === 'INPUT' || (tag === 'TEXTAREA' && !isMonacoInput)) return;

    // Only act on printable chars and our action keys
    const isAltGr     = e.ctrlKey && e.altKey;   // Windows AltGr fires ctrlKey+altKey
    const isPrintable = e.key.length === 1 && (!e.ctrlKey || isAltGr) && !e.metaKey && (!e.altKey || isAltGr);
    const isAction    = e.key === 'Enter' || e.key === 'Backspace' || e.key === 'Tab';
    if (!isPrintable && !isAction) return;

    e.preventDefault();   // block browser defaults (scroll on Space, etc.)

    if (currentIndex >= code.length) return;  // game already finished

    const mode     = getMode();
    const expected = code[currentIndex];

    // ─── Backspace ──────────────────────────────────────────────────────
    if (e.key === 'Backspace') {
      if (mode !== 'natural' || currentIndex <= 0) return;

      // Step back one real typed position, un-skip any auto-indented chars
      currentIndex--;
      while (currentIndex > 0 && autoSkipSet.has(currentIndex)) {
        autoSkipSet.delete(currentIndex);
        currentIndex--;
      }
      // Edge-case: landed exactly on an auto-skipped position
      if (autoSkipSet.has(currentIndex)) {
        autoSkipSet.delete(currentIndex);
      }
      errorSet.delete(currentIndex);

      applyDecorations();
      updateMetrics();
      _highlightKey(currentChar());
      return;
    }

    // ─── Map key to expected character ─────────────────────────────────
    const typed =
      e.key === 'Enter' ? '\n' :
      e.key === 'Tab'   ? '\t' :
      e.key;

    // Normalize typographic dashes (em dash —, en dash –, figure dash ‒) to
    // a regular hyphen so the keyboard '-' key is always accepted for them.
    const normDash = c => (c === '\u2014' || c === '\u2013' || c === '\u2012') ? '-' : c;
    const isCorrect = normDash(typed) === normDash(expected);

    // ─── Forced mode: wrong key → flash & ignore (don't count) ─────────
    if (!isCorrect && mode === 'forced') {
      flashError();
      return;
    }

    // ─── All remaining paths count as a keystroke ───────────────────────
    if (!isRunning) startTimer();
    totalKS++;

    if (isCorrect) {
      // Correct key ───────────────────────────────────────────────────
      errorSet.delete(currentIndex);
      currentIndex++;

      // Auto-indent: after Enter, skip leading whitespace automatically
      if (typed === '\n') {
        while (
          currentIndex < code.length &&
          (code[currentIndex] === ' ' || code[currentIndex] === '\t')
        ) {
          autoSkipSet.add(currentIndex);
          currentIndex++;
        }
      }

      skipNonTypeable();

      if (currentIndex >= code.length) {
        applyDecorations();
        finishSession();
      } else {
        applyDecorations();
        updateMetrics();
        _highlightKey(currentChar());
      }

    } else {
      // Wrong key — Natural mode ──────────────────────────────────────
      errors++;
      errorSet.add(currentIndex);
      currentIndex++;

      skipNonTypeable();

      applyDecorations();
      updateMetrics();
      _highlightKey(currentChar());
    }
  }

  // ── 10. Flash overlay (Forced mode) ────────────────────────────────────
  function flashError() {
    flashEl.classList.add('flash');
    setTimeout(() => flashEl.classList.remove('flash'), 160);
  }

  // ── 11. Session completion ──────────────────────────────────────────────
  function finishSession() {
    stopTimer();

    const elapsedSecs = startTime ? Math.round((Date.now() - startTime) / 1000) : 0;
    const elapsedMins = elapsedSecs / 60;
    const valid       = Math.max(0, totalKS - errors);
    const wpm         = elapsedMins > 0.001 ? Math.round(valid / 5 / elapsedMins) : 0;
    const accuracy    = totalKS > 0
      ? parseFloat((((totalKS - errors) / totalKS) * 100).toFixed(1))
      : 100.0;

    // Update final metrics bar too
    elWpm.textContent = wpm;
    elAcc.textContent = `${accuracy}%`;

    // Populate modal
    document.getElementById('result-wpm').textContent  = wpm;
    document.getElementById('result-acc').textContent  = `${accuracy}%`;
    document.getElementById('result-time').textContent = elapsedSecs;

    modal.classList.add('open');

    saveStats(wpm, accuracy, elapsedSecs);
  }

  async function saveStats(wpm, accuracy, timeTaken) {
    const statusEl = document.getElementById('result-status');

    // Playground mode: snippetId === 0 means custom code — no DB record to link
    if (APP.snippetId === 0) {
      if (statusEl) statusEl.textContent = '✎ Playground mode — stats not saved.';
      return;
    }

    // Read the Django csrftoken cookie so the endpoint's CSRF middleware is satisfied
    const csrfToken = (document.cookie.split(';')
      .map(c => c.trim())
      .find(c => c.startsWith('csrftoken=')) || '')
      .replace('csrftoken=', '');

    try {
      const res = await fetch(APP.statsUrl, {
        method:  'POST',
        headers: {
          'Content-Type':   'application/json',
          'X-CSRFToken':    csrfToken,
        },
        body: JSON.stringify({
          snippet_id:         APP.snippetId,
          wpm,
          accuracy,
          time_taken_seconds: timeTaken,
          typing_mode:        getMode(),
        }),
      });
      if (res.ok) {
        const data = await res.json();
        statusEl.textContent = `✓ Stats saved — session ${data.session_id.slice(0, 8)}…`;
      } else {
        statusEl.textContent = '⚠ Unable to save stats (server error).';
      }
    } catch (_) {
      statusEl.textContent = '⚠ Stats not saved (network error).';
    }
  }

  // ── 12. Reset ───────────────────────────────────────────────────────────
  function resetSession() {
    stopTimer();

    currentIndex  = 0;
    errors        = 0;
    totalKS       = 0;
    startTime     = null;

    errorSet.clear();
    autoSkipSet.clear();
    skipNonTypeable();

    elTimer.textContent = '0:00';
    elWpm.textContent   = '0';
    elAcc.textContent   = '100%';

    modal.classList.remove('open');

    applyDecorations();
    _buildKb(getLayout());
    _highlightKey(currentChar());
  }

  resetBtn.addEventListener('click', resetSession);
  retryBtn.addEventListener('click', resetSession);

  // ── 13. Auto-scroll toggle ──────────────────────────────────────────────
  const scrollBtn   = document.getElementById('scroll-toggle-btn');
  const scrollLabel = document.getElementById('scroll-toggle-label');

  scrollBtn.addEventListener('click', () => {
    autoScroll = !autoScroll;
    if (autoScroll) {
      scrollBtn.classList.remove('text-gray-500');
      scrollBtn.classList.add('text-brand-400');
      scrollLabel.textContent = 'Follow';
      // Immediately snap to current position
      if (editor && currentIndex < code.length) {
        editor.revealPositionInCenter(
          model.getPositionAt(currentIndex),
          monaco.editor.ScrollType.Smooth
        );
      }
    } else {
      scrollBtn.classList.remove('text-brand-400');
      scrollBtn.classList.add('text-gray-500');
      scrollLabel.textContent = 'Free';
    }
  });

})();
