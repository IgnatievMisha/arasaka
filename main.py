import logging
import random
#1
class Calculator:
    def __init__(self):
        self.logger=logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self, a, b):
        result =  a + b
        self.logger.info(f"{a} + {b} = {result}")
        return result
    def sub(self, a, b):
        result = a - b
        self.logger.info(f"{a} - {b} = {result}")
        return result
    def mult(self, a, b):
        result = a * b
        self.logger.info(f"{a} * {b} = {result}")
        return result
    def div(self, a, b):
        result = a / b
        self.logger.info(f"{a} / {b} = {result}")
        return result
calc=Calculator()
calc.add(6, 5)
calc.sub(1, 1)


#2
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename="loggy.log", filemode="w")
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")

def write_file(fill_path, data):
    try:
        with open(fill_path, "w") as file:
            file.write(data)
        logging.info("succesfully writed")
    except Exception as e:
        logging.error(f"error {e} in {fill_path}")

write_file("output.txt", input())





#3
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename="ex3.log", filemode="w")
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")
def rand_file(fill_path, num):
    try:
        with open(fill_path, "w") as file:
            for i in range(num):
                rand=random.randint(1, 10)
            file.write(rand)
        logging.info("succesfully writed")
    except Exception as k:
        logging.error(f"error {k} in {fill_path}")

rand_file("qpqpqp.txt", int(input()))