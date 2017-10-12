#!/usr/bin/python3

from flask_wtf import Form
from wtforms import StringField, TextField

class PostForm(Form):
    post = TextField()

class NameForm(Form):
    name = TextField()
