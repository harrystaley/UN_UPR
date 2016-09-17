"""
Creates the UPR package and imports and initializes all required objects.
"""
# import top-level flask bits.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create the app.
app = Flask("upr")
# load the app's config.
app.config.from_object('upr.config')
# initialize the sqlalchemy object.
db = SQLAlchemy(app)

# import controlers to establish routes.
import controlers
# import models to create them:
import models
# import controlers to establish routes.
import controlers
