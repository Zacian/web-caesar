from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/" method="POST">
                <label for="rot"><b>Rotate by:</b></label>
                <input type="text" name="rot" value="0"/>
                <textarea name="text">{0}</textarea>
                <input type="submit" value="Submit Query"/>
            </form>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form["rot"])
    string = request.form["text"]
    #encrypt = '<h1>'
    encrypt = rotate_string(string, rot)
    #encrypt += '</h1>'

    return form.format(encrypt)

app.run()