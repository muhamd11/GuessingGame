secret_word = "bomba"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guessing = False

while guess != secret_word and not out_of_guessing :
    if guess_count < guess_limit:
     guess = input("enter your word : ")
     guess_count += 1
    else:
     out_of_guessing = True

if out_of_guessing:
    print("you lose")
else:
    print("you win")




