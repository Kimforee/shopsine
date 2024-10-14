# Django Shop Registration and User Search System
deployed link : `shopsine-production.up.railway.app/`

This is a Django project that allows shops to register with their details (name, latitude, and longitude) and lets users search for shops based on their current location using latitude and longitude. The system calculates the distance between the user's location and the registered shops using the Haversine formula and returns a sorted list of nearby shops.

## Landing page
![image](https://github.com/user-attachments/assets/e799b41a-7612-4c92-bc82-9d68196ff9b1)

## Register Shop
![image](https://github.com/user-attachments/assets/404838cf-b4d8-43e9-88e7-3c0d9ef9c6ca)
![image](https://github.com/user-attachments/assets/713204ae-40d8-4241-a46c-2a5f7935dad6)

## Search Shop
![image](https://github.com/user-attachments/assets/166594ee-f84a-4374-9a16-72bb1cfd45bb)
![image](https://github.com/user-attachments/assets/9b5ecd41-1b9d-4cf4-aa27-e5269f9c9271)

## Rest API (DRF)
![image](https://github.com/user-attachments/assets/649bbba0-dabe-4213-949e-d3c916d56de9)

## Features

- Shop Registration: Register a shop with its name, latitude, and longitude.
- User Search: Users can search for nearby shops by providing their current location (latitude and longitude).
- Distance Calculation: The Haversine formula is used to calculate the distance between the user and each shop.
- REST APIs: Built using Django Rest Framework (DRF) with proper API documentation.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django 4.x
- Django Rest Framework (DRF)
- Postgres

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-shop-registration.git
    cd django-shop-registration
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Run the server:**

    ```bash
    python manage.py runserver
    ```

## Project Structure

```
src/
├── manage.py                 # Django management script
├── shops/
│   ├── admin.py              # Shop model admin configuration
│   ├── apps.py               # Shop app configuration
│   ├── forms.py              # Shop registration form
│   ├── models.py             # Shop model definition
│   ├── serializers.py        # Shop serializers for DRF
│   ├── urls.py               # URL routing for the app
│   ├── utils.py              # Utility functions (Haversine function)
│   ├── views.py              # Views for handling API requests
│   ├── tests.py              # Unit and API tests
│   └── ...
├── project_name/
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project-level URL routing
│   └── ...
```

## APIs

### 1. Shop Registration

- **Endpoint**: `/shops/api/register/`
- **Method**: `POST`
- **Description**: Registers a new shop with its name, latitude, and longitude.

**Request Body:**

```json
{
  "name": "My Shop",
  "latitude": 40.730610,
  "longitude": -73.935242
}
```

**Response:**

```json
{
  "id": 1,
  "name": "My Shop",
  "latitude": 40.730610,
  "longitude": -73.935242
}
```

### 2. Search Shops by Location

- **Endpoint**: `/shops/api/search/`
- **Method**: `GET`
- **Description**: Search for nearby shops by providing user's current latitude and longitude.

**Query Parameters**:

- `latitude`: User's latitude
- `longitude`: User's longitude

**Example Request**:

```http
GET /shops/api/search/?latitude=40.730610&longitude=-73.935242
```

**Response**:

```json
[
    {
        "shop": {
            "id": 1,
            "name": "Test Shop",
            "latitude": 40.73061,
            "longitude": -73.935242
        },
        "distance": 0.0
    },
    {
        "shop": {
            "id": 2,
            "name": "Another Shop",
            "latitude": 34.052235,
            "longitude": -118.243683
        },
        "distance": 3936.5
    }
]
```

## Running Tests

This project includes unit tests for the Haversine distance calculation and the API functionality.

Run tests with the following command:

```bash
python manage.py test
```

## Haversine Formula

The project uses the Haversine formula to calculate the great-circle distance between two points on the earth's surface based on their latitude and longitude. The function is located in `shops/utils.py`.

## License

This project is licensed under the MIT License.
```

### Key Sections:
1. **Features**: Brief overview of what the system offers.
2. **Prerequisites and Installation**: Step-by-step guide to setting up the project.
3. **Project Structure**: Explanation of the file structure.
4. **APIs**: Detailed descriptions of the API endpoints, request examples, and expected responses.
5. **Running Tests**: Instructions for running the included tests.
6. **Haversine Formula**: A brief mention of the core distance calculation method.
