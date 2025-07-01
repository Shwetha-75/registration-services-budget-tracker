from models.UserModel import User
import requests
class UserManipulation:
      
        def __init__(self):
            self.user_model={}
            
        def insert(self,userData):
            user_data=User(
                    userData['first_name'],
                    userData['last_name'],
                    userData['phone'],
                    userData['gender'],
                    userData['password'],
                    userData['confirm_password'],
                    userData['mail'])
            self.user_model=user_data.__str__()
           
            return requests.post("http://localhost:7006/insert",json=user_data.__str__()).json()
        
            
            