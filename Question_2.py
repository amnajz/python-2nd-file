def find_patterns(data_list: list, pattern_length: int = 2, min_occurrences: int = 2)-> dict:
    """
	Finds repeating patterns of a given length in a list and records their positions.

	Args:
		data_list (list): The list in which to search for patterns
		pattern_length (int): The number of consecutive elements to form a pattern
		min_occurrences (int): Minimum number of times a pattern must appear

	Returns:
		dict: Keys are patterns as tuples, values are lists of starting positions in data_list.
	"""
    pattern_dict = {}
    i = 0
    while i <= len(data_list) - pattern_length:
        pattern = tuple(data_list[i:i + pattern_length])
        if pattern not in pattern_dict:
            positions = []
            j = 0
            while j <= len(data_list) - pattern_length:
                if data_list[j:j + pattern_length] == list(pattern):
                    positions.append(j)
                j += 1
            if len(positions) >= min_occurrences:
                pattern_dict[pattern] = positions
        i += 1
    return pattern_dict
