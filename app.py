
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
students = []

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Student Management System</title>
<style>
body { font-family: Arial; background: #eef3f9; padding: 30px; }
main { max-width: 750px; margin: auto; background: white;
       padding: 25px; border-radius: 12px; }
input { padding: 10px; margin: 5px; }
button { padding: 10px 16px; background: #1764c0;
         color: white; border: 0; cursor: pointer; }
table { width: 100%; margin-top: 25px; border-collapse: collapse; }
td, th { padding: 12px; border-bottom: 1px solid #ddd; text-align: left; }
</style>
</head>
<body><main>
<h1>Student Management System</h1>
<h3>Register a Student</h3>
<form action="/add" method="post">
<input name="name" placeholder="Student Name" required>
<input name="roll" placeholder="Roll Number" required>
<input name="department" placeholder="Department" required>
<button type="submit">Add Student</button>
</form>
<h3>Registered Students</h3>
<table>
<tr><th>Name</th><th>Roll Number</th><th>Department</th></tr>
{% for s in students %}
<tr><td>{{ s.name }}</td><td>{{ s.roll }}</td>
<td>{{ s.department }}</td></tr>
{% endfor %}
</table>
</main></body></html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE, students=students)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"].strip()
    roll = request.form["roll"].strip()
    department = request.form["department"].strip()

    if not any(s["roll"].lower() == roll.lower() for s in students):
        students.append({
            "name": name,
            "roll": roll,
            "department": department
        })
    return redirect("/")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
