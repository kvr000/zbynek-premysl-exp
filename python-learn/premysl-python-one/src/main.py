
aliens = 2
password = "ALIENS"
print("Quickly! Aliens are invading the planet.")
print("You need to activate the global defense platforms.")
print("Hope you know the password, for Earth's sake...")
print()
print("--------------------------------------------------")
print("       WELCOME TO THE GLOBAL DEFENCE NETWORK      ")
print("--------------------------------------------------")
print()
print("Hint: The password is one word")
print()
guess = input ("Please enter the password: ").upper()
while guess != password:
    print()
    print("INCORRECT PASSWORD")
    print()
    aliens = aliens ** 2
    print("There are", aliens, "aliens now on Earth. Try again!")
    if aliens > 7400000000:
        break
    print()
    print(" Hint: the things that are attacking us.")
    print()
    guess = input("Quick! Please enter the password: ").upper()
if aliens > 7400000000:
    print("Noooooo! The aliens have outnumbered us. All is lost.")
else:
    print("Hooray! We won the fight and the world is saved!")






















