from flask import Flask,render_template,request,redirect
from flask_pymongo import PyMongo
app = Flask(__name__)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/utkal_divas_feedback"
mongo = PyMongo(app)
mongodb=mongo.db.user

@app.get("/")
def show():
    return render_template("index.html")

@app.get('/styles.css')
def styles():
    return render_template('styles.css')
        
@app.post('/')
def feedback():
    name=request.form['feedback-name']
    email=request.form['feedback-email']
    contact=request.form['feedback-contact']
    feedback=request.form['feedback-message']

    existing_data=mongodb.find_one({'$or':[{'name':feedback-name},{'email':feedback-email}]})
    if existing_data:
        return render_template('index.html',message="user already give his feed-back")
    else:
        mongo.insert_one({'name':name,'email':email,'conact':contact,'feedback':feedback})
    return render_template("index.html",message="feedback is given")
if __name__==("__main__"):
    app.run(debug=True)