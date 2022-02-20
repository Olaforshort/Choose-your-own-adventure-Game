#GAME BODY 
def game ():
  print("Here's your first choice.")

#INITIAL BRANCH 
  choice_1 = input("Left or Right? (left/right) ")
  if choice_1 == "left":
    response = input("Interesting, you've never seen this stray dog before. \nHe looks friendly. \nShould we pet him? (pet/run) ")





##INTRO and CONSENT BODY
print(
    "Welcome to my first choose your own adventure game! \nLet's get acquainted."
)

#NAME AND AGE INPUT
name = input("What's your name? ").capitalize()
while True:
  age = input("How old are you? ")
  try:
    age = int(age)
    break
  except ValueError:
    print("Numbers only please")

    

  
   



#NAME AND AGE OUTPUT
print("Hello", name, "you are", age, "years old.") 

#DECISION BODY FOR GAME CONSENT

if age >= 18: 
  print("you are old enough!")

  play_consent = input("Do you want to play? (yes/no) ").lower()
  if play_consent == "yes" :
    print("Let's play")
    game()
  else:
    print("Bye")
else:
  print("You aren't old enough to play :( ")
  
  adult_supervision = input("Is there an adult with you who can supervise? (yes/no) ").lower()

  if adult_supervision == "yes":
    print("Let's play!")
    game()
  else:
    print("Bye")


