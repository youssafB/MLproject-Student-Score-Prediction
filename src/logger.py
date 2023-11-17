# this file is for the purpose that any excustion happnes shud be able to log all these information in 
# some files (tracking also if there some erors )


import logging
import sys
import os
from datetime import datetime

# Create a log file name based on the current date and time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create a path to the 'logs' directory in the current working directory
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)      ## LOG_FILE !! ##
# Ensure that the 'logs' directory exists, and create it if it doesn't
os.makedirs(logs_path,exist_ok=True)
# Create the full path to the log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
     # Specify the log message format
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Set the logging level to INFO 
    level=logging.INFO,


)


