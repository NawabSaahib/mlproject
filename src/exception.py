import sys
import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="'time = '[%(asctime)s]'Line# = '%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
def error_message_detail(error, error_detail):    
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script '{0}' at line number {1}, and error details are: {2}".format(
        file_name, line_number, str(error))
    
    return error_message

class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

#if __name__=="__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Divide by zero")#
#        raise customException(e,sys)