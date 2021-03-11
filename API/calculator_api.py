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
