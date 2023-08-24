import sys
from src.logger import logging

def errorMessageDetails(error, errorDetails:sys):
    _,_,exc_tb = errorDetails.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    return f"Error Occurred in file name: {fileName} in line no.{exc_tb.tb_lineno} error message: {str(error)}"


class CustomException(Exception):
    def __init__(self, errorMessage, error_detail: sys):
        super().__init__(errorMessage)
        self.errorMessage = errorMessageDetails(errorMessage, error_detail)

    def __str__(self):
        return self.errorMessage
    