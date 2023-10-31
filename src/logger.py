# logger is to maintain the log table details
# it is used to maintain the details of your changes,working,executions

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#this variable gives month_day_year_hour_minute_second
logs_path =os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ =="__main__":
    logging.info("Logging has started")
