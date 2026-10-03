import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

log_file_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

logging.basicConfig(filename=logs_path,level=logging.INFO)

if __name__ == "__main__":
    logging.info("Logging has started.")