import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_coffee")
def get_coffee():
    coffee = list(mongo.db.coffee.find())
    return render_template("coffee.html", coffee=coffee)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    coffee = list(mongo.db.coffee.find({"$text": {"$search": query}}))
    return render_template("coffee.html", coffee=coffee)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_coffee", methods=["GET", "POST"])
def add_coffee():
    if request.method == "POST":
        coffee = {
            "species_type": request.form.get("species_type"),
            "coffee_name": request.form.get("coffee_name"),
            "coffee_strength": request.form.get("coffee_strength"),
            "coffee_quality": request.form.get("coffee_quality"),
            "coffee_description": request.form.get("coffee_description"),
            "created_by": session["user"]
        }
        mongo.db.coffee.insert_one(coffee)
        flash("Coffee Successfully Added")
        return redirect(url_for("get_coffee"))

    species = mongo.db.species.find().sort("species_type", 1)
    return render_template("add_coffee.html", species=species)


@app.route("/edit_coffee/<coffee_id>", methods=["GET", "POST"])
def edit_coffee(coffee_id):
    if request.method == "POST":
        submit = {
            "species_type": request.form.get("species_type"),
            "coffee_name": request.form.get("coffee_name"),
            "coffee_strength": request.form.get("coffee_strength"),
            "coffee_quality": request.form.get("coffee_quality"),
            "coffee_description": request.form.get("coffee_description"),
            "created_by": session["user"]
        }
        mongo.db.coffee.replace_one({"_id": ObjectId(coffee_id)}, submit)
        flash("Coffee Successfully Updated")

    coffee = mongo.db.coffee.find_one({"_id": ObjectId(coffee_id)})
    species = mongo.db.species.find().sort("species_type", 1)
    return render_template("edit_coffee.html", coffee=coffee, species=species)


@app.route("/delete_coffee/<coffee_id>")
def delete_coffee(coffee_id):
    mongo.db.coffee.delete_one({"_id": ObjectId(coffee_id)})
    flash("Coffee Successfully Deleted")
    return redirect(url_for("get_coffee"))


@app.route("/get_species")
def get_species():
    species = list(mongo.db.species.find().sort("species_type", 1))
    return render_template("species.html", species=species)

@app.route("/add_species", methods=["GET", "POST"])
def add_species():
    if request.method == "POST":
        species = {
            "species_type": request.form.get("species_type")
        }
        mongo.db.species.insert_one(species)
        flash("New Species Added")
        return redirect(url_for("get_species"))

    return render_template("add_species.html")


@app.route("/edit_species/<species_id>", methods=["GET", "POST"])
def edit_species(species_id):
    if request.method == "POST":
        submit = {
            "species_type": request.form.get("species_type")
        }
        mongo.db.species.replace_one({"_id": ObjectId(species_id)}, submit)
        flash("Species Successfully Updated")
        return redirect(url_for("get_species"))

    species = mongo.db.species.find_one({"_id": ObjectId(species_id)})
    return render_template("edit_species.html", species=species)

@app.route("/delete_species/<species_id>")
def delete_species(species_id):
    mongo.db.species.delete_one({"_id": ObjectId(species_id)})
    flash("Species Successfully Deleted")
    return redirect(url_for("get_species"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)