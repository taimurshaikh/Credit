import sys
import os
import time
import random

def main():
  result = 1

  while result:
      ask = input("Choose an option:\n1. Check my Card\n2. Import numbers to check\n3. Generate valid CC numbers\n4. Quit ")
      menuOptions = [str(x) for x in range(1, 5)]
      while ask not in menuOptions:
          print()
          ask = input("Choose an option:\n1. Check my Card\n2. Import numbers to check\n3. Generate valid CC numbers\n4. Quit ")

      result = 0

      if ask == "1": result = checkUserCard()
      elif ask == "2": result = importNumbers()
      elif ask == "3": result = generateNumbers()
      else: result = quit()

def luhnsAlgorithm(sequence):

    # Creating new string sequence with every other digit * 2, starting from second to last digit
    eod = ''.join([str(int(x) * 2) for x in sequence[::-1][1::2]])

    # Add eod's DIGITS together
    eodDigitSum = sum([int(x) for x in eod])

    # Sum of digits that weren't multiplied by 2
    everythingElse = sum([int(x) for x in sequence[::-1][::2]])

    total = eodDigitSum + everythingElse

    # CC is valid if last digit is 0
    return True if str(total)[-1] == "0" else False

def isValidSequence(sequence):
    if len(sequence) != 16:
        print("\nINVALID LENGTH OF CC NUMBER\n")
        return 0
    try:
        ask = int(sequence)
    except ValueError:
        print("\nCC NUMBER CANNOT CONTAIN LETTERS\n")
        return 0
    return 1

def isValidInt(num):
    try:
        num = int(num)
    except ValueError:
        return 0
    if num < 1 or num > 100: return 0
    return 1

def checkUserCard():
    userIn = input("Enter credit card number: ")

    while not isValidSequence(userIn):
        userIn = input("Enter credit card number: ")

    if not luhnsAlgorithm(userIn):
        print("\nCC NUMBER IS INVALID\n")

    else:
        print("\nCC NUMBER IS VALID\n")
    return True

def importNumbers():

    # Check if file exists
    userIn = input("Enter file path: ")
    while not os.path.exists(userIn):
        userIn = input("Invalid file path. Try again: ")

    # Reading file and validating each line
    with open(userIn, "r") as f:
        for i, line in enumerate(f.readlines()):

            # Ignores the empty line at the end of the file
            if not line: continue

            # First we must check if the line obeys the constraints of the CC number(length 16, no non-integers)
            if not isValidSequence(line.strip()):
                print(line.strip())
                print(f"Line {i+1} is NOT a valid CC number")
                time.sleep(0.5)
                continue
            if luhnsAlgorithm(line.strip()):
                print(f"Line {i+1} is a valid CC number")
                time.sleep(0.5)
            else:
                print(f"Line {i+1} is NOT a valid CC number")
                time.sleep(0.5)
    print("\n")
    return 1

def generateNumbers():

    userIn = input("How many CC numbers would you like to generate? ")

    # Validating the number inputted
    while not isValidInt(userIn):
        userIn = input("Invalid input. Try again: ")

    userIn = int(userIn)

    res_lst = []
    # Generating random 16 digit sequences and checking if they follow the checksum
    # NOTE: Probably a better way to do this. This is a brute force approach
    while len(res_lst) != userIn:
        randSequence = ''.join([str(random.randint(0, 9)) for i in range(16)])

        if luhnsAlgorithm(randSequence) and randSequence not in res_lst:
            res_lst.append(randSequence)

    print('\n'.join(res_lst))

    # Creating new file with generated CC numbers
    with open("generated.txt", "w") as f:
        for res in res_lst:
            f.write(res + "\n")
    print("New file created.\n")
    return 1

def quit():
    ask = input("Are you sure want to quit? ").lower()
    menuOptions = ["y", "yes", "n", "no"]
    while ask not in menuOptions:
        ask = input("Are you sure want to quit? ").lower()
    if ask == "y" or ask == "yes":
        sys.exit()
    elif ask == "n" or ask == "no":
        return 1

if __name__ == "__main__":
    main()
