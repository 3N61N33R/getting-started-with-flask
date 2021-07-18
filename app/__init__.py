# file to initialize a python module

from flask import Flask

# initialize the app
# set instance_relative_config to true to enable loading of the
# config file with app.config.from_object('config')

app = Flask(__name__, instance_relative_config=True)
