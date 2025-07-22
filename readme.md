💸 Expense Tracker
A simple web-based Expense Tracker built with Django, MySQL (WAMP Server), and a clean frontend using HTML, CSS, and JavaScript. This application allows users to track their income, expenses, and view transaction history in a minimal interface.

🚀 Features
✅ View current balance, total income, and total expenses on the homepage

➕ Add new transactions with a description and amount

📜 View recent transaction history

🛠️ Tech Stack
Component	Technology
Backend	Django
Database	MySQL (via WAMP Server)
Frontend	HTML, CSS, JavaScript

⚙️ Setup and Installation
1. 📥 Clone the Repository
bash
Copy
Edit
git clone https://github.com/aphex18/Expense_Tracker.git
cd Expense_Tracker
2. 🗄️ Set Up the MySQL Database
Start your WAMP server

Create a new MySQL database (e.g., expense_tracker)

3. 🛠️ Configure Database in settings.py
Update the DATABASES section in your Django project's settings.py:

python
Copy
Edit
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
4. 📦 Install Dependencies
Ensure you have a virtual environment activated and run:

bash
Copy
Edit
pip install -r requirements.txt
5. 🔧 Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6. ▶️ Start the Development Server
bash
Copy
Edit
python manage.py runserver
Open your browser and navigate to:
👉 http://localhost:8000

🧑‍💻 Usage
Add a transaction by entering a description and amount

View your current balance and recent transactions on the homepage

All data is saved in your MySQL database

📝 Notes
This is a basic project; features like user authentication, categories, and visual charts are not included

Ensure your MySQL configuration in settings.py matches your WAMP server setup

📁 Project Structure (Simplified)
arduino
Copy
Edit
Expense_Tracker/
│
├── expense_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── Expense_Tracker/
│   └── settings.py
│
├── db.mysql (MySQL setup)
├── requirements.txt
└── manage.py