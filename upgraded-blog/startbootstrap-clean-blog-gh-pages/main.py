from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/a9f4797a6cc6d030fdc9")
response.raise_for_status()
blog_posts_data = response.json()
post_bg_images = ["static/assets/img/post-1-bg.jpg", "static/assets/img/post-2-bg.jpg",
                  "static/assets/img/post-3-bg.jpg"]
post_dates = ["August 24, 2023", "September 4, 2023", "September 11, 2023"]


@app.route("/")
def home():
    return render_template("index.html", all_posts=blog_posts_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def posts(index):
    posts_count = len(post_bg_images)
    requested_post = None
    for a_post in blog_posts_data:
        if a_post["id"] == index:
            requested_post = a_post
    ind = requested_post['id']
    return render_template("post.html", index=ind,
                           posts_count=posts_count, all_blog_posts=requested_post,
                           all_post_images=post_bg_images, all_post_dates=post_dates)


if __name__ == "__main__":
    app.run(debug=True)
