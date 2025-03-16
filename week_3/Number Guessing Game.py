import random

secret_number=random.randint(1,10)
attempt=3

while attempt>0:
    guss=int(input("gesuss number between 1 to 10"))
    if guss==secret_number:
        print("ur guss is right")
        break
    elif guss<secret_number:
        print("too low")
    else:
        print("too high")
    attempt-=1

if attempt==0:
    print("sorry ans=",secret_number)