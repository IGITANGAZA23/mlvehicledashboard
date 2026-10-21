# Machine Learning: Advanced Vehicle Management Dashboard

An interactive and styled Django web dashboard that processes vehicle machine learning dummy data using Pandas and renders grouped analytics, frequency tables, and visualizations formatted with Bootstrap 5.

---

## 🚀 Features

- **Automated Frequency Analysis:** Calculates one-way frequency distribution tables for vehicle manufacturers using Pandas.
- **Bootstrap 5 UI & Styling:** Responsive dashboard layout featuring side navigation with Scrollspy, cards, and striped responsive tables.
- **Django Modular Architecture:** Clean separation of concerns with dedicated `vehicles` application, dashboard analytics module, views, and templates.
- **Test Suite:** Built-in Django `TestCase` testing frequency table generation and HTTP response rendering.

---

## 🛠️ Tech Stack

- **Python 3.14+**
- **Django 6.1+**
- **Pandas 3.0+**
- **Plotly 7.1+**
- **Bootstrap 5.3.2**

---

## 📂 Project Structure

```text
mlvehicledashboard/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # INSTALLED_APPS, ALLOWED_HOSTS, and project configuration
│   ├── urls.py              # Main URL routing including vehicle routes
│   └── wsgi.py
├── dummy_data/
│   └── vehicles_data_1000.csv  # 1,000-record vehicle dummy dataset
├── vehicles/
│   ├── migrations/
│   ├── templates/
│   │   └── vehicles/
│   │       └── index.html   # Bootstrap 5 styled dashboard template
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── dashboard.py         # Data analytics functions (e.g. frequency_table)
│   ├── models.py
│   ├── tests.py             # Unit and integration test suite
│   ├── urls.py              # App-level routing
│   └── views.py             # View controllers serving the dashboard
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/IGITANGAZA23/mlvehicledashboard.git
cd mlvehicledashboard
```

### 2. Create and Activate Virtual Environment

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🧪 Running Tests

Execute Django's automated test runner:
```bash
python manage.py test
```

---

## 📝 License
This project is developed for educational purposes under the Machine Learning practicals curriculum.
