from models.UserModel import User

class UserManipulation:
        def __init__(self,cursor):
            self.cursor=cursor
        def insert(self,userData):
            user_data=User(
                    userData['first_name'],
                    userData['last_name'],
                    userData['phone'],
                    userData['gender'],
                    userData['password'],
                    userData['confirm_password'],
                    userData['mail']
            )
            self.cursor.collection('user_model_table').document(userData['mail']).set(user_data.__str__()) 
        def update(self,userUpdateData,email:str):
            
            self.cursor.collection('user_model_table').document(email).update(userUpdateData)
            
            