from flask import Flask

app = Flask("Server")



@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Aaron Erebholo"

app.run(debug=True)