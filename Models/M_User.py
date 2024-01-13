from .M_Base import M_Base
class User(M_Base):
    """
     مدل یوزر در سیستم
    """
    def __init__(self,
                userName:str,
                password:str,
                webToken:str ,
                Identifier : int = 0):
        super().__init__(Identifier)
        # نام کاربری
        self.UserName = userName
        # رمز عبور
        self.Password = password
        # نشانه ی ورود JWT token
        self.WebToken = webToken
