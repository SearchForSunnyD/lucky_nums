from flask import Flask, render_template, jsonify, request
from forms import LuckyNumForm
from random import randint
import requests

app = Flask(__name__)


@app.route("/")
def homepage():
    """Render and display the homepage.

    Returns:
        str: HTML content for the homepage.
    """
    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def lucky_submit():
    """Process the lucky-form, validate the data, and return JSON response.

    Returns:
        dict: JSON response containing either the errors in the form or random facts.
    """
    r_form = request.form
    form = LuckyNumForm(meta={"csrf": False}, obj=r_form)

    if form.validate_on_submit():
        year = form.year.data
        response = generate_random_facts(year)
        return jsonify(response)

    response = {"errors": form.errors}
    return jsonify(response)


def generate_random_facts(year):
    """Generate a random number and fetch two facts from the Numbers API.

    Args:
        year (int): The year for which to fetch a fact.

    Returns:
        dict: A dictionary containing random facts for a number and a year.
    """
    num = randint(1, 100)
    rand_fact = requests.get(f"http://numbersapi.com/{num}")
    year_fact = requests.get(f"http://numbersapi.com/{year}/year")

    return {
        "num": {"fact": f"{rand_fact.text}", "num": f"Your lucky number is: {num}!"},
        "year": {"fact": f"{year_fact.text}", "year": f"Fun fact for {year}!"},
    }


