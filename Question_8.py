def merge_lists(*lists: tuple, strategy: str = "zip", fill_value: str = None)-> list:
    """
    Merges multiple lists into a single result using different strategies.

    Args:
        *lists: One or more lists to merge
        strategy (str, optional): The merging strategy to use (Default: "zip")
        fill_value (str, optional): Value to use for missing elements

    Returns:
        list: A list containing the merged elements according to the selected strategy.
    """
    result = []

    if strategy == "zip":
        max_len = max(len(lst) for lst in lists)
        for i in range(max_len):
            tuple_row = []
            for lst in lists:
                if i < len(lst):
                    tuple_row.append(lst[i])
                else:
                    tuple_row.append(fill_value)
            result.append(tuple(tuple_row))

    elif strategy == "chain":
        for lst in lists:
            for item in lst:
                result.append(item)

    elif strategy == "alternate":
        max_len = max(len(lst) for lst in lists)
        for i in range(max_len):
            for lst in lists:
                if i < len(lst):
                    result.append(lst[i])

    elif strategy == "unique":
        seen = []
        for lst in lists:
            for item in lst:
                duplicate = False
                for x in seen:
                    if item == x and type(item) == type(x):
                        duplicate = True
                        break
                if not duplicate:
                    seen.append(item)
        result = seen
    
    return result
