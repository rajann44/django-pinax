# Pinax Project (2010 Era)

This is a Pinax project created to demonstrate the state of Django social web development in 2010. Pinax was one of the first comprehensive Django project templates that bundled together common social web features.

## Features

- User authentication and profiles
- Social networking features (tribes, relationships)
- Content management (photos, wikis, topics)
- Messaging and notifications
- Ratings and comments
- And much more!

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python manage.py syncdb
```

4. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `settings.py`: Main Django settings file
- `urls.py`: URL routing configuration
- `wsgi.py`: WSGI application configuration
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded files

## Historical Context

This project uses:
- Django 1.2.7 (released in 2010)
- Pinax 0.9a2 (the version available in 2010)
- Various Django apps that were popular in 2010

## Note

This is a historical recreation and should not be used in production. Modern Django projects should use current versions of Django and follow current best practices. 