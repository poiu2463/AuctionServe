#!/usr/bin/env python

'''
This is the index.py page which should handle the routing and launching of the actual application.
We will split this up as needed into smaller subfiles to allow for better readability.
'''

import flask

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.debug = True
    APP.run()
