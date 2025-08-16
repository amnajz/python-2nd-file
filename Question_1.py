def analyze_string(text: str, operations: list = ["length", "words", "chars"])-> dict:
    """
	Analyzes a given string based on specified operations.

	Args:
		text (str): The string to analyze
		operations (list): List of operations to perform (Default: ["length", "words", "chars"])

	Returns:
		dict: Results of each requested operation.
	"""
    dict = {}
    for op in operations:
        if op =="length":
            dict["length"]=len(text)
        elif op == "words":
            sp=text.split()
            dict["words"]=len(sp)
        elif op=="chars":
            dict["chars"]=len(text)
        elif op=="uppercase":
            dict["uppercase"]=text.upper()
        elif op == "lowercase":
            dict["lowercase"]=text.lower()
    return dict

def validation(operations):
    valid_op=["length","words","chars","uppercase","lowercase"]
   
    for op in operations:
        if op not in valid_op:
          return False
        return True
