import math

def main():
    
    ################## BASICS OF STRINGS ###############################################
    print("\n################## BASICS OF STRINGS ##################\n")
    first = "frances"
    last = "belleza"
    full = f"{first} {last}"
   
    # len() --> is a function 
    # first.find() --> is a function AKA method for the string

    print(first[0:2]) #prints the values in place 0 to 1, go up to 2
    print(first[-1]) #goes back from 0, so in 'frances' it'll be s
    print(first[:3]) #prints up until the third value 0 = f, 1 = r, 2 = a
    print(last[2:]) # prints from the 2nd value onward, b-0, e-1, l-2 so prints "lleza"

    print(full.title(), " -> upper cases the beginning ") 
    print(full.upper(), " -> turns everything into uppercase, can do the same for .lower() ") 
    print(full.replace('a', 'v'), " -> replaces a with v") 
    print(full.find("e"), " -> returns how many times something appeared in string") 
    print("fran" in first, " -> returns boolean")
    print("fran" not in full, " -> checks to see if fran is in full and returns a boolean") 


    ################## IMPORTANT FUNCTIONS FOR WORKING WITH NUMBERS ###################
    print("\n\n\n\n################## IMPORTANT FUNCTIONS FOR WORKING WITH NUMBERS ###################\n")
    print(round(2.7)) # rounds number
    print(abs(-2)) # absolute value of number
    print(math.ceil(9.7)) # prints ceiling of number
    print(math.floor(9.7)) # prints floor of number

    ## conversions ##
    # int()
    # float()
    # bool()
    # str()

    ################### taking inputs ###################################################
    # note: inputs are automatically taken in as strings

    num = input('num: ')


    ## falsy values ##
    # "" -> empty strings
    # 0 -> number zero
    # None -> empty things
    # 
    # everything else is true



    ######################## if statements #####################################################################
    print("\n\n\n\n######################## if statements ########################\n")

    x = 5
   
   # ternary operator --> is a one line if statement, format is: value_if_true if condition else value_if_false
    message = "x is greater than 5" if int(num) > x else "x is 5" if int(num) == x else "x is less than 5"

    add_three = int(num) + 3
    print(f"your new number when added with three is {add_three}")


    ######################## logical operators and comparison operators #####################################################################
    print("\n\n\n\n######################## logical operators and comparison operators ########################\n")

    print("logical operators: and, or, not")
    print("comparison operators: ==, !=, >, <, >=, <=")



if __name__ == "__main__":
    main()