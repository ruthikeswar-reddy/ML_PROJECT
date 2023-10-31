import sys

def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # we get the filename of the file the error occured
    error_message = "Error occured in python script name [{0}] line number [{1}] and error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message
    

# try:
#     if 1/0:
#         print("true")
# except Exception as e:
#     raise CustomException(e, sys)

# sys is a module which deals with run time environment
#sys.exc_info gives all the details of the error like in which file it occured, line_number, error name,....
