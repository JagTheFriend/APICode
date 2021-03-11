FORMAT: {str: str} = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def main(*, hex_code: str) -> dict:
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
