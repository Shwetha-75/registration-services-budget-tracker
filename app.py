from flask import Flask,request
from dotenv import load_dotenv 
from flask_cors import CORS
import os 
load_dotenv()

app=Flask(__name__)

@app.route("/")
def index():
    if request.method=='POST':
        user_data=dict(request.form) if request.form else request.get_json()
        
    pass



if __name__=='__main__':
    app.run(port=os.getenv('PORT'),debug=True)
