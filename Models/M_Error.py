from .M_Base import M_Base
class Error(M_Base):
    """
    دیتا مدل گزارش خطا در سیستم
    """
    def __init__(self,fullReport : "in __str__ function of the ExceptionFactory.SystemError",Identifier:int=0):
        super().__init__(Identifier)
        self.FullReport = fullReport
    