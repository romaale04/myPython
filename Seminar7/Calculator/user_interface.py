import logging
import keyboard
from check_mod import check_div_zero, check_int_div_op, check_rem_div_op
from user_data import rational_data, complex_data
from mod_calc import addition_op, composition_op, subtraction_op


def start_menu():
    while True:
        print("the number selection menu is rational or complex")
        logging.info('selection menu is rational or complex')
        type_numbers = input("Choosing the type of numbers\n"
                             "1 - Rational numbers\n"
                             "2 - Complex numbers\n"
                             "3 - Exit\n"
                             )
        match type_numbers:
            case "1" | "2":
                logging.info("Choosing the type of numbers")
                menu_calc(type_numbers)
            case "3":
                logging.info("Stop program")
                break
            case _:
                logging.error("Incorrect choice")
                print("Incorrect choice")


def menu_calc(type_numbers):
    while True:
        if type_numbers == "1":
            logging.info("rational numbers are selected")
            print("Calculator Menu")
            type_operation = input("Select the type of operation\n"
                                   "1 - Addition( + )\n"
                                   "2 - Subtraction( - )\n"
                                   "3 - Composition( * )\n"
                                   "4 - Division( / )\n"
                                   "5 - Integer division( // )\n"
                                   "6 - Remainder division( % )\n"
                                   "7 - Return to the start menu\n"
                                   )
            match type_operation:
                case "1":
                    logging.info("operation addition")
                    num_1, num_2 = rational_data()
                    print(f"result = {addition_op(num_1, num_2)}")
                    print("To continue, press the space bar")
                    pause()
                case "2":
                    logging.info("operation subtraction")
                    num_1, num_2 = rational_data()
                    print(f"result = {subtraction_op(num_1, num_2)}")
                    print("To continue, press the space bar")
                    pause()
                case "3":
                    logging.info("operation composition")
                    num_1, num_2 = rational_data()
                    print(f"result = {composition_op(num_1, num_2)}")
                    print("To continue, press the space bar")
                    pause()
                case "4":
                    logging.info("operation division")
                    num_1, num_2 = rational_data()
                    logging.info("check division by zero")
                    check_div_zero(num_1, num_2)
                    print("To continue, press the space bar")
                    pause()
                case "5":
                    logging.info("operation integer division")
                    num_1, num_2 = rational_data()
                    check_int_div_op(num_1, num_2)
                    print("To continue, press the space bar")
                    pause()
                case "6":
                    logging.info("operation remainder division")
                    num_1, num_2 = rational_data()
                    check_rem_div_op(num_1, num_2)
                    print("To continue, press the space bar")
                    pause()
                case "7":
                    logging.info("stop operation")
                    break
                case _:
                    logging.error("Incorrect choice")
                    print("Incorrect choice")
        elif type_numbers == "2":
            logging.info("complex numbers are selected")
            print("Calculator Menu")
            type_operation = input("Select the type of operation\n"
                                   "1 - Addition( + )\n"
                                   "2 - Subtraction( - )\n"
                                   "3 - Composition( * )\n"
                                   "4 - Division( / )\n"
                                   "5 - Return to the start menu\n"
                                   )
            match type_operation:
                case "1":
                    logging.info("operation addition")
                    num_1, num_2 = complex_data()
                    print(f"result = {addition_op(num_1, num_2)}")
                    print("To continue, press the space bar")
                    pause()
                case "2":
                    logging.info("operation subtraction")
                    num_1, num_2 = complex_data()
                    print(f"result = {subtraction_op(num_1, num_2)}")
                    print("To continue, press the space bar")
                    pause()
                case "3":
                    logging.info("operation composition")
                    num_1, num_2 = complex_data()
                    print(f"result = {composition_op(num_1, num_2)}")
                    print("To continue, press the space bar")
                    pause()
                case "4":
                    logging.info("operation division")
                    num_1, num_2 = complex_data()
                    logging.info("check division by zero")
                    check_div_zero(num_1, num_2)
                    print("To continue, press the space bar")
                    pause()
                case "5":
                    logging.info("stop operation")
                    break
                case _:
                    logging.error("Incorrect choice")
                    print("Incorrect choice")


def pause():
    while True:
        if keyboard.read_key() == 'space':
            break


start_menu()
