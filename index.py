#!/usr/bin/env python
import os

import flask

# Create the application.
# template_dir = os.path.abspath('src-backend/templates')
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.debug = True
    APP.run()
