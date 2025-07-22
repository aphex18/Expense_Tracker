# Expense Tracker

A basic **Expense Tracker** web application built with **Django**, **MySQL** (WAMP server), and a simple frontend using **HTML, CSS, and JavaScript**.

## Features

- View current **balance**, **income**, and **expense** totals on the homepage
- **Add new transactions** with description and amount
- **View transaction history** with recent entries

## Tech Stack

| Component  | Technology            |
|------------|----------------------|
| Backend    | Django               |
| Database   | MySQL (WAMP server)  |
| Frontend   | HTML, CSS, JavaScript|

## Setup and Installation

1. **Clone the Repository**

<<<<<<< HEAD
    git clone https://github.com/aphex18/Expense_Tracker.git
        
=======
    git clone https://github.com/aphex18/Expense_Tracker.git  
>>>>>>> b5f98c8311eca5b159c7166be8847b64c01635ca
    cd Expense_Tracker


2. **Set Up the MySQL Database**
- Start your **WAMP server**
- Create a new database, e.g., `expense_tracker`

3. **Configure Database in Django**
- Edit `settings.py` in your Django project:
  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'expense_tracker',
          'USER': 'your_mysql_user',
          'PASSWORD': 'your_mysql_password',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

4. **Install Dependencies**

    pip install -r requirements.txt


5. **Apply Migrations**

    python manage.py makemigrations
    python manage.py migrate


6. **Start the Development Server**

    python manage.py runserver

- Open your browser and go to `http://localhost:8000`

## Usage

- Enter the **description** and **amount** of your expense/income and submit the form.
- See your current balance, and recent transactions.
- All data is stored in your MySQL database.

## Notes

- This is a **basic project** to track expenses; advanced features like authentication, categories, and charts are not included.
- Make sure your database configuration in `settings.py` matches your local WAMP server setup.
