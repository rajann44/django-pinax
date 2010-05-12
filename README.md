# Pinax Project

A Django-based social web platform built with Pinax. This project demonstrates how to build a feature-rich social website using Django and Pinax.

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

## Dependencies

- Django 1.2.7
- Pinax 0.9a2
- Various Django apps for social features

## Note

This project is for educational purposes and demonstrates the capabilities of Django and Pinax for building social web applications. 