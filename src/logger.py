# importr lib
import sys
import logging
import os

from datetime import datetime

# save which time and date logs created 

Log_time  = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S ')}.logs"

log_file = os.path.join(os.getcwd() ,"logs" , Log_time)


os.makedirs(log_file , exist_ok= True)

file_path = os.path.join(log_file , Log_time)

logging.basicConfig(
    filename =  file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == 'main':
    logging.info("Logging Started")

