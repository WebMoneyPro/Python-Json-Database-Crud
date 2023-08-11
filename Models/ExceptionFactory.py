import traceback
from Models.M_Base import M_Base

class APIError(Exception):
    """
    خطاهای رخ داده در API
    """
    def __init__(self, message, error_code):
        # پیامی که به کلاینت ارسال می‌شود
        self.Message = message
        # کد خطای HTTP که به کلاینت ارسال می‌شود
        self.Error_Code = error_code


class SystemError(Exception):
    """
    دیتا مدل
    خطاهای رخ داده در سیستم
    """
    def __init__(self, message, lineNumber, fileName, functionName, lineCode):
        # پیام خطا
        self.Message = message
        # شماره خط
        self.LineNumber = lineNumber
        # نام فایل
        self.FileName = fileName
        # نام تابع
        self.FunctionName = functionName
        # کد سینتکس که در خط ارور داده
        self.LineCode = lineCode
    def __str__(self):
        """
        گزارش برای ثبت در پایگاه داده
        """
        return f'[Message] : {self.Message}\n [LineNumber] : {self.LineNumber}\n [FileName] : {self.FileName}\n [FunctionName] : {self.FileName}\n [SyntaxCode]{self.LineCode}'

def SystemErrorHandler(error: Exception) -> SystemError:
    """
    تابع برای تبدیل ارور های پایتون به مدل ارور های سیستم

    """
    frames = traceback.extract_tb(error.__traceback__)
    frame = frames[0]
    return SystemError(str(error), frame.lineno, frame.filename, frame.name, frame.line)

class X_Base(Exception):
    """
    Interface for exception factory
    """
    ...

class X_Database(X_Base):
    """
    DATABASE ERROR
    برای ساخت ارور های دیتابیس
    """
    ...



def APIErrorHandler(error_code: str, default_message: str = "مشکلی پیش آمده است.") -> APIError:
    return APIError(default_message, error_code)

def exception_factory(exception_name, exceptionType: CustomError, default_message="An exception occurred.") -> CustomError:
    """
    Factory function to create custom exception classes dynamically.
    :param default_message: The default error message for the exception.
    :return: The custom exception class.
    """
    return type(exception_name, (exceptionType,), {"message": default_message})

def DatabaseError(message):
    return exception_factory('DbError', X_Database, message)
