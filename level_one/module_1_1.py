import logging

from level_one.level_two.module_2_1 import hello_from_module_2_1

logger = logging.getLogger(name="Module 1 Level 1")

def hello_from_module_1_1():
    logger.info(f"Hello from {__name__}")

def circular_action_with_log_supression(iteration_count, supress=True):
    suppression = "with" if supress else "without"
    logger.info(f"Calling level 2 function {suppression} suppression {iteration_count} times.")
    initial_logger_level = logger.root.getEffectiveLevel()
    if supress:
        logger.root.setLevel(logging.ERROR)
    for iteration in range(iteration_count):
        logger.info(f"Calling level 2 function {iteration} times.")
        hello_from_module_2_1()
    logger.root.setLevel(initial_logger_level)
