from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<html><body><h1>Simple Instrumented Calculator</h1><p><a href='/calc'>Start calculator</a></p></body></html>" 
    
@app.route("/calc", methods=["POST","GET"])
def calculator_page():
    number = 0
    to_add = 0
    new_value = 0
    if request.method == "POST":
        number = int(request.form['start_value'])
        to_add = int(request.form['add_value'])
        new_value = number + to_add
    return f"<html><body><h1>Simple Instrumented Calculator</h1><form action='/calc' method='post'><input type='text' name='start_value' value='{new_value}' readonly /><br/><h4>+</h4><br/><input type='text' name='add_value'/><br/><input type='submit' value='Add Number'/></form></body></html>"
