from flask import Flask
from flask import request
from flask import render_template


design_app = Flask (__name__)

@design_app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    design_app.run(host="0.0.0.0",port=5050)