⚠️ Important note:
For security reasons, the external database used by this application is not publicly accessible.
If you want to fully interact with this app (create, update, or delete data), you can contact me (+52 246-239-2759) so database access can be temporarily enabled.
Otherwise, if the Aiven database is not enabled, no commands will work and the project will not function, even if it has been correctly cloned from GitHub.

### Install and configure dependencies

0. Create a virtual environment with Python of your choice and activate it.
    - It is common to create it in C:// (in Windows, for example)
1. Go to the folder that contains the requirements file.
2. Run `pip install -r requirements.txt`.

### Migrations

1. Go to the `financial` folder (the one that contains the `manage.py` file).
2. Run `python manage.py makemigrations` to create the migrations in the DB.
3. Run `python manage.py migrate` to migrate the data.

### Create superuser
⚠️ Admin Panel Notice

The Django admin panel is currently not enabled for this project.
At this moment, the admin interface is not required and will not be useful for interacting with the application.

For this reason, creating a superuser is optional and not necessary to run or test the project features.

1. Go to the `financial` folder (the one that contains the `manage.py` file).
2. Run `python manage.py createsuperuser`.
3. Answer the questions that will be prompted in the terminal.
4. Access to "localhost:8000/admin/".
5. Login and check everything is fine.

### Run development mode

1. Go to the `financial` folder (the one that contains the `manage.py` file).
3. Run `python manage.py runserver`.

Project Architecture
This project is composed of two main applications:

🔹 App 1 (consuming_api) – External API (Postman usage)
Backend application developed with Django REST Framework, designed to interact with the external REST Countries API.
Intended to be used directly from Postman.
Includes documentation (Check the "Documentation_file.md" to handle the consuming_api app) explaining how to perform requests from scratch.
No additional database configuration is required for basic usage.

🔹 App 2 (ecommerce) – Backend API + Frontend Client

Backend application developed with Django REST Framework, built from scratch and designed to be consumed by an external frontend client developed with JavaScript and Bootstrap.

The backend manages custom models, static file handling (including image uploads), and communication with an external database.

The project is configured to allow interaction with a frontend client deployed on Vercel.

The frontend vercel link allows users to visualize and interact with the application.

Once you have confirmed that the server is running correctly by executing python manage.py runserver without any issues, and the server is successfully running in your terminal, you can access the following link to test all functionalities from the frontend client, which will interact with your locally running Django backend server:
https://online-ecommerce-ten.vercel.app/