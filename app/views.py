from app import app

from flask import Flask, flash, url_for, redirect, render_template, request, session
import json
from app.db_view import Registration




app.secret_key = "143"
reg = Registration()


@app.route("/")
def home():
    records = reg.display_records()
    # records = json.loads(records_json)
    # records_list = [list(record) for record in records]
    print(records)
    return render_template("index.html", records=records)




# # Route for the insert page
@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        user_pass = request.form.get("user_pass")
        # Insert a new record into the database
        reg.insert_record(user_name, email, user_pass)
        flash("record inserted")
    # Render the insert.html template
    return render_template("insert.html")


@app.route("/update", methods=["POST"])
def update():
    try:
        if request.method == "POST":
            user_id = request.form.get('user_id')
            user_name = request.form.get('user_name')
            email = request.form.get('email')
            user_pass = request.form.get('user_pass')
            reg.update_record(user_id, user_name, email, user_pass)
            flash("Record updated successfully")
        else:
            flash("Failed to update record")
        return redirect(url_for("home"))
    except Exception as e:
        print(f"Error in update route function: {e}")


@app.route("/delete", methods=["POST", "GET"])
def delete():
    if request.method == "POST":
        try:
            user_id = request.form.get("user_id")
            reg.delete_record(user_id)
            flash("record deleted successfully")
            return redirect(url_for("home"))
        except Exception as e:
            print(f"Error in delete route function: {e}")

if __name__ == "__main__":
    app.run(debug=True)
