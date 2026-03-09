# InstaCode

A Python typing-practice web app built with Django. Reinforce code knowledge by **typing** real snippets — algorithms, design patterns, interview answers, and more — directly in a Monaco editor inside your browser.

---

## Features

- **Typing Practice** — Monaco editor with live accuracy and WPM tracking
- **7 Learning Tracks** covering DSA, Web Dev, DevOps, System Design, Python Certs, Data Science, Python Data Structures
- **Python Interview: 100 Q&A** — 97 curated Q&A snippets (Q1–Q100) at `/interview/`
- **DSA Interview: 99 Q&A** — 99 DSA-focused Q&A snippets (Q101–Q199) at `/dsa-interview/`
- **Django Slides** — 14 snippets from the Django QMD slideshow at `/django/`
- **FastAPI Slides** — 18 snippets from the FastAPI QMD slideshow at `/fastapi/`
- **DSA Slides** — 20 snippets from the DSA QMD slideshow at `/dsa/`
- **Playground** — free-form typing sandbox
- **Dashboard & Stats** — per-snippet history and progress tracking
- **User Management** — staff-only CRUD for site users
- **Auth-protected** — every view requires login; `/login/` is the entry point

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.3, Python 3.12 |
| Frontend | TailwindCSS (CDN), FontAwesome 6.5.0, Monaco Editor |
| Database | SQLite (`db.sqlite3`) |
| Static files | WhiteNoise 6.12.0 |
| Deployment | PythonAnywhere |

---

## Learning Tracks

| Track | URL | Topics |
|---|---|---|
| **DSA & Algorithms** | `/tracks/dsa/` | Big-O, arrays, strings, trees, graphs, DP, greedy, 18 patterns |
| **Web Development** | `/tracks/web/` | Django MVT, ORM, CBVs, FastAPI, design patterns |
| **DevOps & Cloud** | `/tracks/devops/` | Git, Linux, Ansible, Docker, Kubernetes, AWS/Azure/GCP |
| **System Design** | `/tracks/system-design/` | Scalability, caching, consistent hashing, distributed systems |
| **Python Certifications** | `/tracks/python-certs/` | PCEP, PCAP, PCPP |
| **Data Science** | `/tracks/data-science/` | NumPy, Pandas |
| **Python Data Structures** | `/tracks/python-ds/` | Arrays, linked lists, stacks, queues, hash tables, graphs |

### Dedicated browsers

| Section | URL | Snippets | Theme |
|---|---|---|---|
| Python Interview Q&A | `/interview/` | 97 (Q1–Q100) | Rose |
| DSA Interview Q&A | `/dsa-interview/` | 99 (Q101–Q199) | Amber |
| Django Slides | `/django/` | 14 | Blue |
| FastAPI Slides | `/fastapi/` | 18 | Teal |
| DSA Slides | `/dsa/` | 20 | Brand |

---

## Local Setup

```bash
# 1. Clone and enter the project
git clone <repo-url>
cd InstaCode

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env — set SECRET_KEY, DJANGO_DEBUG=True for dev

# 5. Apply migrations
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. Run the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and log in.

---

## Seeding Content

All seed commands are **idempotent** (safe to re-run). Use `--clear` to wipe and re-seed from scratch.

### Interview Q&A

**Python Interview (Q1–Q100):**
```bash
python manage.py seed_interview_questions --file /path/to/python_100_questions_and_answers.md
```

**DSA Interview (Q101–Q199):**
```bash
python manage.py seed_dsa_questions --file /path/to/python_dsa_100_questions_and_answers.md
```

### Slideshow Snippets (QMD files)

**Django** (14 snippets — settings, views, ORM, auth, DRF, testing):
```bash
python manage.py seed_django_snippets
# or with explicit path:
python manage.py seed_django_snippets --file /path/to/django.qmd
```

**FastAPI** (18 snippets — routing, Pydantic, async SQLAlchemy, JWT, WebSockets):
```bash
python manage.py seed_fastapi_snippets
# or with explicit path:
python manage.py seed_fastapi_snippets --file /path/to/fastapi.qmd
```

**DSA** (20 snippets — data structures, algorithms, patterns & reference):
```bash
python manage.py seed_dsa_slides
# or with explicit path:
python manage.py seed_dsa_slides --file /path/to/dsa.qmd
```

### Seed All at Once

```bash
python manage.py seed_interview_questions --file /path/to/python_100_questions_and_answers.md
python manage.py seed_dsa_questions       --file /path/to/python_dsa_100_questions_and_answers.md
python manage.py seed_django_snippets     --file /path/to/django.qmd
python manage.py seed_fastapi_snippets    --file /path/to/fastapi.qmd
python manage.py seed_dsa_slides          --file /path/to/dsa.qmd
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key (generate with `get_random_secret_key()`) |
| `DJANGO_DEBUG` | `True` for development, `False` for production |
| `ALLOWED_HOSTS` | Comma-separated hostnames (e.g. `yourusername.pythonanywhere.com`) |
| `CSRF_TRUSTED_ORIGINS` | Must start with `https://` — same as `ALLOWED_HOSTS` |

