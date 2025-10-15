from flask import Flask, render_template
from main import CollectGender
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("name_init.html")

@app.route('/<name>')
def collect_name(name):
    gender = CollectGender()
    age = CollectGender()
    data_gender = gender.collect_gender(name=name)
    gender = data_gender['gender']
    data_age = age.collect_age(name=name)
    years_old = data_age['age']
    return render_template('index.html', name=name, gender=gender, years_old=years_old)


@app.route('/post/blog/<num>')
def blog_posts(num):
    response = requests.get(url="https://api.npoint.io/51e4bf5f576774206625")
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)