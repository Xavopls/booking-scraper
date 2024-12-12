# Sin título

# **Technical Test Documentation for Athlos Booking Scraper**

## **Overview**

This project is a **Booking Scraper** built with Django, which allows users to retrieve hotel data by scraping information from a specified hotel. The application exposes two main endpoints:

1. An authentication endpoint that returns a bearer token.
2. A hotel scraping endpoint that fetches hotel data based on the provided hotel name.

The application is packaged using **Docker** to streamline deployment and testing. You can run the application in a local environment or via Docker containers.

---

## **Prerequisites**

Before running the project, ensure that the following prerequisites are met:

- **Docker** and **Docker Compose** installed on your system.
- **Python 3.11** (or higher) installed locally if running outside of Docker.
- **Django 5.1.4** (or compatible) for local testing.
- The `.env` file configured with the appropriate environment variables.

---

## **Endpoints**

### 1. **Authentication Endpoint**

- **URL**: `http://localhost:8000/api/token/`
- **Method**: `POST`
- **Description**: Authenticates the user and returns a JWT bearer token to be used for subsequent requests.

### Request:

- **Headers**:
    - Content-Type: application/json
- **Body**: (Example)
    
    ```json
    
    {
      "username": "your-username",
      "password": "your-password"
    }
    
    ```
    

### Response:

- **Status**: 200 OK
- **Body**:
    
    ```json
    
    {
      "access": "your-jwt-access-token",
      "refresh": "your-jwt-refresh-token"
    }
    
    ```
    

### 2. **Hotel Scraping Endpoint**

- **URL**: `http://localhost:8000/api/hotels/scrape?name=Hotel%20California`
- **Method**: `GET`
- **Description**: Fetches the hotel data for the provided hotel name.

### Request:

- **Headers**:
    - Authorization: Bearer `{access_token}`
- **Query Parameters**:
    - `name`: The name of the hotel (e.g., "Hotel California").

### Response:

- **Status**: 200 OK
- **Body**:
    
    ```json
    {
      "name": "Hotel California",
      "location": "Santa Monica, California",
      "average_price": 250.00,
      "description": "A beautiful hotel with breathtaking views.",
      "review_mark": 8.5,
      "number_of_comments": 1000,
      "photo_urls": [
        "https://cf.bstatic.com/xdata/images/hotel/square240/70484675.webp"
      ],
      "amenities": ["Pool", "Gym", "Wi-Fi"]
    }
    ```
    

---

## **Docker Setup**

### 1. **Building the Docker Container**

To set up the project using Docker, you will need to build the container and run it using Docker Compose. This will start the application in a containerized environment with all necessary dependencies.

### Steps to build the Docker container:

1. **Clone the repository (if not already done)**:
    
    ```bash
    git clone https://your-repository-url.git
    cd athlosscraper
    ```
    
2. **Set up the `.env` file**:
    - Copy `.env.example` to `.env` and set the environment variables accordingly. These variables are used for database configuration, Django settings, and other environment-specific configurations.
3. **Build the Docker image**:
    
    ```bash
    docker build -t athlosscraper .
    ```
    
4. **Run the Docker containers**:
    
    ```bash
    docker-compose up -d
    ```
    

This will start the containers in the background and set up the application, database, and other necessary services.

### 2. **Docker and Environment Configuration**

- **Local Development**: By default, the Docker setup assumes that services (like the database) are hosted on the `localhost`.
- **Dockerized Environment**: If you are running the setup with Docker containers, you need to modify the `.env` file to point to the Docker containers instead of `localhost`.
    - Change any URLs or service hostnames that point to local services to refer to the corresponding Docker service names.

Example:

```bash
bash
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## **Environment Variables (.env)**

The `.env` file contains the necessary environment variables for configuring the application. Here is an example of what the `.env` file might look like:

```bash
bash
Copiar código
# Database Configuration
POSTGRES_DB=athlosscraper_db
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Django settings
DEBUG=True
SECRET_KEY=your-secret-key

# JWT Authentication settings
ACCESS_TOKEN_LIFETIME=60
SLIDING_TOKEN_LIFETIME=30
SLIDING_TOKEN_REFRESH_LIFETIME=1

```

Make sure to replace the placeholders with your actual values. When using Docker, modify the `POSTGRES_HOST` and other environment settings to match the Docker container configuration.

---

## **Running the Application Locally**

If you want to run the application without Docker, you can do so by setting up your environment locally with the following steps:

1. **Set up a virtual environment**:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows
    ```
    
2. **Install dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Run migrations**:
    
    ```bash
    python manage.py migrate
    ```
    
4. **Start the development server**:
    
    ```bash
    python manage.py runserver
    ```
    
    The application will be available at `http://localhost:8000`.