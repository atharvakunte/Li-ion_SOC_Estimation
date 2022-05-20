
from flask import Flask, render_template , request
import model

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def predict():
    if request.method =="POST" :

         voltage=request.form['voltage']
         current=request.form['current']
         temp=request.form['temp']
         soc=model.predict(voltage,current,temp)
         perc_soc=soc[0][0]*100
         return render_template("frontend.html", predicted_output=perc_soc)

    else :
        return render_template("frontend.html")
    


if __name__=="__main__":
    app.run(debug=True)