````
# 📝 Blog App (Django)

A full-featured blog application built with **Python** and **Django**. This app allows users to create, read, update, and delete blog posts, with user authentication and an admin panel for content management.

👉 **Live Demo:** [https://blog-app-ik5e.onrender.com/](https://blog-app-ik5e.onrender.com/)

---

## 🚀 Features

- ✅ User registration and login
- 📝 Create, update, and delete blog posts
- 🔐 Authenticated access to editing and deletion
- 🗂️ Admin dashboard with Django Admin

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default) 
- **Authentication:** Django's built-in auth system

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip
- Django

### Setup Instructions

```bash
git clone https://github.com/iamshammas/blog-app.git
cd blog-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate DB and create superuser
python manage.py migrate
python manage.py createsuperuser

# Run the server
python manage.py runserver
````

Visit: `http://127.0.0.1:8000/`

---

## 🔐 Default User Credentials

For demo/testing purposes:

```
Username: user1
Password: user1
```

## 📁 Project Structure

```
blog-app/
├── blog/                 # Blog app logic
├── blog_app/             # Project settings
├── templates/            # HTML templates
├── static/               # Static files
├── manage.py             # Django CLI utility
├── requirements.txt      # Dependencies
└── README.md             # Project README
```

---

## ⚙️ Environment Variables

Optional `.env` file:

| Variable       | Description                            |
| -------------- | -------------------------------------- |
| `SECRET_KEY`   | Django secret key                      |
| `DEBUG`        | `True` or `False`                      |
| `DATABASE_URL` | Optional DB override (e.g. PostgreSQL) |

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

```bash
# Fork & clone the repo
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
```

Then open a pull request.


## 👤 Author

**[@iamshammas](https://github.com/iamshammas)**

---

## 🌐 Live Demo

👉 [https://blog-app-ik5e.onrender.com/](https://blog-app-ik5e.onrender.com/)

```

---

You're all set! Let me know if you'd like badges, screenshots, or deployment instructions (like Render/Heroku configs) added as well.
```
