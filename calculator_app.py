# calculator_app.py
from flask import Flask, render_template, request

app = Flask("__name__")

@app.route('/')
def main():
    return '<h1>Hello World</h1>'