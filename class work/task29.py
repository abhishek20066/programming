import random
while True:
  computer = random.choice(["stone","paper","scissor"])
  user =input("enter stone,paper,scissor :")

  if computer == user:
    print("draw!!")

  elif  user == "stone"  and computer == "scissor":
    print("you win")

  elif user == "paper" and computer == "stone" :
    print ("you win")

  elif user =="scissor" and computer=="paper":
    print("you winnnn")    

  else:
    print("computer win")
    break
  


   






