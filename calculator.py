#!/usr/bin/env python
import sys
import os
import time
import logging
sys.dont_write_bytecode = True
from datetime import datetime

start_dt = datetime.now()

class Calculator(object):

    def __init__(self):
        logging.info("We are now initializing the calculator")
        logging.info("Please run your first calculation!")

    def addition(self, to_be_calculated, **kwargs):
        logging.info("Conducting the requested addition: {}".format(to_be_calculated))
        to_be_calculated_split = to_be_calculated.split(' ')
        return float(to_be_calculated_split[0]) + float(to_be_calculated_split[2])

    def subtraction(self, to_be_calculated, **kwargs):
        logging.info("Conducting the requested subtraction: {}".format(to_be_calculated))
        to_be_calculated_split = to_be_calculated.split(' ')
        return float(to_be_calculated_split[0]) - float(to_be_calculated_split[2])

    def division(self, to_be_calculated, **kwargs):
        logging.info("Conducting the requested division: {}".format(to_be_calculated))
        to_be_calculated_split = to_be_calculated.split(' ')
        return float(to_be_calculated_split[0]) / float(to_be_calculated_split[2])

    def multiplication(self, to_be_calculated, **kwargs):
        logging.info("Conducting the requested multiplication: {}".format(to_be_calculated))
        to_be_calculated_split = to_be_calculated.split(' ')
        return float(to_be_calculated_split[0]) * float(to_be_calculated_split[2])

    def parseInput(self, input, calc, **kwargs):
        if input.find('+') > 1:
            calc = calc.addition(input)
        elif input.find('-') > 1:
            calc = calc.subtraction(input)
        elif input.find('*') > 1:
            calc = calc.multiplication(input)
        elif input.find('/') > 1:
            calc = calc.division(input)
        else:
            logging.error("We did not find a mathematical operator in the requested calculation!")
            sys.exit(1)
        return calc

def run_calc(calc):
    logging.info("Would you like to run a calculation? Y for Yes, N for No")
    request_calc = raw_input()
    if request_calc == 'Y':
        logging.info("Please enter your calculation:")
        calc_request = raw_input()
        calc = calc.parseInput(calc_request, calc)
        logging.info("The answer is: {}".format(calc))
        calc = Calculator()
        run_calc(calc)
    else:
        sys.exit(0)

if '__main__' == __name__:

    log_level = os.environ.get('PY_LOG_LVL', 'INFO')
    logging.basicConfig(level=getattr(logging, log_level), format="%(asctime)s::%(filename)s::%(lineno)d::%(levelname)s|| %(message)s")

    try:
        answer = Calculator()
        run_calc(answer)
        sys.exit(0)
    except Exception as e:
        logging.exception(e)
    logging.error("Closing with errors after {}".format(datetime.now() - start_dt))
    sys.exit(1)
