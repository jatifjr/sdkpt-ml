# Project Name README

Welcome to Project Name! This README will guide you through setting up the project environment.

## Installation

1. **Install Python:**

   - If Python is not already installed, download and install it from [python.org](https://www.python.org/).
   - Make sure to add Python to your system's PATH during installation.

2. **Install Poetry:**

   - Poetry is a dependency management tool for Python. Install it by running the following command in your terminal or command prompt:
     ```bash
     curl -sSL https://install.python-poetry.org | python -
     ```
     or, on Windows:
     ```bash
     (Invoke-WebRequest -Uri https://install.python-poetry.org | Invoke-Expression)
     ```

3. **Install Dependencies:**

   - Once Poetry is installed, navigate to the project directory and run:
     ```bash
     poetry install
     ```
   - This command will install all project dependencies defined in the `pyproject.toml` file.

4. **Set Environment Variables:**

   - Copy the `.env.example` file to `.env` and set the necessary environment variables required for your project.
   - Make sure to populate any placeholders with actual values.

5. **Database Migration with Alembic:**
   - Alembic is a database migration tool for SQLAlchemy. Run the following command to initialize Alembic in your project:
     ```bash
     poetry run alembic init alembic
     ```
   - This command will create an `alembic` directory in your project.
   - Next, edit the `alembic.ini` file and set the appropriate database connection string under `[alembic] > sqlalchemy.url`.
   - Once configured, you can generate a migration script based on changes to your database models. For example:
     ```bash
     poetry run alembic revision --autogenerate -m "initial migration"
     ```
   - This will create a new migration script in the `alembic/versions` directory.
   - Finally, to apply the migration and update your database, run:
     ```bash
     poetry run alembic upgrade head
     ```
