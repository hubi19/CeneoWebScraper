from app import app
from flask import Flask, render_template

@app.route("/name", defaults={'name': "Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}!"

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/author")
def author():
    return render_template('author.html')

@app.route("/extraction")
def extraction():
    return render_template('extraction.html')

@app.route("/product_list")
def product_list():
    return render_template('product_list.html')
