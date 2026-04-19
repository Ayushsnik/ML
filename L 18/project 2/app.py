from flask import * 

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        s1 = request.form.get("name")
        msg = "welcome "+s1
        return render_template("home.html", msg = msg)
    else:
        return render_template("home.html")
    
if __name__ == "__main__":
    app.run(use_reloader=True, debug = True)
