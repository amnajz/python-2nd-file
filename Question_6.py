def calculate_stats(numbers: list, operations: list = None, precision: int = 2)-> dict:
    """
	Calculates statistical measures for a given list of numbers based on specified operations.

	Args:
		numbers (list): A list of values to analyze (Can contain integers, floats, or strings (only allowed for 'mode'))
		operations (list, optional): A list of statistical operations to perform
		precision (int, optional): Number of decimal places to round numeric results to (Default: 2)

	Returns:
		dict: A dictionary with operation names as keys and their calculated values as results.
    """
    
    result={}
    possible= True
    for num in numbers:
        if not isinstance(num,(float,int)):
            possible=False
            break
    for op in operations:
        if op == "mean" and possible:
            mean=0
            for num in numbers:
                mean+=num
            mean/=len(numbers)
            result["mean"]= round(mean, precision)
        elif op == "median" and possible:
            median=0
            if len(numbers) % 2 == 0:
                median = (numbers[int(len(numbers)/2) - 1] + numbers[int(len(numbers)/2)])/2
            else:
                median = numbers[int(len(numbers)//2)]
            result["median"]=round(median, precision)
        elif op == "mode":
            highest_count=0
            mode=[]
            for num in numbers:
                if isinstance(num,(float,int,str)):
                    if numbers.count(num)> highest_count:
                        highest_count=numbers.count(num)
                        mode = [num]
                    elif numbers.count(num) == highest_count and num not in mode:
                        mode.append(num)
                    if highest_count == 1:
                        mode=[0]
                else:
                    mode=[0]
                    break
            result["mode"]=mode
        elif op == "range" and possible:
            
            range = max(numbers)-min(numbers)
            result["range"]= round(range, precision)
    return result
