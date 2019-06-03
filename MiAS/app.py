from flask import Flask
import models
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
