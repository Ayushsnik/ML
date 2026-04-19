from flask import *
from pickle import load

f = open("addict.pkl", "rb")
model = load(f)
f.close()

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        daily = float(request.form["daily_usage"])
        sleep = float(request.form["sleep"])
        academic = float(request.form["academic"])
        checks = float(request.form["checks"])
        weekend = float(request.form["weekend"])

        result = model.predict([[daily, sleep, academic, checks, weekend]])
        return render_template("index.html", result=result)
    else: 
        return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader= True)

