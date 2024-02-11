name = input("Write your name: ")
sur = input("Write your surname: ")
age = input("Write your age: ")
import sys
#from pprint import pprint

if age.isdigit():
   pass
   #print(f"oh, me too {age} years")
else:
    print("Write your age as number please")
    sys.exit()
if age> "18":
     print("access is allowed")
else:
    print("access is denied")
    sys.exit()

print(f"""Your name  {name} {sur} 
Your age: {age}""")


