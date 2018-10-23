##### server file ######
# import ipdb; ipdb.set_trace()

#################
#### imports ####
#################
import os
from flask import Flask, render_template, redirect, request, flash, session, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug import secure_filename
import datetime

app = Flask(__name__)


################
#### routes ####
################


@app.route('/')
def homepage():
    """Show homepage."""
  
    return render_template('homepage.html')



if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
