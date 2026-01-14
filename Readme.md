# 🏎️ F1 Ticket Booking System

A full-stack web application for booking Formula 1 race tickets, built using **Django** and **MySQL**, featuring secure user authentication, seat availability management, and a responsive F1-themed UI.

---

## 🚀 Features

- 🏁 View upcoming F1 races with circuit images
- 🎟️ Browse ticket categories (General, Grandstand, VIP)
- 🪑 Real-time seat availability tracking
- 🔒 Secure user authentication (login & logout)
- 👤 User-specific booking history (“My Bookings”)
- ✅ Booking confirmation flow
- 🎨 Responsive F1-themed UI using Bootstrap & custom CSS
- 🛡️ Secure logout via POST (Django 4+/5 compliant)

---

## 🛠️ Tech Stack

**Backend**
- Python 3.11+
- Django 4 / 5
- MySQL
- Django ORM

**Frontend**
- HTML5
- Bootstrap 5
- Custom CSS (F1 theme)

**Other**
- Django Authentication
- Django Admin
- Pillow (image handling)

---

## 📂 Project Structure


---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd F1
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'f1_ticket_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000

✅ This README is **interview-safe** and **GitHub-ready**.

---

# 3️⃣ DEPLOYMENT GUIDE (BEGINNER FRIENDLY)

We’ll use **Render** (simple, free-tier friendly).

---

## 🧱 STEP 1: Create `requirements.txt`

Run this locally:

```bash
pip freeze > requirements.txt
