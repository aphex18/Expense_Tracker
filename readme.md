
# 💸 Expense Tracker

**Expense Tracker** is a beginner-friendly, full-stack web application built with **Django**, **MySQL (or SQLite)**, and basic frontend technologies. It helps users securely manage their personal finances by tracking income and expenses in real-time.

This project is ideal for **new developers** exploring **full-stack development**, covering backend logic, database integration, frontend presentation, user authentication, and deployment-ready structure.

---

## 🚀 Features

- 🔐 **User Authentication**  
  Secure login and registration using Django's built-in auth system.

- 💰 **Transaction Management**  
  Add, view, and manage income or expense entries.

- 📊 **Real-Time Dashboard**  
  Displays current balance, total income, and total expenses.

- 🗄️ **Database Integration**  
  Supports **MySQL** (with WAMP) and **SQLite** for persistent data storage.

---

## 🧰 Technology Stack

| Layer     | Technology             |
|-----------|------------------------|
| Backend   | Django (Python)        |
| Database  | MySQL (WAMP) / SQLite  |
| Frontend  | HTML, CSS, JavaScript  |

---

## ⚙️ Getting Started

### ✅ Prerequisites

- Python 3.6+
- MySQL Server (WAMP recommended) or use SQLite (default)
- Git

---

### 📦 Installation Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/aphex18/Expense_Tracker.git
cd Expense_Tracker
```

#### 2. Set Up the Database

**For MySQL (recommended):**

- Start WAMP/MySQL server.
- Create a database named `expense_tracker`.
- Update the `DATABASES` section in `expense_tracker/settings.py`:

```python
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

**For SQLite (default & no config needed):**  
Skip DB setup — SQLite will work out of the box.

#### 3. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit 👉 **http://127.0.0.1:8000/** in your browser.

---

## 👨‍💼 Usage

1. **Register** a new user or **log in**.
2. **Add income or expenses** via the dashboard form.
3. See **real-time updates** of your financial status.
4. **Log out** securely when finished.

---

## 📁 Project Structure

```
EXPENSE_TRACKER/
│
├── expense_tracker/           # Django project configuration
│   ├── __pycache__/           # Compiled Python bytecode
│   ├── middleware/            # Custom middleware (optional)
│   ├── __init__.py            # Marks this directory as a Python package
│   ├── asgi.py                # ASGI entrypoint for async deployments
│   ├── settings.py            # Main settings file (DB, static, apps)
│   ├── urls.py                # Project-wide URL routing
│   ├── wsgi.py                # WSGI entrypoint for deployment
│   └── public/
│        └── static/
│             └── css/
│                  └── main.css   # Custom CSS styles
│
├── tracker/                   # Core Django app — models, views, templates
│   ├── __pycache__/           # Python bytecode cache
│   ├── migrations/            # Django migration files
│   ├── templates/             # HTML templates (rendered by views)
│   ├── __init__.py            # App module init
│   ├── admin.py               # Admin panel configuration
│   ├── apps.py                # App configuration class
│   ├── models.py              # Database models (Transaction, etc.)
│   ├── tests.py               # Unit tests for this app
│   ├── urls.py                # App-specific URL routes
│   └── views.py               # Core business logic
│
├── venv/                      # Python virtual environment (excluded from version control)
│
├── .env                       # Environment variables file (not committed)
├── .env.sample                # Sample environment file for reference
├── .gitignore                 # Git ignore rules for files/folders
├── db.sqlite3                 # SQLite database file (for quick dev setup)
├── manage.py                  # Django management script
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---


## 📌 Why This Project?

This Expense Tracker is a **solid first step into full-stack development**, teaching you:

- Backend routing and logic with Django
- Database integration and ORM concepts
- Frontend templating and interaction
- Secure user authentication
- Clean, modular project structure

---

