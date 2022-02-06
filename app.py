from flask import Flask, request, render_template, send_from_directory
from functions import get_post_by_tag, get_all_tags_from_posts


UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():

    all_tags = get_all_tags_from_posts()
    return render_template("index.html", all_tags=all_tags)


@app.route("/tag")
def page_tag():
    tag_name = request.args.get("tag")
    posts = get_post_by_tag(tag_name)
    return render_template("post_by_tag.html", tag_name=tag_name,  posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

