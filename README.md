# Bank API Server

A RESTful API built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL** that provides bank and branch information.

---

## 🚀 Features
- List all banks
- Get branch details using IFSC code
- PostgreSQL database support
- CSV data import script
- Modular project structure
- Unit tests included

---

## 🛠 Tech Stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

---

## 📂 Project Structure

bank-api-server/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routers/
│ ├── bank.py
│ └── branch.py
│
├── data/
│ ├── bank_branches.csv
│ └── import_data.py
│
├── tests/
│ └── test_api.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️. Clone the repository
```bash
git clone https://github.com/prasadmanish8081/bank-api-server.git
cd bank-api-server

### 2️. Create virtual environment

python -m venv venv
venv\Scripts\activate   


### 3. Install dependencies

pip install -r requirements.txt

### 4. Setup Database

CREATE DATABASE bank_api_server;

### 5. Import CSV data

python data/import_data.py

### 6. Run the server

uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000

🔗 API Endpoints

Get all banks
GET /banks/

Get branch by IFSC
GET /branches/{ifsc}

🧪 Run Tests
pytest

👤 Author

Manish Prasad

📄 License

This project is for assignment and learning purposes.


---

### Commit README
```bash
git add README.md
git commit -m "Update README with project details"
git push
