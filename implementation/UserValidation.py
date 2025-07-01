import requests
class UserValidation:
        def __init__(self):
               
                self.currentUser=None 
                self.doc=None 
        def userValidate(self,mail:str): 
               result=requests.get(f"http://localhost:7006/fetch/{mail}").json()        
               return result
        
        def validateUser(self,mail:str)->bool:
                self.doc=self.userValidate(mail)
                return True if self.doc['status']=='ok' else False 
                