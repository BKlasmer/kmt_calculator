#!flask/bin/python
from flask import Flask, request
from kmt_calculator import CalculatorInfix, CalculatorPrefix

app = Flask(__name__)


@app.route("/calculator")
def welcome_message():
    return "Welcome to the KMT Calculator Flask Application"


@app.route("/calculator/infix", methods=["POST"])
def calculate_infix():
    CalcInfix = CalculatorInfix()
    return f"{request.json['expression']} evaluates to: {CalcInfix.parse_infix_expression(request.json['expression'])} \n"


@app.route("/calculator/prefix", methods=["POST"])
def calculate_prefix():
    CalcPrefix = CalculatorPrefix()
    return f"{request.json['expression']} evaluates to: {CalcPrefix.parse_prefix_expression(request.json['expression'])} \n"


if __name__ == "__main__":
    app.run(debug=True)
