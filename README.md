# Emporium

Emporium is a project that consists of a Django backend server and a React frontend application. The backend server creates a database with three tables and provides an API endpoint to perform CRUD (Create, Read, Update, and Delete) operations. The frontend application displays the data from the backend server in a table and enables sorting, filtering, and searching of the data.
## Prerequisites

Before running the project, you must install and start memcached by running the following commands:

- `brew install memcached`
- `brew services start memcached`


## How to run

To run the project, follow these steps:

1. Clone the repository with `git clone git@github.com:esrefozturk/emporium.git`

2. Navigate to the backend directory and run the following commands:
    - `pip install -r requirements.txt`
    - `python manage.py migrate`
    - `python manage.py import`
    - `python manage.py runserver`

3. Navigate to the frontend directory and run the following commands:
    - `npm install`
    - `npm start`

## Next steps

Here are some possible next steps to improve the project:

- Productionize the project by adding integrations such as Docker, Postgresql, and gunicorn.
- Review the database columns to set proper types according to the data structure.
- Implement Add, Edit, and Delete functions on the frontend.
- Add documentation

