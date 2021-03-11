FORMAT: {str: str} = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


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


def hex_denary(*, hex_code: str) -> dict:
    """
    Gets the result of a calculation

    Arguments:
        @hex_code => This the hexadecimal code given by the user

    :return: Python dictionary
    """

    hex_code = list(hex_code)
    for e, i in enumerate(hex_code):
        if i in FORMAT:
            hex_code[e] = f"{FORMAT[i]}"

    return {"output": ''.join(hex_code)}
