################################################################################
# Copyright (c) 2021 JagTheFriend
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

FORMAT: {str: int} = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def main(*, equation: str) -> dict:
    """
    Gets the result of a calculation
    :param formula: Stuff on which calculation will be carried on Example: 5+7*9
    :return: Dictionary
    """
    try:
        new_equation = equation.replace("^", "**")
        new_equation = equation.replace("\\", "/")
        return {"output": f"{str(eval(new_equation))}"}
    except Exception:
        return {"output": "Please write the formula properly"}


def hex_denary(*, hex_code: str) -> dict:
    """
    Converts hexadecimal to decimal
    :param hex_code: This is the hexadecimal code given by the user
    :return: Dictionary
    """
    answere = 0
    power = len(hex_code) - 1
    for digit in hex_code:
        answere += FORMAT[digit]*16**power
        power -= 1

    return {"output": str(answere)}


def denary_binary(*, binary) -> dict:
    """
    Converts decimal to binary
    :param binary: This is the decimal code given by the user
    :return: Dictionary
    """
    return {"output": ''.join(format(ord(i), '08b') for i in binary)}
