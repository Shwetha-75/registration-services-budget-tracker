class UserValidation:
        def __init__(self,cursor):
                self.cursor=cursor
                self.currentUser=None 
                self.doc=None 
        def userValidate(self,mail:dict): 
               return self.cursor.collection('user_model_table').document(mail)
        
        def validateUser(self,dataModel:dict)->bool:
                self.doc=self.userValidate(dataModel['mail'])
                doc=self.doc.get()
                return True if not doc.exists else False 
                