# 🚀 DjangoCRM

A clean, professional **Contact Management CRM** built with Django and Python. Manage your leads, prospects, and customers from a single, elegant dashboard.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📸 Pages

| Page | Route |
|---|---|
| Login | `/login/` |
| Register | `/register/` |
| Dashboard | `/dashboard/` |
| Contacts | `/contacts/` |
| Add Contact | `/contacts/add/` |
| Edit Contact | `/contacts/<id>/edit/` |
| Delete Contact | `/contacts/<id>/delete/` |

---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout
- 👥 **Contact Management** — Add, Edit, Delete contacts
- 🔍 **Search** — Filter contacts by name, email, or company
- 📊 **Dashboard** — Live stats: Total, Leads, Prospects, Customers
- 🏷️ **Status Tagging** — Lead → Prospect → Customer pipeline
- 🔒 **Data Isolation** — Each user only sees their own contacts
- 💅 **Professional UI** — Custom CSS, no Bootstrap or Tailwind needed

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Framework | Django 4.x |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | HTML5 + Custom CSS |
| Fonts | Plus Jakarta Sans, Space Grotesk |
| Auth | Django `contrib.auth` |

---

## ⚡ Quick Start

### 1. Clone or unzip the project

```bash
unzip djangocrm_project.zip
cd djangocrm
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Open in browser

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
djangocrm/
│
├── djangocrm/                  # Project configuration
│   ├── settings.py             # App settings
│   ├── urls.py                 # Root URL config
│   └── wsgi.py                 # WSGI entry point
│
├── crm/                        # Main CRM application
│   ├── models.py               # Contact data model
│   ├── views.py                # Page logic & controllers
│   ├── forms.py                # Login, Register, Contact forms
│   ├── urls.py                 # CRM URL routes
│   └── migrations/             # Database migrations
│
├── templates/
│   └── crm/
│       ├── base.html           # Sidebar layout (authenticated)
│       ├── login.html          # Login page
│       ├── register.html       # Registration page
│       ├── dashboard.html      # Stats & recent contacts
│       ├── contacts.html       # Full contacts list
│       ├── contact_form.html   # Add / Edit contact form
│       └── confirm_delete.html # Delete confirmation
│
├── static/
│   └── css/
│       └── style.css           # All custom styles
│
├── manage.py
├── db.sqlite3                  # SQLite database (auto-created)
└── README.md
```

---

## 🗄️ Contact Model

```python
class Contact(models.Model):
    user        = ForeignKey(User)       # Owner (logged-in user)
    first_name  = CharField             # Required
    last_name   = CharField             # Required
    email       = EmailField            # Required
    phone       = CharField             # Optional
    company     = CharField             # Optional
    status      = CharField             # lead | prospect | customer
    notes       = TextField             # Optional
    created_at  = DateTimeField         # Auto set
    updated_at  = DateTimeField         # Auto updated
```

---

## 🔄 Sales Pipeline

```
Lead  ──►  Prospect  ──►  Customer
```

| Status | Meaning |
|---|---|
| **Lead** | New, unqualified contact |
| **Prospect** | Interested, being evaluated |
| **Customer** | Converted / paying client |

---

## 🚀 Deploy to Production

### Option 1 — Railway (Recommended, Free)

1. Push project to a GitHub repository
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add environment variable: `DJANGO_SETTINGS_MODULE=djangocrm.settings`
4. Done — live in ~2 minutes

### Option 2 — Render (Free)

1. Push to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Build command: `pip install django && python manage.py migrate`
4. Start command: `gunicorn djangocrm.wsgi`

### Option 3 — PythonAnywhere (Free)

1. Upload zip at [pythonanywhere.com](https://pythonanywhere.com)
2. Unzip in console, configure WSGI file
3. Set static files path in dashboard

### Before deploying, update `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')  # Use env variable
```

---

## 🔐 Default Demo Credentials

> ⚠️ Change these before deploying to production!

```
Username: admin
Password: admin123
```

---

## 🛣️ Roadmap / What to Add Next

- [ ] Password reset via email
- [ ] Kanban deal pipeline board
- [ ] Pagination on contacts list
- [ ] Export contacts to CSV
- [ ] Analytics charts (Chart.js)
- [ ] Notes history with timestamps
- [ ] REST API with Django REST Framework
- [ ] PostgreSQL for production

---

## 📄 License

This project is open source under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙌 Built With

- [Django](https://www.djangoproject.com/) — The web framework for perfectionists with deadlines
- [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) — UI font
- [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) — Brand font
