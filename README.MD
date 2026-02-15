
## 📌 Project Overview

This project is a Simple REST API built using Flask (Python) to manage users.

The API supports:
- GET /users → Retrieve all users
- POST /users → Add a new user

Data is stored in memory (no database used).

All API responses follow a consistent JSON structure:

{
  "status": "success" | "error",
  "data": ...
}

---

## 🛠 Technologies Used

- Python 3.x
- Flask
- Postman (Manual Testing)
- VS Code

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
2️⃣ Run the application
python app.py
Server will start at:

http://127.0.0.1:5000
📌 API Endpoints
🔹 GET /users
Returns list of all users.

Response Example:

{
"status": "success",
"data": [
{
"id": 1,
"name": "Alice",
"email": "alice@example.com"
}
]
}

Status Code:

200 OK

🔹 POST /users
Adds a new user.

Request Body (JSON):

{
"name": "Alice",
"email": "alice@example.com"
}

Validations:

name is required

email is required

email must contain "@"

duplicate emails are not allowed

Success Response:

201 Created

Error Response:

400 Bad Request

🧪 Manual Testing & Bug Fix
Manual testing was performed using Postman.

✅ Phase 1: Normal API Testing (No Bug)
Tested:

GET /users → returned 200 with correct JSON structure

POST /users → returned 201 and stored user correctly

Screenshots included in repository:

Working GET request

Working POST request

All responses were consistent and validated properly.

🐞 Phase 2: Introduced Bug (Duplicate Email Allowed)
Bug Description
The duplicate email validation was intentionally removed from the code.

Steps to Reproduce
Remove duplicate email validation logic.

Send POST request with:
{
"name": "Alice",
"email": "alice@example.com"
}

Send another POST request with the same email.

Observed Behavior
Both requests returned:

201 Created

This allowed duplicate emails in the system.

Problem
Allowing duplicate emails:

Breaks data integrity

Can cause identity conflicts

Creates potential security issues

Screenshots included:

Two successful POST requests with same email


🔧 Bug Fix
Duplicate email validation logic was reintroduced:

Before adding a new user, the system checks if the email already exists.

After Fix
Second POST request now returns:

{
"status": "error",
"data": "Email already exists"
}

Status Code:

400 Bad Request

This ensures data integrity and prevents duplicates.

🧠 Schema Validator (Aptitude Task)
A separate file schema_validator.py contains a function:

validate_response(obj)
It checks:

id must be int

name must be string

email must be string and contain "@"

Three test cases included:

1 valid response

2 invalid responses

📊 What I Learned
Building REST APIs using Flask

Handling HTTP status codes properly

Designing consistent JSON responses

Performing manual API testing using Postman

Identifying and fixing logical bugs

Importance of data validation and integrity