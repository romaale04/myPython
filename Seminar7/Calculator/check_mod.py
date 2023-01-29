import logging
from mod_calc import division_op, int_div_op, rem_div_op


def check_div_zero(num_1, num_2):
    try:
        print(f"result = {division_op(num_1, num_2)}")
    except ZeroDivisionError:
        logging.error("division by zero")
        print("You can't divide by zero!!!!!! Enter the correct data!!!!")


def check_int_div_op(num_1, num_2):
    try:
        print(f"result = {int_div_op(num_1, num_2)}")
    except ZeroDivisionError:
        logging.error("division by zero")
        print("You can't divide by zero!!!!!! Enter the correct data!!!!")


def check_rem_div_op(num_1, num_2):
    try:
        print(f"result = {rem_div_op(num_1, num_2)}")
    except ZeroDivisionError:
        logging.error("division by zero")
        print("You can't divide by zero!!!!!! Enter the correct data!!!!")