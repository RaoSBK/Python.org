bycycles = [ 'terk', 'cannondale', 'redline', 'specilized']
print(bycycles)
print(bycycles[0])
print(bycycles[0].title())
print(bycycles[-1])     # helps us to print the last element from the list 

massage = f"this is my first bycycle {bycycles[0].title()}"
print(massage)


# practice question3-1 3-1. Names: Store the names of a few of your friends in a list called names. Print 
    # each person’s name by accessing each element in the list, one at a time.

names = ['gulshan', 'onam', 'rahul', 'abhishek']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-1].title())


#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
    #printing each person’s name, print a message to them. The text of each mes
    #sage should be the same, but each message should be personalized with the 
    #person’s name.

names = ['gulshan', 'onam', 'rahul', 'abhishek']
greeting = "Good Morning"
print(greeting, names[0].title())
print(greeting,names[1].title())
print(greeting,names[2].title())
print(greeting,names[-1].title())


motorcycles = ['hunda', 'suzuki', 'yamha']
print(motorcycles)

motorcycles[0] = 'royal Enfield'
print(motorcycles)

motorcycles.append('hunda')
print(motorcycles)


motorcycles.insert(0, 'GT')
print (motorcycles)

del motorcycles[0]
print(motorcycles)


del motorcycles[3]
print(motorcycles)


pooped_motorcycles = motorcycles.pop()
print(pooped_motorcycles)

first_owned = motorcycles.pop(0)
print(f"I owned my first bike which is {first_owned.title()}")


