def process_text_data(text: str, config: dict)-> tuple:
    """
    Processes text according to filtering, transformation, and sorting rules.

    Parameters:
        text (str): The input text to process
        config (dict): Configuration dictionary with optional keys
           
    Returns:
        tuple: 
            - list: The processed list of words after applying all rules.
            - dict: Statistics with keys:
                * "total" (int): Total number of processed words.
                * "unique" (int): Count of unique words in processed output.
    """

    words = text.split()
    if "filter" in config:
        min_len = config["filter"].get("min_length", 0)
        starts = config["filter"].get("starts_with", [])
        ends = config["filter"].get("ends_with", [])
        filtered = []
        for w in words:
            if len(w) < min_len:
                continue
            if starts:
                match_s = False
                for s in starts:
                    if w.startswith(s):
                        match_s = True
                if not match_s:
                    continue
            if ends:
                match_e = False
                for e in ends:
                    if w.endswith(e):
                        match_e = True
                if not match_e:
                    continue
            filtered.append(w)
        words = filtered
    if "transform" in config:
        transforms = config["transform"]
        if "capitalize" in transforms:
            words = [w.capitalize() for w in words]
        if "reverse" in transforms:
            words = [w[::-1] for w in words]
        if "encode" in transforms:
            words = [str(ord(ch)) for w in words for ch in w]
    if "sort" in config:
        if config["sort"] == "alphabetical":
            words = sorted(words)
        elif config["sort"] == "length":
            words = sorted(words, key=len)
        elif config["sort"] == "frequency":
            freq = {w: words.count(w) for w in set(words)}
            def sort_key(word):
                return (-freq[word], word)
            words = sorted(words, key=sort_key)
    stats = {
        "total": len(words),
        "unique": len(set(words))
    }
    return (words, stats)
