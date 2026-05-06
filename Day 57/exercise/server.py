from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


def get_age(name):
    agify_response = requests.get("https://api.agify.io", params={'name': name})
    data = agify_response.json()
    return data.get("age")


def get_gender(name):
    genderize_response = requests.get("https://api.genderize.io", params={'name': name})
    data = genderize_response.json()
    return data.get("gender")


@app.route('/')
def index():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route("/guess/<name>/")
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template('guess.html', name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c9c79e3a32a8e6194432"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)


