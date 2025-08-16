
import Question_1
import Question_2
import Question_3
import Question_4
import Question_5
import Question_6
import Question_7
import Question_8
import Question_9
import Question_10

while True:
    print(" 1: String Analyzer \n 2: List Pattern Finder \n 3: String Formatter with Templates \n 4: List Transformer \n 5: String Encryption/Decryption \n 6: List Statistics Calculator \n 7: String Parser with Rules \n 8: Advanced List Merger \n 9: String Pattern Generator \n 10: List-Based Text Processor")
    input_user=input("Which function do u want to run(Type exit if u don't want to run): ")
    if input_user=='1':
        text_in = input("Enter text: ")
        choiceO = input("Do u want to specify operations on text? (Answer in yes/no)(Default: length, words, chars) ")
        if choiceO == "yes":
            op_input = input("Enter operations (only include length, words, chars, uppercase and lowercase): ")
            while not Question_1.validation([ops.strip() for ops in op_input.split(',')]):
                op_input = input("Please choose only allowed operations(length, words, chars, uppercase and lowercase): ")
            op_input = [ops.strip() for ops in op_input.split(',')]
            print(Question_1.analyze_string(text_in, op_input))
        else:
            print(Question_1.analyze_string(text_in))
    elif input_user=='2':
        list_in = input("Enter data (comma separated): ")
        list_in = [dataL.strip() for dataL in list_in.split(',')]
        choice_length = input("Do u want to enter pattern length (Default: 2)(If u want to specify enter yes): ")
        choice_minOccurance = input("Do u want to enter min occurance required? (Default: 2)(If u want to specify enter yes): ")

        if choice_length == "yes":
            length_in = input("Enter length: ")
            length_in = int(length_in)
            if choice_minOccurance == "yes":
                occurance_in = input("Enter occurance: ")
                occurance_in = int(occurance_in)
                print(Question_2.find_patterns(list_in, length_in, occurance_in))
            else:
                print(Question_2.find_patterns(list_in, length_in))

        else:
            if choice_minOccurance == "yes":
                occurance_in = input("Enter occurance: ")
                occurance_in = int(occurance_in)
                print(Question_2.find_patterns(list_in, min_occurrences = occurance_in))
            else:
                print(Question_2.find_patterns(list_in))

        
    elif input_user=='3':
        template_in = input("Enter template: ")
        placeHolder_in = eval(input("Enter dict of placeholders where keys match the placeholders in the template: "))
        print(Question_3.smart_format(template_in, placeHolder_in))
  
    elif input_user=='4':
        transfomList_in = input("Enter list to transform: ")
        transfomList_in = [item.strip() for item in transfomList_in.split(',')]
        rules_in = eval(input("Enter rules(reverse, sort, unique, flatten) in dict form like {\"sort\": True, \"unique\": True}: "))       
        print(Question_4.transform_list(transfomList_in, rules_in))                               
    elif input_user=='5':
        in_text = input("Enter text: ")
        choiceShift=input("Do u want to specify shift(By default: 3)(if yes then Answer in yes): ")
        choiceMode=input("Do u want to specify mode (By default: encrypt)(if yes then Answer in yes): ")
        if choiceShift == "yes":
            input_shift = int(input("Enter shift in digits: "))
            if choiceMode=="yes":
                input_mode = input("Enter mode (encrypt, decrypt): ")
                print(Question_5.caesar_cipher(in_text, input_shift, input_mode))
            else:
                print(Question_5.caesar_cipher(in_text, input_shift))
        else:
            if choiceMode=="yes":
                input_mode = input("Enter mode (encrypt, decrypt): ")
                print(Question_5.caesar_cipher(in_text, mode= input_mode))
            else:
                print(Question_5.caesar_cipher(in_text))
    elif input_user=='6':
        num_in = input("Enter numbers with ,: ")
        num_in = [float(op.strip()) if '.' in op else int(op.strip()) for op in num_in.split(',')]
        choiceOp = input("Do u want to spcify operations? Answer in yes if u want (Default: None ): ")
        choicePercision = input("Do u want to spcify percision? Answer in yes if u want (Default: 2): ")
        if choiceOp == "yes":
            input_op = input("Enter operations(mean,median,mode, or range) with ,:" )
            input_op = [op.strip() for op in input_op.split(',') ]
            if choicePercision == "yes":
                input_p = int(input("Enter percision: "))
                print(Question_6.calculate_stats(num_in, input_op, input_p))
            else:
                print(Question_6.calculate_stats(num_in, input_op))
        else:
            if choicePercision == "yes":
                input_p = int(input("Enter percision: "))
                print(Question_6.calculate_stats(num_in, input_op, input_p))
            else:
                print(Question_6.calculate_stats(num_in, input_op))
    elif input_user=='7':
        input_text = input("Enter text: ")
        input_rules = eval(input("Enter rules(reverse, capitalize, upeer, remove) in dict form like {\"1\": \"upper\", \"2\": \"reverse\"}): "))
        choiceDelimeter = ("Do u want to spcify delimiter? Answer in yes if u want (Default: ' '): ")
        if choiceDelimeter == "yes":
            input_deli = input("Enter delimiter only 1 character: ")
            print(Question_7.parse_string(input_text, input_rules, input_deli))
        else:
            print(Question_7.parse_string(input_text, input_rules))
    elif input_user=='8':
        num_lists = int(input("How many lists do you want to merge? "))
        lists_data = []
    
        for i in range(num_lists):
            lst = input(f"Enter list {i+1} (comma separated): ").split(",")
            lst = [item.strip() for item in lst]
            lists_data.append(lst)
    
        print("\nChoose a merging strategy:")
        print(" 1. zip \n 2. chain \n 3.alternate \n 4. unique")
        choice = input("Enter choice (1,2,3 or 4): ")
        if choice == "1":
            strategy = "zip"
        elif choice == "2":
            strategy = "chain"
        elif choice == "3":
            strategy = "alternate"
        elif choice == "4":
            strategy = "unique"
        else:
            print("Invalid choice. Using default 'zip'.")
            strategy = "zip"
    
        choiceD = input("Do u want to spcify delimiter? Answer in yes if u want (Default: ' '): ")
        if choiceD == "yes":
            inputD = input("Enter a single delimiter: ")
            if len(inputD) != 1:
                inputD = " "
            print(Question_8.merge_lists(*lists_data, strategy = strategy, fill_value = inputD))
        else:
            print(Question_8.merge_lists(*lists_data, strategy = strategy))
    elif input_user=='9':
        input_base = input("Enter starting of pattern: ")
        input_count = int(input("Enter count: "))
        print("Do u want to specify separator? \n 1. yes \n 2. no")
        choiceS = input("Coose 1 or 2: ")
        inputS = ""
        if choiceS == "1":
            inputS = input("Enter separator: ")
        print("Do u want to specify operations? \n 1. yes \n 2. no")
        choice_O = input("Coose 1 or 2: ")
        inputOp = None
        if choice_O == "1":
            inputOp = input("Enter operations with comma(,): ")
            inputOp = [item.strip() for item in inputOp.split(',')]
        print(Question_9.generate_pattern(input_base, input_count, inputS, inputOp))
    elif input_user=='10':
        text = input("Enter text: ")
        print("Applies multiple processing steps from config: \n Filter by: length, starts_with, ends_with \n Transform: capitalize, reverse, encode \n Sort by: alphabetical, length, frequency")
        config = eval(input("Enter config: "))
        print(Question_10.process_text_data(text, config))
    elif input_user=="exit":
        break
    