from flask import Flask, render_template, request
from db import get_post, get_posts, update_post

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/posts")
def posts():
    posts = get_posts()
    return render_template("posts/index.html", posts=posts)


@app.route("/posts/edit/<int:post_id>", methods=["GET", "PUT"])
def edit_post(post_id: int):
    if request.method == "PUT":
        title = str(request.form.get("Title"))
        content = str(request.form.get("Content"))
        update_post(post_id, title, content)
        return show_post(post_id)

    post = get_post(post_id)
    return render_template("/posts/_partials/edit.html", post=post)


@app.route("/posts/<int:post_id>")
def show_post(post_id: int):
    post = get_post(post_id)
    return render_template("/posts/_partials/show.html", post=post)
