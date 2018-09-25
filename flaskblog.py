from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Jyotirmoy Mandal',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': 'September 25, 2018'
    },
    {
        'author': 'Randy Orton',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': 'September 20, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
