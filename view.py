from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route("/",methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route("/generate",methods=["POST","GET"])
def generate():
    pass
    


if __name__ == "__main__":
    app.run(debug=True, port=5000)