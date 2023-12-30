import logging


logger = logging.getLogger(name="Module 1 Level 2")


def hello_from_module_2_1():
    logger.info(f"Hello from {__name__}")


class SomeImportantClass:
    def __init__(self):
        self.logger = logging.getLogger(name=self.__class__.__name__)

    def hello_from_important_class(self):
        self.logger.info("Doing some stuff within class..")