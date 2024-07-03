from flask import Flask, render_template, request
import google.generativeai as palm 

palm.configure(api_key="AIzaSyCCT1K998J1blwhCE7qOcQ5KOZcPJ9ZZ4")

model = {"model" : "models/chat-bison-001"}

app = Flask(_name_)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET","POST"])
def main():
    r = request.form.get("q")
    print(r)
    return(render_template("main.html",r=r))

if __name__ == "__main__":
    app.run()
    @app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/traffic_thailand", methods=["GET","POST"])
def traffic_thailand():
    r = request.form.get("q")
    print(r)
    return(render_template("traffic_thailand.html",r=r))

if __name__ == "__main__":
    
    app.run()
