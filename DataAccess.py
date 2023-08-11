import os
import json
from Models.ExceptionFactory import DatabaseError
from Models.M_Base import M_Base


class JSONDatabase:
    def __init__(self,FileName):
        self.data = {}
        self.file_path = os.path.join('./Datas', f"{FileName}.json")
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    self.data = json.load(file)
                except:
                    self.data = {}
        else:
            raise DatabaseError(f'دیتابیس {FileName} وجود ندارد')

    def CommitData(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file)
    
    def Create(self, model:M_Base)->int:
        Id = len(self.data) + 1
        if(Id not in self.data):
            self.data[Id] = model
            self.CommitData()
        else:
            raise DatabaseError('رکورد با این شناسه قبلاً ایجاد شده است.')
    
    def Read(self,Id:int) -> M_Base:
        if(Id in self.data):
            return self.data[Id]
        else:
            raise DatabaseError('رکورد با این شناسه وجود ندارد.')
    
    def Update(self, Id : int, updated_model : M_Base):
        if(Id in self.data):
            self.data[Id] = updated_model
            self.CommitData()
        else:
            raise DatabaseError('رکورد با این شناسه وجود ندارد.')
    
    def Delete(self, Id:int):
        if(Id in self.data):
            del self.data[Id]
            self.CommitData()
        else:
            raise DatabaseError('رکورد با این شناسه وجود ندارد.')

DB_Logs = JSONDatabase('Errors')
    