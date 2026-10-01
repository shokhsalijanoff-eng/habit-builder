from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route("/")
def home():
    with open("habits.json", "r") as file:
        habits = json.load(file)

    return render_template("index.html", habits=habits)


@app.route("/add", methods=["POST"])
def add_habit():
    habit_name = request.form["name"]

    with open("habits.json", "r") as file:
        habits = json.load(file)

    new_habit = {
        "name": habit_name,
        "completed": False
    }

    habits.append(new_habit)

    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)

    return redirect("/")

@app.route("/complete/<int:habit_id>", methods=["POST"])
def complete_habit(habit_id):
    with open("habits.json", "r") as file:
        habits = json.load(file)

    habits[habit_id]["completed"] = True

    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)

    return redirect("/")

@app.route("/delete/<int:habit_id>", methods=["POST"])
def delete_habit(habit_id):
    with open("habits.json", "r") as file:
        habits = json.load(file)

    habits.pop(habit_id)

    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)

    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)