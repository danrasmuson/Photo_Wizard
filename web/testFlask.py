# for the full tutorial visit this site
# http://flask.pocoo.org/docs/quickstart
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# /post/12 -- good
# /post/hello -- 404 error
@app.route('/post/<int:post_id>')
# can use
# int   accepts integers
# float   like int but for floating point values
# path    like the default but also accepts slashes
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/urlPrint')
def printUrl():
    # using the function names
    return url_for("hello")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do_the_login()
        return "you sent a post"
    else:
        # show_the_login_form()
        return "you sent a get"


if __name__ == '__main__':
    app.run(debug=True)