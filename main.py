from flask import Flask, render_template, redirect, url_for, flash, g, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, SubmitField, \
    PasswordField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm
from projects import projects_list
import os
import smtplib


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


app = Flask(__name__)

os.environ["SECRET_KEY"] = "22@2003@22"

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Thank you for your message. I will get back to you soon!")
        name = form.name.data
        email = form.email.data
        message = form.message.data

        send_messages(name=name, email=email, message=message)

        return redirect(f"{url_for('home')}#contact")

    return render_template("index.html", form=form)


@app.route("/projects")
def project_showcase():
    return render_template("projects.html", projects=projects_list)


def send_messages(name, message, email):
    sender = os.environ.get("EMAIL_USER")
    receiver = "truongthoithang@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")
    msg_subject = "Alert!!! Someone is trying to contact from your portfolio!!!"
    msg_body = f"The person with the name of {name} with the email of {email} has a message for you \n  {message}"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)

        msg = f"Subject : {msg_subject}\n\n {msg_body}"

        try:
            smtp.sendmail(sender, receiver, msg)
            print("Successfully Sent")
        except:
            print("Error")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