---

## Deployment (PythonAnywhere)

1. Upload the project to PythonAnywhere and activate the virtualenv
2. Set the environment variables in the `.env` file (never commit it)
3. Run `python manage.py collectstatic`
4. Configure the WSGI file to point to `instacode.wsgi`
5. Reload the web app

---

## Project Structure

```
InstaCode/
├── instacode/              # Django project config (settings, urls, wsgi)
├── typing_practice/        # Main app
│   ├── management/
│   │   └── commands/
│   │       ├── seed_interview_questions.py   # Python Q&A  Q1–Q100
│   │       ├── seed_dsa_questions.py         # DSA Q&A     Q101–Q199
│   │       ├── seed_django_snippets.py       # django.qmd  14 slides
│   │       ├── seed_fastapi_snippets.py      # fastapi.qmd 18 slides
│   │       └── seed_dsa_slides.py            # dsa.qmd     20 slides
│   ├── models.py           # Category, CodeSnippet, TypingSession
│   ├── views.py            # All views, TRACKS, Interview/Slide views
│   └── urls.py
├── templates/
│   ├── base.html
│   └── typing_practice/
│       ├── interview.html
│       ├── dsa_interview.html
│       ├── django_slides.html
│       ├── fastapi_slides.html
│       └── dsa_slides.html
├── static/
├── .env.example
├── pyproject.toml
└── manage.py
```

---

## License

See [LICENSE](LICENSE).


---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.3, Python 3.12 |
| Frontend | TailwindCSS (CDN), FontAwesome 6.5.0, Monaco Editor |
| Database | SQLite (`db.sqlite3`) |
| Static files | WhiteNoise 6.12.0 |
| Deployment | PythonAnywhere |

---

## Learning Tracks

| Track | Topics |
|---|---|
| **DSA & Algorithms** | Big-O, arrays, strings, trees, graphs, DP, greedy, patterns |
| **Web Development** | Django MVT, ORM, CBVs, FastAPI, design patterns |
| **DevOps & Cloud** | Git, Linux, Ansible, Docker, Kubernetes, AWS/Azure/GCP |
| **System Design** | Scalability, caching, consistent hashing, distributed systems |
| **Python Certifications** | PCEP, PCAP, PCPP |
| **Data Science** | NumPy, Pandas |
| **Python Data Structures** | Arrays, linked lists, stacks, queues, hash tables, graphs |

Plus two dedicated interview browsers:
- `/interview/` — Python Interview Q1–Q100 (rose theme)
- `/dsa-interview/` — Python DSA Interview Q101–Q199 (amber theme)

---

## Local Setup

```bash
# 1. Clone and enter the project
git clone <repo-url>
cd InstaCode

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env — set SECRET_KEY, DJANGO_DEBUG=True for dev

# 5. Apply migrations
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. Run the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and log in.

---

## Seeding Interview Questions

The two interview sections require running seed commands against their source markdown files.

**Python Interview (Q1–Q100):**
```bash
python manage.py seed_interview_questions --file /path/to/python_100_questions_and_answers.md
```

**DSA Interview (Q101–Q199):**
```bash
python manage.py seed_dsa_questions --file /path/to/python_dsa_100_questions_and_answers.md
```

Both commands are idempotent (safe to re-run). Use `--clear` to wipe and re-seed from scratch.

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key (generate with `get_random_secret_key()`) |
| `DJANGO_DEBUG` | `True` for development, `False` for production |
| `ALLOWED_HOSTS` | Comma-separated hostnames (e.g. `yourusername.pythonanywhere.com`) |
| `CSRF_TRUSTED_ORIGINS` | Must start with `https://` — same as `ALLOWED_HOSTS` |

---

## Deployment (PythonAnywhere)

1. Upload the project to PythonAnywhere and activate the virtualenv
2. Set the environment variables in the `.env` file (never commit it)
3. Run `python manage.py collectstatic`
4. Configure the WSGI file to point to `instacode.wsgi`
5. Reload the web app

---

## Project Structure

```
InstaCode/
├── instacode/              # Django project config (settings, urls, wsgi)
├── typing_practice/        # Main app
│   ├── management/
│   │   └── commands/       # seed_interview_questions.py, seed_dsa_questions.py
│   ├── models.py           # Category, CodeSnippet, TypingSession
│   ├── views.py            # All views + TRACKS + InterviewView + DsaInterviewView
│   └── urls.py
├── templates/
│   ├── base.html
│   └── typing_practice/    # Per-view templates
├── static/
├── .env.example
├── pyproject.toml
└── manage.py
```

---

## License

See [LICENSE](LICENSE).
