# Django REST Framework Boilerplate

Template for quick-setup of DRF projects with properly refactored code.

## Development Setup

Follow the following steps if you want to set this project up on your own machine.

1. Clone the repository using:  `git clone <link.git>`
2. Move into the repository directory using:    `cd folderName`
3. Create a Python virtual environment: `python -m venv env`
4. Activate the virtual environment:    `source env/scripts/activate`
5. Update `PIP` to the specified version:   `python -m pip install --upgrade pip==22.0.4`
6. Install `PIP-Tools` using:   `pip install pip-tools`
7. Compile the `requirements.in` file using:    `pip-compile`
8. Install the dependencies:    `pip install -r requirements.txt`
9. Install the `spacy` model using: `python -m spacy download en_core_web_md`
10. Copy the `.env` file to the directory root.

    - Create a `PostgreSQL` database in your machine as per the `Database Settings` in the `.env` file.
        - `PostgreSQL` setup instructions can be found [here](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm).
        - `PGAdmin` is a recommended tool for managing a `PostgreSQL` database and instructions for its own setup can be found [here](https://www.pgadmin.org/download/).
    - Alternatively, you can use Amazon's [`RDS`](https://aws.amazon.com/rds/) service to create a managed instance of a `PostgreSQL` database.

        _If using Amazon's_ `RDS`_, change the following values in your_ `.env` _file to reflect the values of the_ `RDS` _database._

        - `PGHOST`: _The host URL of the RDS instance._
        - `PGPORT`: _The port on the host URL the database is accessed through._
        - `PGDATABASE`: _The name of the database instance._
        - `PGUSER`: _The username with which to log into the database._
        - `PGPASSWORD`: _The password for the username above with which to log into the database._

    _Alternately, you can also use a [`database_URI`](https://pypi.org/project/dj-database-url/) in the `settings` page to connect to the database._

    __Eg:__ __`PGUSER`:`PGPASSWORD`@`PGHOST`:`PGPORT`/`PGDATABASE`__

11. Create the necessary migrations:    `./manage.py makemigrations`
12. Migrate the database:   `./manage.py migrate`
13. Create a new `SuperUser` for the system using:  `./manage.py createsuperuser`

    Recommended values for `SuperUser`:

    ```shell
    - username: admin
    - email: admin@admin.com
    - password: password
    ```

14. Start the server:   `./manage.py runserver`

## .env File Format

```env
APP_NAME = "Name of the Project you want to have"

# Site Settings:
SECRET_KEY = 'some_random_32_bit__hex_key'
DEBUG = True/False
ENV_TYPE = 'DEV/PROD'
ALLOWED_HOSTS = 'host_01 host_02 host_03 etc'

# Database Settings:
PGDATABASE = 'name_of_db'
PGHOST = 'host/url_of_db'
PGPORT = 'port_of_db'
PGUSER = 'username_for_db'
PGPASSWORD = 'password_for_db'

# Internationalization Settings:
LANGUAGE_CODE = 'language_code'
TIME_ZONE = 'standard_time_location as city/continent'
USE_I18N = True/False
USE_TZ = True/False

## Email Settings:
EMAIL_HOST = ' '
EMAIL_USE_TLS = True/False
EMAIL_USE_SSL = True/False
EMAIL_PORT = int
EMAIL_HOST_USER = " "
EMAIL_HOST_PASSWORD = "Generated App Password"
```

## Documentation

Post the [Postman Documentation](link-to-documentation-here) here as a markdown hyperlink.

## Author(s)

1. [Profile Name](link-to-profile)
