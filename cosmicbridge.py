
from flask import Flask, render_template, request
import requests

def send_simple_message(email,name):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox89f291fedc7243d38414d6871efcab53.mailgun.org/messages",
		auth=("api", "675d7587416512d36fb5bc88ac45cb27-acb0b40c-81fd1365"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox89f291fedc7243d38414d6871efcab53.mailgun.org>",
			"to": email,
			"subject": name,
			"text": "Congratulations, you just sent an email with Mailgun!  You are truly awesome!"})


app = Flask("comicsbridge")

@app.route("/")
def say_hello():
    return render_template("index.html")

@app.route("/about")
def about_page():
	return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/confirmation", methods=["POST"])
def send_email():
    data = request.values
    send_simple_message(data['email'],data['name'])
    return render_template("confirmation.html",form_data=data)

app.run(debug=True)
