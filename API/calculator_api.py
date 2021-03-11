<<<<<<< HEAD
FORMAT: {str: int} = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}


=======
>>>>>>> 9ec4e891975e502ac7df41e7e5beae0967cf3536
def main(*, equation: str) -> dict:
    """
    Gets the result of a calculation

    Arguments:
        @formula => Stuff on which calculation will be carried on Example: 5+7*9

    :return: Python dictionary
    """

    try:
        new_equation = equation.replace("^", "**")
        return {"output": f"{str(eval(new_equation))}"}
    except Exception:
        return {"output": "Please write the formula properly"}
<<<<<<< HEAD


def hex_denary(*, hex_code: str) -> dict:
    """
    Gets the result of a calculation

    Arguments:
        @hex_code => This the hexadecimal code given by the user

    :return: Python dictionary
    """

    answere = 0
    power = len(hex_code) - 1
    for digit in hex_code:
        answere += FORMAT[digit]*16**power
        power -= 1

    return {"output": str(answere)}
=======
>>>>>>> 9ec4e891975e502ac7df41e7e5beae0967cf3536
