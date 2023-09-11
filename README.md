# Event Reservation

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Project Functions](#project-functions-with-visualization)
- [Installation](#instalation)
- [Usage](#usage)

## Introduction

This Django-based Event Reservation System allows users to view upcoming events, make reservations, and receive confirmation emails for successful reservations. The system also includes a management interface for users to manage their reservations and check for expired reservations. User can delete not expired events.

## Project Structure

The project consists of the following key components:

1. **Views**:

   - `index`: Displays a list of upcoming events and handles event reservations. It sends confirmation emails for successful reservations.
   - `management`: Manages user reservations and checks for expired reservations.
   - `delete`: Handles the deletion of user reservations and checks for expiration.

2. **Models**:

   - `Event`: Represents an event with fields such as name, start date, and end date.
   - `Reservation`: Represents a user's reservation for an event.

3. **Utils**:

   - `send_confirmation_email`: Sends confirmation emails to users with reservation details and a cancellation link.
   - `check_data_and_delete`: Checks if a reservation is expired and deletes it if necessary.

4. **Templates**: Contains HTML templates for rendering views.

## Project Functions with Visualization

1. **Index View**:

   - This view displays a list of upcoming events and allows users to make reservations.
   - It sends confirmation emails to users for successful reservations.

2. **Management View**:

   - This view allows users to manage their reservations and check for expired reservations.
   - Users can delete reservations that are not expired.

3. **Delete View**:

   - This view handles the deletion of user reservations and checks for expiration.
   - If a reservation is not expired, it can be deleted.

## Instalation

1. Download code from this repository and open it in IDE (for example Visual Studio Code).

2. Create a .env file inside food_order_system folder
   It has to contain the following data:

   ```
    # Replace variable values with your secrets / key / logins

    # Django settings
   DEBUG='TRUE_OR_FALSE'
   SECRET_KEY='YOUR_SECRET_KEY'

   # Database settings
   SQL_ENGINE=django.db.backends.postgresql
   POSTGRES_DB='DATABASE_NAME'
   POSTGRES_PASSWORD='DATABASE_PASSWORD'
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   # Email settings
   EMAIL_HOST_USER = "YOUR_EMAIL_ADDRESS"
   EMAIL_HOST_PASSWORD = "YOUR_EMAIL_PASSWORD"
   ```

3. Make sure you have docker installed and running

4. Run following commands from app directory

   ```
   cd .docker
   docker compose build
   ```

## Usage

1. Run following commands from app directory

   ```
   cd .docker
   docker compose build
   ```

2. Docker will install all requirments, create and apply migrations and then start server using the following commands from Dockerfile and docker-compose.yaml

   ```
   bash -c "python manage.py makemigrations
   && python manage.py migrate --run-syncdb
   && python manage.py runserver 0.0.0.0:8000"
   ```

3. Create a superuser account to access the Django admin panel (if needed):

   ```
   python manage.py createsuperuser
   ```

4. Access the application in your web browser at `http://localhost:8000/`.
