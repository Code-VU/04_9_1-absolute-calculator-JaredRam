def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = (int(input("Enter a number: ")))

    if in_num <= 21:
        difference = 21 - in_num

    else:
        difference = (in_num - 21) * 2
    
    print("Result:", difference)
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
