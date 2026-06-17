from flask import *
import webbrowser,threading

app=Flask(__name__)
app.secret_key="abc"

@app.route("/contador",methods=["GET","POST"])
def contador():
 if request.method=="POST":
  session.pop("contador",None)
  return redirect("/contador")
 session["contador"]=session.get("contador",0)+1
 return render_template("contador.html",contador=session["contador"])

if __name__=="__main__":
 threading.Timer(1,lambda:
webbrowser.open("http://127.0.0.1:5000/contador")).start()
 app.run() 
 