# Books Exchange App

A Django-based fullstack application for exchanging books between users. Users can list their books, browse others' books, and propose trades. Customized admin panel for bulking books from apis.

## Features

- User authentication
- Browse and search for books
- Request book exchanges
- Accept or decline exchange offers
- Responsive design
- Async books import

## Technologies Used

- Django
- PostgreSQL
- Bootstrap
- Docker
- Celery
- Redis
- Bootstrap

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Python

### Clone the Repository

```bash
git clone https://github.com/yourusername/books-exchange-app.git
cd books-exchange-app
```

### Build and Run with Docker

1. **Create a `.env` file**

   Create a file named `.env` in the root directory of the project and add your environment variables, such as presented in the .env-example:

2. **Build the Docker containers**

   Run the following command to build the Docker images:

   ```bash
   docker-compose build
   ```

3. **Run the application**

   Start the application and database containers using:

   ```bash
   docker-compose up
   ```

5. **Create a Superuser (Optional)**

   If you want to access the Django admin, you can create a superuser account by accessing the web's container console:

   ```bash
   python manage.py createsuperuser
   ```

6. **Access the Application**

   You can access the application at `http://localhost:8000`. If you created a superuser, you can log in to the admin interface at `http://localhost:8000/admin`.

### Usage

- **Register**: Sign up for a new account.
- **Add Books**: Users can add books they want to exchange.
- **Browse Books**: View and search for available books.
- **Request Exchange**: Propose a trade with other users.
- **Respond to Offers**: Accept or decline exchange requests.
- **Bulk import**: Importing books with async worker from api.


### Docker Commands

- **Stop the containers**: 
   ```bash
   docker-compose down
   ```

### Configuration

- Update the `docker-compose.yml` file to configure your services, volumes, and networks as necessary.
- Modify the Django settings in `settings.py` to match your environment.