import os
import wandbox as wand
import re
import textwrap

CODE_TXT = "compile.txt"
OUTPUT_TXT = "output.txt"

ESCAPE_REGEX = re.compile("[`\u202E\u200B]{3,}")
FORMATTED_CODE_REGEX = re.compile(
    r"(?P<delim>(?P<block>```)|``?)"
    r"(?(block)(?:(?P<lang>[a-z]+)\n)?)"
    r"(?:[ \t]*\n)*"
    r"(?P<code>.*?)"
    r"\s*"
    r"(?P=delim)",
    re.DOTALL | re.IGNORECASE
)

RAW_CODE_REGEX = re.compile(
    r"^(?:[ \t]*\n)*"
    r"(?P<code>.*?)"
    r"\s*$",
    re.DOTALL
)

LANGUAGES = [
    "Bash(Language Name: bash)",
    "CPP(Language Name: cxx)",
    "C#(Language Name: cs)",

    "Elixir(Language Name: elixir)",
    "Haskell(Language Name: ghc)",
    "Java(Language Name: java)",

    "JavaScript(Language Name: js)",
    "Nim(Language Name: nim)",
    "Python(LanguageName: python)",
    "Ruby(Language Name: ruby)",

    "Swift(Language Name: swift)",
]


def prepare_input(code: str) -> str:
    """
    Returns the code to be run
    """

    # easiest way to fix the bug:
    try:
        match = list(FORMATTED_CODE_REGEX.finditer(code))
        if match:
            blocks = [block for block in match if block.group("block")]

            if len(blocks) > 1:
                code = '\n'.join(block.group("code") for block in blocks)

            else:
                match = match[0] if len(blocks) == 0 else blocks[0]

                code, block, lang, delim = match.group(
                    "code", "block", "lang", "delim")

        else:
            code = RAW_CODE_REGEX.fullmatch(code).group("code")

        code = textwrap.dedent(code)
        return code

    except Exception:
        code = "No_code"
        return code


def _compile(*, lang: str, code: str = "") -> dict:
    """
    To allow users to run code

    Arguments:
        @code => Code to be compiled and ran
        @lang => The langage used for compiling the code

    :return: Python dictionary
    """

    result = {}
    result["output"] = ""

    if lang == "support":
        result["SupportedLanguages"] = LANGUAGES
        return result

    # check whether the lang is valid or not
    if lang not in [i.split(":")[-1].strip(" ").strip(")") for i in LANGUAGES]:
        result["output"] = "Language not recognized"
        result["SupportedLanguages"] = LANGUAGES
        return result

    _code = prepare_input(code)  # getting the code
    if _code == "No_code":  # no code is given
        result["output"] = "Please send the code to be run"
        return result

    # store the code in a file
    with open(CODE_TXT, "w") as f:
        f.write(f"{_code}")

    # compile the file, and store the output in a different file
    os.system(f"wandbox-{lang} run {CODE_TXT} > {OUTPUT_TXT}")

    # loading the data
    with open(OUTPUT_TXT, "r") as f:
        data = f.read()

    data = data[len("program_message:\n"):-2]
    result["output"] = f"{data}"
    return result
