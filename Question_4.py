def transform_list(lst: list, rules: dict)-> tuple:
    """
        Transforms a list based on the specified rules.

        Args:
            lst (list): The list to transform
            rules (dict): A dictionary specifying rules

        Returns:
            tuple: A tuple containing:
                list: The transformed list
                list: A log of applied transformations
    """
    log = []
    for key in rules:
        if key == "flatten" and rules[key]:
            flat = []
            for item in lst:
                if isinstance(item, list):
                    flat.extend(item)
                else:
                    flat.append(item)
            lst=flat
            log.append("Flatten list")
        elif key == "reverse" and rules[key]:
            lst.reverse()
            log.append("Reversed list")
        elif key == "sort" and rules[key]:
            try:
                lst.sort()
                log.append("Sorted list")
            except:
                log.append("Sorting not possible")
        elif key == "unique" and rules[key]:
            unique=[]
            msg="Removed duplicates: "
            for x in lst:
                if x not in unique:
                    unique.append(x)
                else:
                    msg+="{} ,".format(x)
            if msg[-1] == ',':
                msg = msg[:-1]
            log.append(msg)
            lst=unique
            #print(lst)
    return (lst,log)     
