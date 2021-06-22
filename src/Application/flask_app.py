from src.imageProcessing import Image
from flask import Flask, render_template, request, redirect, url_for

from src.imageProcessing.Main import Main

app = Flask(__name__)
output_img = Image.Image("outputImage")

def set_output_img(img: Image.Image):
    global output_img
    output_img = img
@app.route("/", methods=["POST", "GET"])
def home():
    global output_img
    return render_template('home.html', user_image=output_img)
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)