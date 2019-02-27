from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "hello.."
@app.route("/home")
def home():
    return "WELCOME TO MY HOME PAGE"
@app.route("/about")
def about():
    return "About Me"
@app.route("/contact")
def contact():
    return "CONTACT IS 9447996345"
if(__name__=="__main__"):
    app.run(debug=True)