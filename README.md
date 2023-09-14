# User-Authentication-Assessment
# Django User Authentication and Authorization Project

This project is a simple Django-based web application that provides user authentication and authorization features. Users can register, log in, log out, and access protected views once authenticated. This README will guide you through the process of setting up and running the project on your local machine.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x recommended)
- Django (3.x recommended)
- Virtual environment (optional but recommended)

## Getting Started

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository:**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Munaelekwa/User-Authentication-Assessment.git

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd User-Authentication-Assessment

3. **Create a Virtual Environment (Optional):**

   It's a good practice to create a virtual environment for your project. Run the following command to create one:

   ```bash
   python -m venv venv

4. **Activate the virtual environment:**

   ```bash
   venv\Scripts\activate #windows
   source venv/bin/activate #macOs and Linux

5. **Install Dependencies:**

   Install the project's Python dependencies using pip:

   ```bash
   pip install -r requirements.txt

6. **Configure Database:**

   By default, this project uses SQLite for the database. You can configure your database settings in the settings.py file if you want to use a different database.

7. **Apply Migrations:**

   Apply the database migrations to create the necessary tables:

   ```bash
   python manage.py migrate


8. **Run the Development Server:**

   Start the Django development server:

   ```bash
   python manage.py runserver

The development server will be accessible at http://127.0.0.1:8000/.


9. **Explore the Application:**

   Open a web browser and access the application at http://127.0.0.1:8000/.
   You should be able to register, log in, and access protected views.
   Run Tests (Optional):

   To run the project's tests, use the following command:

   ```bash
   python manage.py test

**Project Structure**

   myapp/: The main Django app for user authentication and views.
   
   auth/: The project's settings and configuration.






