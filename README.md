# Weather-App Project

## Description
This project is a Weather App developed using Django and Bootstrap for UI design.

## Features
- Weather according to the user location.
- Weather according to other cities.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/SaugatMgr/Weather-App.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Weather-App
    ```
3. **Create a virtual environment:**
    ```bash
    python -m venv .venv
    ```
4. **Activate the virtual environment:**

    On Windows:

    ```bash
    .\.venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source .venv/bin/activate
    ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

A `.env.local` file needs to be created in the main project folder with the following contents:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=postgres://db_user:db_password@localhost:db_port_number/db_name
WEATHER_API_KEY=your_weather_api_key
CORS_ALLOW_ALL_ORIGINS=True # for mobile app to send requests to django rest framework api
```

Then follow the following steps:
1. **Create a superuser:**
    - Run the following command and follow the prompts:
        ```bash
        python manage.py createsuperuser
        ```
2. **Migrate Changes:**
    ```bash
    python manage.py migrate
    ```
3. **Run the server:**
    ```bash
    python manage.py runserver
    ```
    
## Usage
Note: At first, you need to register and create API key for the Weather API used in this project. Go to [https://openweathermap.org] and register account then navigate to Account > My API keys. Then you need to generate API key and wait few hours for the API key to work. Until then paste the API key to the respective variable in the env file.

## Technologies Used
- Django for the web framework
- Jazzmin for the admin panel customization
- Bootstrap for UI
