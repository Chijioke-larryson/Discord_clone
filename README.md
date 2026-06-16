# Justcord

Justcord is a beginner-friendly Django project that currently serves two simple pages through a `base` application. The project is set up with Django templates, a SQLite database, and a small URL structure that can be extended into a fuller chat, room, or community-style application.

## Project Status

This project is in early development. At the moment it includes:

- A Django project package named `Justcord`
- A Django app named `base`
- A home route that renders a navbar template
- A room route that renders a room navbar/control template
- SQLite as the default development database
- Project-level template discovery through the root `templates/` directory

## Tech Stack

- Python 3.12
- Django 6.0.6
- SQLite
- HTML templates
- Bootstrap-style markup in the templates

## Project Structure

```text
Justcord/
├── Justcord/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── base/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── navbar.html
│   └── room.html
├── db.sqlite3
├── manage.py
└── README.md
```

## How The App Works

The main project URL configuration is in `Justcord/urls.py`. It includes the `base` app routes at the root path:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('base.urls')),
]
```

The `base` app defines two routes in `base/urls.py`:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
]
```

Those routes are handled by `base/views.py`:

```python
def home(request):
    return render(request, 'navbar.html')

def room(request):
    return render(request, 'room.html')
```

Because `Justcord/settings.py` includes this template directory:

```python
'DIRS': [
    BASE_DIR / 'templates'
],
```

Django can find templates placed inside the root `templates/` folder.

## Available Pages

| URL | View | Template | Description |
| --- | --- | --- | --- |
| `/` | `home` | `templates/navbar.html` | Displays the main navigation bar. |
| `/room/` | `room` | `templates/room.html` | Displays a room-style navigation bar with mock controls. |
| `/admin/` | Django admin | Django admin templates | Default Django admin route. |

## Getting Started

Follow these steps to run the project locally.

### 1. Clone The Repository

```bash
git clone <your-repository-url>
cd Justcord
```

If you are already inside the project folder, you can skip this step.

### 2. Create A Virtual Environment

```bash
python3 -m venv class
```

This project currently uses a virtual environment folder named `class`.

### 3. Activate The Virtual Environment

On macOS or Linux:

```bash
source class/bin/activate
```

On Windows:

```bash
class\Scripts\activate
```

### 4. Install Django

If you do not already have the dependencies installed, install Django:

```bash
pip install django
```

The project was generated with Django 6.0.6. To install that exact version:

```bash
pip install Django==6.0.6
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start The Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

To view the room page:

```text
http://127.0.0.1:8000/room/
```

## Common Commands

Run the development server:

```bash
python manage.py runserver
```

Create database migrations:

```bash
python manage.py makemigrations
```

Apply database migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Run Django checks:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```

## Templates

Templates are stored in the root `templates/` directory.

- `navbar.html` is rendered by the home page.
- `room.html` is rendered by the room page.

The current template files contain Bootstrap-style class names. To make Bootstrap styles and interactive navbar toggles work fully in the browser, add Bootstrap CSS and JavaScript links to a base layout later.

A recommended future improvement is to create a shared layout file, for example:

```text
templates/base.html
```

Then `navbar.html` and `room.html` can extend that base template instead of each page standing alone.

## Development Notes

- `DEBUG` is currently set to `True`, which is fine for local development but should be changed before production deployment.
- `ALLOWED_HOSTS` is currently empty. This is fine for local development with Django's default server, but it must be configured for deployment.
- `db.sqlite3` is present in the project. For small local projects this is normal, but for a public repository you may choose to ignore it and let each developer create their own local database.
- The virtual environment folder `class/` should not be pushed to Git.
- Python cache folders such as `__pycache__/` should not be pushed to Git.
- The project does not currently include a `requirements.txt` file. Adding one will make setup easier for other developers.

## Recommended `.gitignore`

Before pushing to GitHub or another Git remote, make sure your `.gitignore` includes common Python, Django, and local environment files:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual environments
class/
venv/
.venv/
env/

# Django/local database
db.sqlite3

# Environment variables
.env

# OS/editor files
.DS_Store
.vscode/
.idea/
```

## Suggested Next Improvements

- Add a shared `base.html` template.
- Add Bootstrap CSS and JavaScript properly.
- Replace placeholder links such as `href="#"` with real routes.
- Add models for rooms, users, messages, or channels.
- Add authentication so users can join and leave rooms.
- Add a `requirements.txt` file using:

```bash
pip freeze > requirements.txt
```

- Add tests for the home page and room page.

## Pre-Push Checklist

Before pushing this project to a Git repository:

- Confirm the app runs locally with `python manage.py runserver`.
- Confirm `/` and `/room/` load correctly.
- Run `python manage.py check`.
- Add a `.gitignore` file if one does not exist.
- Avoid committing the `class/` virtual environment folder.
- Avoid committing `__pycache__/` folders.
- Decide whether `db.sqlite3` should be committed or ignored.
- Add `requirements.txt` if other people need to install the project easily.

## License

No license has been added yet. If this project will be public, consider adding a license file before publishing.
