from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [ {'author': 'paarijat thakur',
        'title': 'blog1',
        'date_posted':'22-12-22',
        'content':'blog post1'},
        {
        'author': 'shiva',
        'title': 'blog2',
        'date_posted':'22-12-23',
        'content':'blog post1'

        }
        ]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About us")




if __name__=='__main__':
    app.run(debug=True)
