# Chatbot API

This repository contains a Django application created for learning and practicing how to use the OpenAI API, it serves as a basic example of an API integrated with OpenAI, designed as an AI-powered chatbot.

## Prerequisites

Ensure you have the following installed before starting:

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv ./envs/env
   source ./envs/env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. Move to / folder:

   ```bash
   cd my_django_gpt_api
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Access the application

Using http://127.0.0.1:8000/ or http://localhost:8000/

## Usage

Once the development server is running, you can access:

- Admin panel at `http://127.0.0.1:8000/admin/` to manage users, categories, posts and comments
- Endpoints documentation at `http://localhost:8000/doc/` or `http://localhost:8000/redoc/`

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.
