from random import randint

first_name = input("What is your name?")
birth_year = input ("What year were you born?")
minimum = int(birth_year)
maximum = int (birth_year) + 70
random_year = randint(minimum, maximum)

print ("Hello " + first_name + ", your lucky year is " + str(random_year))
