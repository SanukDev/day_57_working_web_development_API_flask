from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/51e4bf5f576774206625")
    data =  response.json()
    return render_template("index.html", data=data)

@app.route('/blog/<id>')
def get_post(id):
    b = Post(int(id))
    t = Post(int(id))
    title = t.collect_title()
    body = b.collect_body()
    return render_template("post.html", body=body, title=title)


if __name__ == "__main__":
    app.run(debug=True)
