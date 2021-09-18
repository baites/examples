from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
        <p style="font-size:300%;color:green;"><b><i>Hello, Julieta</i></b></p>
        <img src="https://www.cdc.gov/healthypets/images/pets/cute-dog-headshot.jpg"/>"""