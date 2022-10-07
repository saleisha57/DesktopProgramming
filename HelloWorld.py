print("Hello World!")
day = input("Enter a day: Mon, Tues, Wed, Thur, Fri, Sat, Sun \n")

print(day)

if day == "Mon" or day == "mon":
    print("NOOOOOOO \n")
if day == "Tues" or day == "tues":
    print("AHHHHHHH \n")
if day == "Wed" or day == "wed":
    print("k \n")
if day == "Thur" or day == "thur":
    print("fine \n")
if day == "Fri" or day == "fri":
    print("yay! \n")
if day == "Sat" or day == "sat":
    print("Woohoo \n")
if day == "Sun" or day == "sun":
    print("Tomorrow is Monday :( \n")


color = input("What is your favorite color?: blue, red, green, yellow, silver \n")
print("You chose " + color + "\n")

if color == "blue":
    variant = input("For the color choose variations with different starting letters: cyan, turquoise, sky \n")
if color == "red":
    variant = input("For the color choose variations with different starting letters: scarlet, pink, burgundy \n")
if color == "green":
    variant = input("For the color choose variations with different starting letters: forest, sea, grass \n")
if color == "yellow":
    variant = input("For the color choose variations with different starting letters: dandelion, gold, brass \n")
if color == "silver":
    variant = input("For the color choose variations with different starting letters: platinum, grey, mercury \n")

print("You chose " + variant + "\n")



# Interesting: num = input("Enter a number: \n") * 4


num = input("Enter a number: \n")
holder = int(num) * 4
print(holder)








































