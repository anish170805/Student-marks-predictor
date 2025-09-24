import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # gives exception info
    file_name = exc_tb.tb_frame.f_code.co_filename # gives file name where exception occurred

    # error message format
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} error message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys): # self is used to refer to current class instance
        super().__init__(error)  # calling parent class constructor
        self.error = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error