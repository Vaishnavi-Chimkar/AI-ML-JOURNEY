#end point 

from flask import Flask,render_template,url_for,request,jsonify,flash,redirect

# app = Flask(__name__,static_folder="assets",static_url_path="/assets")
app = Flask(__name__)

app.secret_key = "some secret message or key"


@app.route("/")
def hello_world():
    return redirect(url_for("login"))
    #static file => dynamically generate the url
    # print(url_for("static",filename="style2.css"))

    # name  = request.args.get("name", default="anonymous")
    # subject = request.args.get("subject")

    # return render_template("index.html",name=name,sub=subject)

    # data = {
    #     "message":" Welcome to the platform!"
    # }

    # return jsonify(data)

# @app.route("/prime")
# def prime():
#     return "<p>Hello, from Prime :)</p>"

# @app.route("/login",methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         name = request.form["username"]
#         password = request.form["password"]

#         # return f"<p> Welcome {name} !</p>"
#         return render_template("welcome.html",name = name,password=password)
#     else:
#         return render_template("login.html")

@app.route("/contact")
def contact():
    flash("support timings are from 9-5")
    return render_template("contact.html")

@app.route("/login")
def login():
    return "<p>Login Successful</p>"

if __name__ == "__main__":
    app.run(debug=True)