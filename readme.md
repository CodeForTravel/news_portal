# news_portal

### Project setup

- Clone the repository: https://github.com/CodeForTravel/news_portal.git

  ```bash
  git clone https://github.com/CodeForTravel/news_portal.git
  ```

- Create a **.env** file inside the project directory and copy from **env_example** to **.env** and set the environment variables according to the needs.

  Such as, set your local `postgres` user name and password to the DB_USER and DB_PASSWORD:

  ```bash
  # example
  DB_NAME=example_db
  DB_USER=postgres
  DB_PASSWORD=admin1234
  DB_PORT=5432
  EMAIL_NOREPLY=email_to_send_email_with_sendgrid
  ```

- Create an account in **https://newsapi.org/** get the API_KEY and set is to .env file:

  ```bash
  NEWS_API_KEY=your_news_api_key
  ```

- Create an account in **https://sendgrid.com//** get the API_KEY and set is to .env file:

  ```bash
  SENDGRID_API_KEY=your_nedgrid_api_key
  ```

- Create a virtual environment named **env** with Python's **venv**:

  ```bash
  python3 -m venv env
  ```

  - Activate the virtual environment (For Ubuntu):
    ```bash
    source env/bin/activate
    ```
  - For Windows:
    ```bash
    env\Scripts\activate
    ```

- Install all required packages:

  ```bash
  pip install -r requirements.txt
  ```

- Run **migrate** command to propagate the migrations files into the db

  ```bash
  python manage.py migrate
  ```

- Create admin account

  ```
  python manage.py createsuperuser
  ```

- Run Django server

  ```bash
  python manage.py runserver ip_address:port
  ```

### Fetch news source

- Fetch news source with following command:
  ```bash
  python manage.py fetch_news_sources
  ```

---

- Install packages for the Front-end

  ```bash
  # From "frontend" directory
  cd frontend
  yarn install
  ```

- Serve frontend in **development** mode

  ```bash
  # From "frontend" directory
  cd frontend
  yarn run dev
  ```

- Build **app.js** with (in **production**)

  ```bash
  # From "frontend" directory
  cd frontend
  yarn run build
  ```

### Makefile

- Delete `.pyc` files with the command:

  ```bash
  make clean
  ```
