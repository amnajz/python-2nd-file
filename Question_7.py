def parse_string(text: str, rules: dict, delimiter: str = " ")-> str:
    """
    Parses and transforms specific words in a string based on given rules.

    Args:
        text (str): The string to perform rules
        rules (dict): A dictionary where each key is a word index (as a string) and value is rule to apply
        delimiter (str, optional): The character(s) used to split and join words (Default: " ")

    Returns:
        str: The string after applying all specified rules.
    """

    words=text.split(delimiter)

    for key in rules:

        if rules[key] == "reverse":
            words[int(key)] = words[int(key)][::-1]

        elif rules[key] == "capitalize":
            words[int(key)] = words[int(key)].capitalize()
            
        elif rules[key] == "upper":
            words[int(key)] = words[int(key)].upper()

        elif rules[key] == "remove":
            words[int(key)] = ''

    resulted = delimiter.join(words)
    return resulted
