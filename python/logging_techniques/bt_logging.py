import logging
import logging.handlers
import logging.config


#logging.config.fileConfig('loggly.conf', disable_existing_loggers=False)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("test.log"),
        logging.StreamHandler(),
        logging.handlers.RotatingFileHandler("rot_test.log", maxBytes=(1048576*5), backupCount=7)
    ])
logging.info("info test")
logging.debug("debug message")
logging.error("should not occur at all")