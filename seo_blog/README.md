# seo_blog

A small Django-based SEO blog app used as part of the SEO Tool project. This repository contains a Django app named `blog` and supporting project configuration for local development and testing.

## TL;DR

- Language: Python (Django)
- Quick start (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## What this repo contains

- `blog/` — Django application containing views, models, templates and static assets for the SEO blog.
- `manage.py` — Django management script (project root)
- `requirements.txt` — Python dependencies (if present)

(Your workspace may have additional top-level files and folders; the `blog` app is the focus.)

## Prerequisites

- Python 3.10+ recommended (adjust to your environment)
- Git (optional)
- A virtual environment (recommended)

## Setup (development)

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is missing, install Django and common deps manually, e.g. `pip install Django`.

3. Apply database migrations:

```powershell
python manage.py migrate
```

4. Create a superuser (optional):

```powershell
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Running tests

If tests exist in the project, run:

```powershell
python manage.py test
```

## Project structure (example)

```
D:/.../seo_blog/
├─ blog/
│  ├─ migrations/
│  ├─ templates/
│  ├─ static/
│  ├─ views.py
│  └─ models.py
├─ manage.py
├─ requirements.txt
└─ README.md
```

## Contributing

- Open a branch for your feature/fix: `git checkout -b feat/some-feature`
- Keep changes small and focused
- Add tests for new behavior where appropriate
- Run the test suite locally before submitting a PR

## Notes and assumptions

- This README assumes a Django project layout (presence of `manage.py` and a `blog` app). If your project is configured differently, adapt the commands accordingly.
- If you use a different Python version or containerized workflow, update the instructions.

## License

Include your preferred license here (e.g., MIT) or remove this section if a license is tracked elsewhere.
