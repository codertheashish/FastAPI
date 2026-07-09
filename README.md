# 🎓 FastAPI Student CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built using **FastAPI** and **Pydantic**. This project demonstrates how to create API endpoints for managing student records without using a database.

---

## 🚀 Features

- ➕ Create Student
- 📄 View All Students
- 🔍 View Student by ID
- ✏️ Update Student Details
- ❌ Delete Student
- ⚡ Built with FastAPI
- ✅ Request Validation using Pydantic

---

## 🛠️ Technologies Used

- Python 3
- FastAPI
- Pydantic
- Uvicorn

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Installation

### Clone the repository

```bash
https://github.com/codertheashish/FastAPI-CRUD
```

### Move into the project

```bash
cd your-repository
```

### Create Virtual Environment (Optional)

```bash
python -m venv myenv
```

### Activate Virtual Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux/Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

FastAPI automatically generates API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Create Student

**POST**

```
/create
```

Example JSON

```json
{
  "id": 101,
  "name": "Ashish Kumar Prajapati",
  "email": "codertheashish@gmail.com"
}
```

---

### View All Students

**GET**

```
/view
```

---

### View Student by ID

**GET**

```
/views/{id}
```

Example

```
/views/101
```

---

### Update Student

**PUT**

```
/update/{id}
```

Example JSON

```json
{
  "id": 101,
  "name": "Ashish Kumar",
  "email": "codertheashish@gmail.com"
}
```

---

### Delete Student

**DELETE**

```
/delete/{id}
```

Example

```
/delete/101
```

---

## 📷 Example Workflow

1. Create a student
2. View all students
3. Search a student by ID
4. Update student information
5. Delete the student

---

## ⚠️ Note

This project stores data in a Python list, so all data will be lost when the server is restarted. It is intended for learning FastAPI CRUD operations.

---

## 📚 Future Improvements

- Connect with MySQL
- Connect with MongoDB
- Add SQLAlchemy ORM
- JWT Authentication
- User Login & Registration
- Data Validation
- Error Handling
- Docker Support

---

## 👨‍💻 Author

**Ashish Kumar Prajapati**

GitHub:<br>
https://github.com/codertheashish <br>
Linkedin : <br>
https://linkedin.com/in/codertheashish
