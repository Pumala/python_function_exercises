def play_again():
    while True:
        answer = raw_input("Do you want to play again? ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print "Invalid input."

print play_again()
