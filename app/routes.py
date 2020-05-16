from flask import render_template, url_for, flash, redirect, request
from app.models import User
from app.form import SubmitForm
from app import app, db
import secrets
import os

@app.route("/")
@app.route("/home")
def home():
    return "Hello"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = SubmitForm()
    if form.validate_on_submit():
        user = User(id=form.id.data, name=form.name.data, regno=form.regno.data, dpt=form.dpt.data, cgpa=form.cgpa.data)
        db.session.add(user)
        db.session.commit()
        flash("Data Added to Database", "success")
        return redirect(url_for('submit'))
    return render_template("submit.html", title="Add data to database", form=form)