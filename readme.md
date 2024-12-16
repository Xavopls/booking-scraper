# Django Web Scraper Application

This application is built using Django 5.14 and designed to scrape data from various websites. It is containerized with Docker and includes a scraping service powered by Selenium and Chrome in headless mode, as well as a PostgreSQL database. This guide will walk you through how to run the application locally or via Docker and how to access the different features it provides.

## Table of Contents

1. [Getting Started](https://www.notion.so/Django-Web-Scraper-Application-15ad6d13694a80778532cab1bda2ce48?pvs=21)
2. [Running the Application](https://www.notion.so/Django-Web-Scraper-Application-15ad6d13694a80778532cab1bda2ce48?pvs=21)
3. [Accessing Documentation](https://www.notion.so/Django-Web-Scraper-Application-15ad6d13694a80778532cab1bda2ce48?pvs=21)
4. [Environment Variables](https://www.notion.so/Django-Web-Scraper-Application-15ad6d13694a80778532cab1bda2ce48?pvs=21)
5. [Architecture Overview](https://www.notion.so/Django-Web-Scraper-Application-15ad6d13694a80778532cab1bda2ce48?pvs=21)
6. [Authentication](https://www.notion.so/Django-Web-Scraper-Application-15ad6d13694a80778532cab1bda2ce48?pvs=21)

---

## Getting Started

### Prerequisites

- Python 3.11
- Docker (for Selenium and PostgreSQL setup)

---

## Running the Application

### Docker Setup

To run the application using Docker, simply run:

```bash
docker-compose build
docker-compose up -d
```

This will set up the necessary containers, including the database (PostgreSQL) and Selenium with Chrome in headless mode.

### Local Setup

To run the application locally:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.11 installed.
3. Ensure Docker is installed and running for Selenium and PostgreSQL containers.
4. Copy the local environment configuration:

```bash
cp .env_local .env
```

The `.env` file contains the necessary configuration for Docker.

---

## Accessing Documentation

Once the application is running, you can access the following API documentation:

- **Swagger UI**: Navigate to localhost:8000/api/swagger-ui/
- **Redoc UI** (Alternative docs view): Navigate to localhost:8000/api/redoc/

The default path for the application is [localhost:8000](http://localhost:8000/).

---

## Environment Variables

You can modify the application’s behavior by changing the values in the `.env` file. These environment variables include settings for database connections, scraping configurations, and authentication.

---

## Architecture Overview

### Django Apps

The project is structured into two main apps:

1. **Core**:
    - Contains shared logic between apps.
    - Stores exceptions.
    - Holds normalized models.
2. **Scraper**:
    - Contains all scraping logic.
    - Manages the controllers that interact with the external websites.

### Use Cases and Services

- The **usecases** folder contains site-specific logic for scraping different websites (e.g., `booking.com`).
- The **services** folder contains the business logic, with each service dedicated to a specific site (e.g., a service for scraping booking.com).

### Models

The main models in the application are:

- **Booking**: Represents a booking entry.
- **Amenities**: Represents the amenities available for a booking.

These models have a many-to-many relationship, which is represented by an intermediary table linking `Booking` and `Amenities`.

---

## Authentication

### Bearer Token Authentication

All endpoints require authentication via a Bearer token.

- To obtain a token, use the login endpoint available in the Swagger UI.
- The default credentials are:
    - **Username**: admin
    - **Password**: 1234

---

## Troubleshooting

If you encounter issues or errors during setup, consider the following:

- Ensure your `.env` is correctly configured.
- Check Docker containers are running if using Docker.
- Review logs for any errors with the scraping service or database connection.

---

This README should help you get up and running with the application. If you have further questions or issues, feel free to reach out!