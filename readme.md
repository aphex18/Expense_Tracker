Expense Tracker
Expense Tracker is a beginner-friendly Django-based web application designed to help users manage and monitor their personal finances efficiently. This project serves as an excellent first step into full-stack development, combining backend, database, and frontend fundamentals in a clean and modular codebase.

Features
User Authentication: Secure registration and login powered by Django’s built-in authentication system for personalized expense management.

Transaction Management: Add, view, and track income and expenses with a simple, intuitive interface.

Real-Time Summary: Dashboard displays current balance, total income, and total expenses.

Database Integration: Uses MySQL or SQLite for robust data persistence and demonstrates database setup and migrations.

Technology Stack
Layer	Technology
Backend	Django (Python)
Database	MySQL (optional) / SQLite
Frontend	HTML, CSS, JavaScript
Getting Started
Prerequisites
Python 3.6+

MySQL Server (WAMP recommended for MySQL; SQLite is default)

Git

Installation Steps
Clone the repository

bash
git clone https://github.com/aphex18/Expense_Tracker.git
cd Expense_Tracker
Set up the database

For MySQL:

Start your MySQL server (e.g., via WAMP).

Create a database, e.g., expense_tracker.

Update the database settings in expense_tracker/settings.py accordingly.

For SQLite:

No setup needed as it’s the default database.

Optional: Create and activate a virtual environment

bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Manage migrations

bash
python manage.py makemigrations
python manage.py migrate
Run the application

bash
python manage.py runserver
Access

Open http://127.0.0.1:8000/ in your browser.

Usage
Register a new user or log in with existing credentials.

Add income or expense transactions through the dashboard.

View your current balance and transaction history.

Log out to maintain your account security.

Project Structure
text
EXPENSE_TRACKER/
│
├── expense_tracker/           # Django project configuration
│   ├── __pycache__/
│   ├── middleware/            # Custom middleware 
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Main settings file
│   ├── urls.py                # Project-wide routing
│   ├── wsgi.py
│   └── public/
│        └── static/
│             └── css/
│                  └── main.css   # Custom CSS styles
│
├── tracker/                   # Core Django app — models, views, templates
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── venv/                      # Python virtual environment (excluded from version control)
│
├── .env                       # Environment variables file (not committed)
├── .env.sample                # Sample environment variables template
├── .gitignore                 # Git ignore rules
├── db.sqlite3                 # SQLite database file django default database # in this project mysql(wamp server) is used
├── manage.py                  # Django management script
├── readme.md                  # Project documentation
└── requirements.txt           # Python dependencies
