# log-decorator.py
import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        result = func(*args, **kwargs)
        logger.info(f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def always_true(*args):
    return True

@logger_decorator
def return_logger(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    always_true(1, 2, 3)
    return_logger(test=1, example=2)