# Lekki Foodie Restaurant API

A Django REST Framework API for managing restaurant information in the Lekki area.

## Features

- List all restaurants
- Create new restaurants
- Retrieve details of a specific restaurant
- Update restaurant information
- Delete restaurants
- RESTful API endpoints

## Technologies Used

- Django 6.0.2
- Django REST Framework
- SQLite3 (development database)

## Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone [repository-url]
cd lekki_foodie
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

### 3. Activate the Virtual Environment

- On Windows:
  ```bash
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

*Note: If there's no requirements.txt, install the core dependencies:*
```bash
pip install django djangorestframework
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

All API endpoints are prefixed with `/api/`:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/restaurants/` | List all restaurants |
| POST | `/api/restaurants/` | Create a new restaurant |
| GET | `/api/restaurants/<id>/` | Retrieve a specific restaurant |
| PUT/PATCH | `/api/restaurants/<id>/` | Update a specific restaurant |
| DELETE | `/api/restaurants/<id>/` | Delete a specific restaurant |

## Example Usage

### List Restaurants
```bash
curl http://127.0.0.1:8000/api/restaurants/
```

### Create a Restaurant
```bash
curl -X POST http://127.0.0.1:8000/api/restaurants/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Example Restaurant", "location": "Lekki Phase 1", "rating": 4.5}'
```

## Project Structure

```
lekki_foodie/
├── lekki_foodie/          # Django project settings
├── restaurants/           # Restaurants app
│   ├── migrations/        # Database migrations
│   ├── models.py          # Restaurant model
│   ├── serializers.py     # Restaurant serializer
│   ├── views.py           # API views
│   ├── urls.py            # App URL configuration
│   └── tests/             # Tests (if any)
├── manage.py              # Django management script
└── db.sqlite3             # SQLite database (development)
```

## Admin Interface

Access the Django admin interface at `http://127.0.0.1:8000/admin/` using the superuser credentials:

- **Username:** lekki_foodie
- **Email:** lekkifoodie77@gmail.com
- **Password:** Jesus_lekki77

*Note: These credentials are provided for convenience. In a production environment, you should create your own superuser and change these credentials.*

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.