class M_Base:
    def __init__(self,Identifier):
        self.Id = Identifier
    def GetFields(self):
        """
        دریافت فیلد های مدل در قالب دیکشنری برای ثبت در دیتابیس جیسون فایل
        """
        result = {}
        for attr in self.__dict__:
            if(not attr.startswith('__') and str(attr) != "Id"):
                result[attr]=getattr(self,attr)
        return result
    