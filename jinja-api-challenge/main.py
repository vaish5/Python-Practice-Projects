from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/guess/<some_name>")
def guess(some_name):

    # Getting gender from genderize API

    genderize_response = requests.get(f"https://api.genderize.io?name={some_name}")
    genderize_response.raise_for_status()
    gender_data = genderize_response.json()
    gender = gender_data["gender"]

    # Getting age from agify API

    agify_response = requests.get(f"https://api.agify.io?name={some_name}")
    agify_response.raise_for_status()
    age_data = agify_response.json()
    age = age_data["age"]

    return render_template("index.html", name=some_name.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
