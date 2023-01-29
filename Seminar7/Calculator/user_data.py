import logging


def rational_data():
    while True:
        try:
            num_1, num_2 = (float(input("Enter the first number: ")),
                            float(input("Enter the second number: ")))
        except ValueError:
            print("You didn't enter a number!!!!! Re-enter!!!!")
            logging.error("Incorrect user_data")
            continue
        else:
            return num_1, num_2


def complex_data():
    while True:
        try:
            actual_1, imaginary_1 = (float(input("Enter the actual part for the first number: ")),
                                     float(input("Enter the imaginary part for the first number: "))
                                     )
            num_1 = complex(actual_1, imaginary_1)
            print(num_1)
            actual_2, imaginary_2 = (float(input("Enter the actual part for the second number: ")),
                                     float(input("Enter the imaginary part for the second number: "))
                                     )
            num_2 = complex(actual_2, imaginary_2)
            print(num_2)
        except ValueError:
            logging.error("Incorrect user_data")
            print("You didn't enter a number!!!!! Re-enter!!!!")
            continue
        else:
            return num_1, num_2