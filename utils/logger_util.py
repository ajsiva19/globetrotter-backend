import logging
from logging.config import dictConfig

# Define the logging configuration
# LOGGING_CONFIG = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s - %(levelname)s - %(message)s",
#         },
#     },
#     "handlers": {
#         "console": { 
#             "class": "logging.StreamHandler",
#             "formatter": "default",
#         },
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "app.log",
#             "formatter": "default",
#         },
#     },
#     "root": {
#         "level": "INFO",
#         "handlers": ["console", "file"],
#     },
#     "loggers": {
#         "uvicorn": {
#             "level": "INFO",
#             "handlers": ["console"],
#             "propagate": False,
#         },
#     },
# }

# # Apply logging configuration
# dictConfig(LOGGING_CONFIG)
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO
)
# Create and configure the logger
logger = logging.getLogger(__name__)
