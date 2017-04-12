# import sys
# sys.path.append("/Users/shiyangli/anaconda/lib/python2.7/site-packages/")
from flask import Flask, render_template
app = Flask(__name__)
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    return 'Post %d' % post_id


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
	return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)
