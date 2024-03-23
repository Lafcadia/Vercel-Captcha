from captcha.image import ImageCaptcha
from flask import Flask, render_template, request
import string
import random
import base64

html = """<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
    <h1>This is a captcha generator.</h1>
    <img src="data:;base64,{{ img_stream }}">
    <form action="/", method="POST">
        <p>Code: <input type="text", name="yanzheng"></input></p>
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""

app = Flask(__name__)

def generator(name="code.png"):
    token = string.digits + string.ascii_letters
    cap = random.sample(token,8)
    token_str = ''.join(cap)
    img = ImageCaptcha(width=400,height=150)
    image = img.generate_image(token_str)
    image.save(name)
    return token_str

@app.route('/', methods=['GET','POST'])
def index():
    global real_str
    if request.method == 'POST':
        result = request.form
        r = result.get('yanzheng').lower() == real_str.lower()
        if r:
            return "1"
        else:
            return "0"
    else:
        return render_template(html, img_stream=streamer())

@app.route('/code.png')
def view():
    return streamer()

def streamer():
    global real_str
    token = string.digits + string.ascii_letters
    cap = random.sample(token,8)
    token_str = ''.join(cap)
    img = ImageCaptcha(width=400,height=150)
    image = img.generate_image(token_str)
    real_str = token_str
    return base64.b64encode(image).decode()

# if __name__ == '__main__':
#     app.run(host='127.0.0.1',port='2333')