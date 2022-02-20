#GAME BODY 
def game ():
  print("Here's your first choice.")

#INITIAL BRANCH 
  choice_1 = input("Left or Right? (left/right) ")
  if choice_1 == "left":
    response = input("Interesting, you've never seen this stray dog before. \nHe looks friendly. \nShould we pet him? (pet/run) ")
    
    if response == "run":
      response == input("He chases you. There's a creepy abandoned building up ahead.\nShould we hide or keep going? (hide/go)")
  
  else:
    response = input("A thunderstorm approaches \nDo you go home to wait it out or keep going? (home/go)")

    if response == "home":
      response = input("You don't make it in time and are struck by lightning")
    else:
      response = input("You're sense of adventure keeps you forging ahead. \nYou find $100 in a rain gutter.") 





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
    print("Numbers (no decimals or fractions)only please")

    

  
   



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


