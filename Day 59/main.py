from flask import Flask, render_template, url_for
import requests
import json

blog_api = "https://api.npoint.io/653c3f9f6814cd0f2e85"
data = requests.get(blog_api).json()






app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", data=data)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None

    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post

    print(requested_post)

    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)