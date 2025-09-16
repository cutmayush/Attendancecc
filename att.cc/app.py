from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    # get lists of values from the form
    attended_list = request.form.getlist("attended")
    total_list    = request.form.getlist("total")

    # convert to ints and sum safely (ignore empty or non-numeric)
    total_attended = 0
    total_classes = 0
    for a, t in zip(attended_list, total_list):
        try:
            ai = int(a)
            ti = int(t)
        except (ValueError, TypeError):
            continue
        total_attended += ai
        total_classes += ti

    percentage = 0.0
    if total_classes > 0:
        percentage = (total_attended / total_classes) * 100

    return render_template("result.html",
                           attended=total_attended,
                           classes=total_classes,
                           percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True)
