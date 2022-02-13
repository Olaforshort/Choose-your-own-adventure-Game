print(
    "Welcome to my first choose your own adventure game! \nLet's get acquainted."
)
name = input("What's your name? ")
age = int(input("How old are you?"))

print("Hello", name, "you are", age, "years old.") 

if age >= 18: 
  print("you are old enough!")

  play_consent = input("Do you want to play?")
  if play_consent.lower == "yes":
    print("Let's play")
  else:
    print("Bye")
else:
  print("You aren't old enough to play!")
