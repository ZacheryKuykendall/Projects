from flask import render_template
import utilities

def home():
    message = utilities.get_message()
    return render_template('index.html', message=message)
