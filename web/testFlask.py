# for the full tutorial visit this site
# http://flask.pocoo.org/docs/quickstart
from flask import Flask, url_for, request, jsonify
from imageSearch import getImageForTerm
from Errors import Errors
app = Flask(__name__)

# this is a Global Object For Logging Errors
error = Errors("static\\")


@app.route('/')
def index():
    return 'Index Page'

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

@app.route('/GetImage', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # request.args.get('key', '')
        # return request.form["hello"]
        data = request.get_json(force=True) 
        return getImageForTerm(data['query'])
    else:
        # show_the_login_form()
        return "you sent a get"


if __name__ == '__main__':
    app.run(debug=True)