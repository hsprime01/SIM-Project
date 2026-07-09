from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    incident = request.form["incident"]
    location = request.form["location"]

    return render_template(
        "success.html",
        name=name,
        incident=incident,
        location=location
    )

if __name__ == "__main__":
    app.run(debug=True)
