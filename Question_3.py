def smart_format(template: str, data: dict) -> tuple:
    """
	Formats a string template by replacing placeholders with corresponding values from a dictionary.

	Args:
		template (str): The template string containing placeholders in curly braces
		data (dict): A dictionary where keys match the placeholders in the template

	Returns:
		tuple: 
			Formatted string with placeholders replaced by values from the dictionary.
			A dictionary with:
				"used": list of keys found and replaced in the template.
				"missing": list of keys not found.
	"""
    used = []
    missing = []

    for word in template.split("{"):
        if "}" in word:
            key = word.split("}")[0]
            if key in data:
                template = template.replace("{" + key + "}", str(data[key]))
                used.append(key)
            else:
                missing.append(key)

    return (template, {"used": used, "missing": missing})
