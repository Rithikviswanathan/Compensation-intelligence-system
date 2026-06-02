
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employees = [
    {"name": "Arun", "department": "IT", "salary": 50000, "bonus": 5000},
    {"name": "Meena", "department": "HR", "salary": 45000, "bonus": 4000},
]

@app.route("/")
def index():
    total_salary = sum(emp["salary"] for emp in employees)
    total_bonus = sum(emp["bonus"] for emp in employees)
    return render_template(
        "index.html",
        employees=employees,
        total_salary=total_salary,
        total_bonus=total_bonus
    )

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    department = request.form["department"]
    salary = int(request.form["salary"])
    bonus = int(request.form["bonus"])

    employees.append({
        "name": name,
        "department": department,
        "salary": salary,
        "bonus": bonus
    })

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
