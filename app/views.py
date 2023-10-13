from app import app

from flask import Flask, flash, url_for, redirect, render_template, request, session
import json
from app.db_view import students




app.secret_key = "143"
reg = students()


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
    try:
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            address = request.form.get("address")
            std_class = request.form.get("std_class")
            # Insert a new record into the database
            reg.insert_record(name, email, address, std_class)
            flash("record inserted")
        
        return redirect(url_for("home"))
    except Exception as e:
        print(f"Error in Insert route function: {e}")


@app.route("/update", methods=["POST"])
def update():
    try:
        if request.method == "POST":
            id = request.form.get('id')
            name = request.form.get('name')
            email = request.form.get('email')
            address = request.form.get('address')
            std_class = request.form.get('std_class')
            reg.update_record(id, name, email, address, std_class)
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
            id = request.form.get("id")
            reg.delete_record(id)
            flash("record deleted successfully")
            return redirect(url_for("home"))
        except Exception as e:
            print(f"Error in delete route function: {e}")

# if __name__ == "__main__":
#     app.run(debug=True)
