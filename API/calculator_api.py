def main(*, equation: str):
    try:
        new_equation = equation.replace("^", "**")
        return str(eval(new_equation))
    except Exception:
        return "Please write the formula properly"
