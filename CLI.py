import sys

try:
    name_arg = (sys.argv[1]).lower()
    if name_arg == "quinn":
        print("Correct my name is Quinn!")
    else:
        print(f"You entered: {name_arg}")
        print("That is not my name, run the script in the command line to try again!")

except IndexError:
    print("No arguments provided, run the script in the command line with arguments to try again!")