import logging
import logging.handlers

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("logs/cinema.log")

file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(file_format)
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

