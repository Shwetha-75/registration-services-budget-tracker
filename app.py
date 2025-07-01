from flask import Flask,request,jsonify
from dotenv import load_dotenv 
from flask_cors import CORS
import os 
from implementation.UserValidation import UserValidation
from implementation.UserManipulation import UserManipulation


load_dotenv()


app=Flask(__name__)

userValidation=UserValidation()
userManipulation=UserManipulation()


@app.route("/",methods=['POST','GET'])
def index():
    if request.method=='POST':
        user_data=dict(request.form) if request.form else request.get_json()
        print(user_data)
        if userValidation.validateUser(user_data['mail']):
            return jsonify({"status":"no"})
        userManipulation.insert(user_data)
    return jsonify({"status":"ok"})



if __name__=='__main__':
    app.run(port=os.getenv('PORT'),debug=True)
