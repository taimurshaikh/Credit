import sys
import os
import time

def main():
  result = 1

  while result:
      ask = input("""Choose an option:
    1. Check my Card
    2. Import numbers to check
    3. Generate a valid CC number
    4. Quit """)
      menuOptions = [str(x) for x in range(1, 5)]
      while ask not in menuOptions:
          print()
          ask = input("""Choose an option:
          1. Check my Card
          2. Import numbers to check
          3. Generate a valid CC number
          4. Quit """)

      result = 0

      if ask == "1": checkUserCard()
      elif ask == "2": importNumbers()
      elif ask == "3": generateNumbers()
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

def isValid(sequence):
    if len(sequence) != 16:
        print("\nINVALID LENGTH OF CC NUMBER\n")
        return 0
    try:
        ask = int(sequence)
    except ValueError:
        print("\nCC NUMBER CANNOT CONTAIN LETTERS\n")
        return 0
    return 1

def checkUserCard():
    userIn = input("Enter credit card number:\n")

    if not isValid(userIn):
        return False

    if luhnsAlgorithm(userIn):
        print("\nCC NUMBER IS VALID\n")
        return True

    print("\nCC NUMBER IS INVALID\n")
    return False

def importNumbers():

    # VALIDATION
    userIn = input("Enter file path:\n")
    while not os.path.exists(userIn):
        userIn = input("Invalid file path. Try again:\n")

    # READING FILE and VALIDATING LINES
    with open(userIn, "r") as f:
        for i, line in enumerate(f.readlines()):

            # First we must check if the line obeys the constraints of the CC number(length 16, no non-integers)
            if not isValid(line.strip()):
                print(f"Line {i} is NOT a valid CC number")
                time.sleep(0.5)
                continue
            if luhnsAlgorithm(line.strip()):
                print(f"Line {i} is a valid CC number")
                time.sleep(0.5)
            else:
                print(f"Line {i} is NOT a valid CC number")
                time.sleep(0.5)
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
