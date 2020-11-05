import os
#os.system("filename") 

print("What would you like to do with the mcatlm database today?")

thing_to_do = input()


if(thing_to_do == "mcatlm -add"):
  os.system("add.py")


elif(thing_to_do == "mcatlm -edit"):
    print(2)
elif (thing_to_do == "mcatlm -del"):
    print(3)
elif (thing_to_do == "mcatlm -search"):
    print(4) 

