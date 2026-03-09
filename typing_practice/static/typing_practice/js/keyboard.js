/*!
 * keyboard.js – InstaCode Virtual Keyboard  (Step 5)
 *
 * Provides (as globals, consumed by engine.js):
 *   buildKeyboard(layout)   – renders the on-screen keyboard
 *   highlightNextKey(ch)    – highlights the key the user must press next
 *
 * Also handles physical keydown/keyup animations independently.
 *
 * Layouts: qwerty | dvorak | colemak
 */
(function () {
  'use strict';

  // ── Helpers ──────────────────────────────────────────────────────────────
  // Character key
  function ch(label, lower, upper, code, width) {
    return { label, lower, upper: upper || '', code, width: width || '', mod: false };
  }
  // Modifier / non-typing key
  function mod(label, code, width) {
    return { label, lower: '', upper: '', code, width: width || '', mod: true };
  }
  // Enter and Tab are "action" keys that do produce typed characters in our engine
  function action(label, char, code, width) {
    return { label, lower: char, upper: '', code, width: width || '', mod: false };
  }
  // Escape HTML for safe innerHTML injection
  function esc(s) {
    return s
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ── Layout definitions ────────────────────────────────────────────────────
  //   Rows → keys defined by physical position (code) + layout-specific chars.
  //   'code' = KeyboardEvent.code (physical, layout-invariant)
  //   'lower'/'upper' = characters produced by this key in that layout
  //
  const LAYOUTS = {

    // ── QWERTY ───────────────────────────────────────────────────────────
    qwerty: [
      /* number row */
      [
        ch('`',  '`', '~', 'Backquote'),
        ch('1',  '1', '!', 'Digit1'),  ch('2', '2', '@', 'Digit2'),
        ch('3',  '3', '#', 'Digit3'),  ch('4', '4', '$', 'Digit4'),
        ch('5',  '5', '%', 'Digit5'),  ch('6', '6', '^', 'Digit6'),
        ch('7',  '7', '&', 'Digit7'),  ch('8', '8', '*', 'Digit8'),
        ch('9',  '9', '(', 'Digit9'),  ch('0', '0', ')', 'Digit0'),
        ch('-',  '-', '_', 'Minus'),   ch('=', '=', '+', 'Equal'),
        mod('⌫', 'Backspace', 'wide-2'),
      ],
      /* top letter row */
      [
        action('Tab', '\t', 'Tab', 'wide-1'),
        ch('q', 'q', 'Q', 'KeyQ'), ch('w', 'w', 'W', 'KeyW'),
        ch('e', 'e', 'E', 'KeyE'), ch('r', 'r', 'R', 'KeyR'),
        ch('t', 't', 'T', 'KeyT'), ch('y', 'y', 'Y', 'KeyY'),
        ch('u', 'u', 'U', 'KeyU'), ch('i', 'i', 'I', 'KeyI'),
        ch('o', 'o', 'O', 'KeyO'), ch('p', 'p', 'P', 'KeyP'),
        ch('[', '[', '{', 'BracketLeft'), ch(']', ']', '}', 'BracketRight'),
        ch('\\', '\\', '|', 'Backslash', 'wide-1'),
      ],
      /* home row */
      [
        mod('Caps', 'CapsLock', 'wide-2'),
        ch('a', 'a', 'A', 'KeyA'), ch('s', 's', 'S', 'KeyS'),
        ch('d', 'd', 'D', 'KeyD'), ch('f', 'f', 'F', 'KeyF'),
        ch('g', 'g', 'G', 'KeyG'), ch('h', 'h', 'H', 'KeyH'),
        ch('j', 'j', 'J', 'KeyJ'), ch('k', 'k', 'K', 'KeyK'),
        ch('l', 'l', 'L', 'KeyL'), ch(';', ';', ':', 'Semicolon'),
        ch("'", "'", '"', 'Quote'),
        action('↵', '\n', 'Enter', 'wide-3'),
      ],
      /* bottom letter row */
      [
        mod('⇧', 'ShiftLeft', 'wide-3'),
        ch('z', 'z', 'Z', 'KeyZ'), ch('x', 'x', 'X', 'KeyX'),
        ch('c', 'c', 'C', 'KeyC'), ch('v', 'v', 'V', 'KeyV'),
        ch('b', 'b', 'B', 'KeyB'), ch('n', 'n', 'N', 'KeyN'),
        ch('m', 'm', 'M', 'KeyM'), ch(',', ',', '<', 'Comma'),
        ch('.', '.', '>', 'Period'), ch('/', '/', '?', 'Slash'),
        mod('⇧', 'ShiftRight', 'wide-4'),
      ],
      /* spacebar row */
      [
        mod('Ctrl', 'ControlLeft',  'wide-1'),
        mod('Alt',  'AltLeft',      'wide-1'),
        ch('', ' ', ' ', 'Space', 'spacebar'),
        mod('Alt',  'AltRight',     'wide-1'),
        mod('Ctrl', 'ControlRight', 'wide-1'),
      ],
    ],

    // ── DVORAK ───────────────────────────────────────────────────────────
    dvorak: [
      /* number row — same as QWERTY, but [ ] swap with - = positions */
      [
        ch('`',  '`', '~', 'Backquote'),
        ch('1',  '1', '!', 'Digit1'),  ch('2', '2', '@', 'Digit2'),
        ch('3',  '3', '#', 'Digit3'),  ch('4', '4', '$', 'Digit4'),
        ch('5',  '5', '%', 'Digit5'),  ch('6', '6', '^', 'Digit6'),
        ch('7',  '7', '&', 'Digit7'),  ch('8', '8', '*', 'Digit8'),
        ch('9',  '9', '(', 'Digit9'),  ch('0', '0', ')', 'Digit0'),
        ch('[',  '[', '{', 'Minus'),   ch(']', ']', '}', 'Equal'),
        mod('⌫', 'Backspace', 'wide-2'),
      ],
      [
        action('Tab', '\t', 'Tab', 'wide-1'),
        ch("'", "'", '"', 'KeyQ'), ch(',', ',', '<', 'KeyW'),
        ch('.', '.', '>', 'KeyE'), ch('p', 'p', 'P', 'KeyR'),
        ch('y', 'y', 'Y', 'KeyT'), ch('f', 'f', 'F', 'KeyY'),
        ch('g', 'g', 'G', 'KeyU'), ch('c', 'c', 'C', 'KeyI'),
        ch('r', 'r', 'R', 'KeyO'), ch('l', 'l', 'L', 'KeyP'),
        ch('/', '/', '?', 'BracketLeft'), ch('=', '=', '+', 'BracketRight'),
        ch('\\', '\\', '|', 'Backslash', 'wide-1'),
      ],
      [
        mod('Caps', 'CapsLock', 'wide-2'),
        ch('a', 'a', 'A', 'KeyA'), ch('o', 'o', 'O', 'KeyS'),
        ch('e', 'e', 'E', 'KeyD'), ch('u', 'u', 'U', 'KeyF'),
        ch('i', 'i', 'I', 'KeyG'), ch('d', 'd', 'D', 'KeyH'),
        ch('h', 'h', 'H', 'KeyJ'), ch('t', 't', 'T', 'KeyK'),
        ch('n', 'n', 'N', 'KeyL'), ch('s', 's', 'S', 'Semicolon'),
        ch('-', '-', '_', 'Quote'),
        action('↵', '\n', 'Enter', 'wide-3'),
      ],
      [
        mod('⇧', 'ShiftLeft', 'wide-3'),
        ch(';', ';', ':', 'KeyZ'), ch('q', 'q', 'Q', 'KeyX'),
        ch('j', 'j', 'J', 'KeyC'), ch('k', 'k', 'K', 'KeyV'),
        ch('x', 'x', 'X', 'KeyB'), ch('b', 'b', 'B', 'KeyN'),
        ch('m', 'm', 'M', 'KeyM'), ch('w', 'w', 'W', 'Comma'),
        ch('v', 'v', 'V', 'Period'), ch('z', 'z', 'Z', 'Slash'),
        mod('⇧', 'ShiftRight', 'wide-4'),
      ],
      [
        mod('Ctrl', 'ControlLeft',  'wide-1'),
        mod('Alt',  'AltLeft',      'wide-1'),
        ch('', ' ', ' ', 'Space', 'spacebar'),
        mod('Alt',  'AltRight',     'wide-1'),
        mod('Ctrl', 'ControlRight', 'wide-1'),
      ],
    ],

    // ── COLEMAK ──────────────────────────────────────────────────────────
    // Same number row as QWERTY; letter changes listed by physical code:
    //   E→f, R→p, T→g, Y→j, U→l, I→u, O→y, P→;
    //   S→r, D→s, F→t, G→d, J→n, K→e, L→i, Semicolon→o
    //   N→k  (everything else same as QWERTY)
    colemak: [
      [
        ch('`',  '`', '~', 'Backquote'),
        ch('1',  '1', '!', 'Digit1'),  ch('2', '2', '@', 'Digit2'),
        ch('3',  '3', '#', 'Digit3'),  ch('4', '4', '$', 'Digit4'),
        ch('5',  '5', '%', 'Digit5'),  ch('6', '6', '^', 'Digit6'),
        ch('7',  '7', '&', 'Digit7'),  ch('8', '8', '*', 'Digit8'),
        ch('9',  '9', '(', 'Digit9'),  ch('0', '0', ')', 'Digit0'),
        ch('-',  '-', '_', 'Minus'),   ch('=', '=', '+', 'Equal'),
        mod('⌫', 'Backspace', 'wide-2'),
      ],
      [
        action('Tab', '\t', 'Tab', 'wide-1'),
        ch('q', 'q', 'Q', 'KeyQ'), ch('w', 'w', 'W', 'KeyW'),
        ch('f', 'f', 'F', 'KeyE'), ch('p', 'p', 'P', 'KeyR'),
        ch('g', 'g', 'G', 'KeyT'), ch('j', 'j', 'J', 'KeyY'),
        ch('l', 'l', 'L', 'KeyU'), ch('u', 'u', 'U', 'KeyI'),
        ch('y', 'y', 'Y', 'KeyO'), ch(';', ';', ':', 'KeyP'),
        ch('[', '[', '{', 'BracketLeft'), ch(']', ']', '}', 'BracketRight'),
        ch('\\', '\\', '|', 'Backslash', 'wide-1'),
      ],
      [
        mod('Caps', 'CapsLock', 'wide-2'),
        ch('a', 'a', 'A', 'KeyA'), ch('r', 'r', 'R', 'KeyS'),
        ch('s', 's', 'S', 'KeyD'), ch('t', 't', 'T', 'KeyF'),
        ch('d', 'd', 'D', 'KeyG'), ch('h', 'h', 'H', 'KeyH'),
        ch('n', 'n', 'N', 'KeyJ'), ch('e', 'e', 'E', 'KeyK'),
        ch('i', 'i', 'I', 'KeyL'), ch('o', 'o', 'O', 'Semicolon'),
        ch("'", "'", '"', 'Quote'),
        action('↵', '\n', 'Enter', 'wide-3'),
      ],
      [
        mod('⇧', 'ShiftLeft', 'wide-3'),
        ch('z', 'z', 'Z', 'KeyZ'), ch('x', 'x', 'X', 'KeyX'),
        ch('c', 'c', 'C', 'KeyC'), ch('v', 'v', 'V', 'KeyV'),
        ch('b', 'b', 'B', 'KeyB'), ch('k', 'k', 'K', 'KeyN'),
        ch('m', 'm', 'M', 'KeyM'), ch(',', ',', '<', 'Comma'),
        ch('.', '.', '>', 'Period'), ch('/', '/', '?', 'Slash'),
        mod('⇧', 'ShiftRight', 'wide-4'),
      ],
      [
        mod('Ctrl', 'ControlLeft',  'wide-1'),
        mod('Alt',  'AltLeft',      'wide-1'),
        ch('', ' ', ' ', 'Space', 'spacebar'),
        mod('Alt',  'AltRight',     'wide-1'),
        mod('Ctrl', 'ControlRight', 'wide-1'),
      ],
    ],
  };

  // ── State ──────────────────────────────────────────────────────────────
  const kbEl     = document.getElementById('virtual-keyboard');
  let codeToEl   = {};   // KeyboardEvent.code → DOM element
  let currentLayout = 'qwerty';

  // ── buildKeyboard ──────────────────────────────────────────────────────
  /**
   * Clears and re-renders the virtual keyboard for a given layout name.
   * Also rebuilds the codeToEl reverse-lookup map.
   * @param {string} layout  'qwerty' | 'dvorak' | 'colemak'
   */
  window.buildKeyboard = function buildKeyboard(layout) {
    currentLayout = layout;
    const rows = LAYOUTS[layout] || LAYOUTS.qwerty;

    kbEl.innerHTML = '';
    codeToEl = {};

    rows.forEach(function (rowKeys) {
      const rowEl = document.createElement('div');
      rowEl.className = 'flex gap-1 justify-center';

      rowKeys.forEach(function (key) {
        const btn = document.createElement('div');

        // Base classes
        let cls = 'key';
        if (key.width) cls += ' ' + key.width;
        btn.className = cls;

        // Data attributes for highlight/press lookups
        btn.dataset.code  = key.code;
        btn.dataset.lower = key.lower;
        btn.dataset.upper = key.upper;

        // Label rendering:
        //   • Letter keys  — show lowercase letter
        //   • Number/symbol dual-char keys — show shifted char (small) above lower char
        //   • Space — show the word "space"
        //   • Everything else — show the label string as-is
        if (key.code === 'Space') {
          btn.innerHTML = '<span class="tracking-widest text-gray-600 text-[9px] uppercase">space</span>';
        } else if (
          !key.mod &&
          key.lower.length === 1 &&
          key.upper.length === 1 &&
          key.lower !== key.upper &&
          key.lower === key.lower.toLowerCase() &&
          key.upper === key.lower.toUpperCase()
        ) {
          // Pure letter key — one char suffices
          btn.textContent = key.lower;
        } else if (
          !key.mod &&
          key.lower.length === 1 &&
          key.upper.length === 1 &&
          key.lower !== key.upper
        ) {
          // Dual symbol/number key — stack upper (small) over lower
          btn.style.flexDirection = 'column';
          btn.style.alignItems    = 'center';
          btn.style.justifyContent = 'center';
          btn.style.lineHeight    = '1';
          btn.innerHTML =
            `<span style="font-size:9px;color:#555580;line-height:1">${esc(key.upper)}</span>` +
            `<span style="line-height:1">${esc(key.lower)}</span>`;
        } else {
          btn.textContent = key.label;
        }

        rowEl.appendChild(btn);
        codeToEl[key.code] = btn;
      });

      kbEl.appendChild(rowEl);
    });
  };

  // ── highlightNextKey ───────────────────────────────────────────────────
  /**
   * Removes all existing next-key highlights and applies a new one for `ch`.
   * If `ch` requires Shift, both Shift keys are highlighted too.
   * @param {string} ch  The single character that needs to be typed next.
   */
  window.highlightNextKey = function highlightNextKey(ch) {
    // Clear previous highlights
    kbEl.querySelectorAll('.highlight-next').forEach(function (el) {
      el.classList.remove('highlight-next');
    });

    if (ch === undefined || ch === null || ch === '') return;

    let needsShift = false;
    let found = false;

    // Search all rendered keys for a matching lower or upper character
    const keys = kbEl.querySelectorAll('.key');
    for (let i = 0; i < keys.length; i++) {
      const btn = keys[i];
      if (btn.dataset.lower === ch) {
        btn.classList.add('highlight-next');
        needsShift = false;
        found = true;
        break;
      }
      if (btn.dataset.upper === ch && ch !== '') {
        btn.classList.add('highlight-next');
        needsShift = true;
        found = true;
        break;
      }
    }

    if (!found) return;

    // Highlight both Shift keys when an uppercase / shifted char is needed
    if (needsShift) {
      const sl = codeToEl['ShiftLeft'];
      const sr = codeToEl['ShiftRight'];
      if (sl) sl.classList.add('highlight-next');
      if (sr) sr.classList.add('highlight-next');
    }
  };

  // ── Physical key press animation ───────────────────────────────────────
  document.addEventListener('keydown', function (e) {
    const el = codeToEl[e.code];
    if (el) el.classList.add('pressed');
  });

  // keyup fires even when keydown called preventDefault()
  document.addEventListener('keyup', function (e) {
    const el = codeToEl[e.code];
    if (el) el.classList.remove('pressed');
  });

  // Safety: clear all pressed states if window loses focus
  window.addEventListener('blur', function () {
    kbEl.querySelectorAll('.pressed').forEach(function (el) {
      el.classList.remove('pressed');
    });
  });

})();
