from flask import * 

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/factorial")
def factorial():
    n= int(request.args.get("n"))
    f= 1
    for i in range(1,n+1):
        f= f*i
        return jsonify(
            {
                "ans":f
            }
        )
    

if __name__ == "__main__":
        app.run(debug=True,use_reloader=True )
