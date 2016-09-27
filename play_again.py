
def play_again():
    answer = raw_input("Do you want to play again? ").upper()
    if answer == "Y":
        return True
    else:
        return False

print play_again()
