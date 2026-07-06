# Vehicle Parking Management System

A Django REST Framework CRUD API for managing vehicle parking records.

## Features

- Create parking records
- View all parking records
- Update parking records
- Delete parking records
- REST API using Django REST Framework

## Technologies Used

- Python 3.11
- Django
- Django REST Framework
- SQLite

## Installation

```bash
git clone <repository-url>
cd parking_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/parking/ | List all parking records |
| POST | /api/parking/ | Create a parking record |
| GET | /api/parking/<id>/ | Retrieve a parking record |
| PUT | /api/parking/<id>/ | Update a parking record |
| DELETE | /api/parking/<id>/ | Delete a parking record |

## Author

Benitta Priscilla