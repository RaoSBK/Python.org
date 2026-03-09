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


print(f"My first motorcycle is {first_owned.title()} ")

print(motorcycles)


too_expensive = 'bugati'

print(f"{too_expensive.title()} is too expensive bike")


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
#would you invite? Make a list that includes at least three people you’d like to 
#invite to dinner. Then use your list to print a message to each person, inviting 
#them to dinner.


guests = ['swaraj', 'bamshi', 'sourabh']
invitation = "i am requestig you to come to the dinner at 9 O clock"
print(invitation, {guests[0].title()})
print(invitation, guests[1].title())
print(invitation, guests[-1].title())

for guest in guests:
    print(guest.title(), invitation )


# Q 3-5

# removed_guest = guests.pop(0)
# print(f"Guys {removed_guest} is  not comming ")
guests[0] = "suraj"
for guest in guests:
    print(guest.title(), invitation)


print("Q: 3-6")
guests.insert(0,'Shubham')

guests.insert(len(guest)//2, 'Biswas')

guests.append('Shiavm')

for guest in guests:
    print(guest.title(), invitation)


print("Q: 3-7")
print(guests)
print("Sorry guys the new table is not reached yet so only two peoples are invited")

removed_guests = guests.pop(0)
sorry_massage = ", I'm really sorry for that but for some issue I'm not going to invite you "
print(removed_guests.title(), invitation)


removed_guests = guests.pop(1)
print(removed_guests.title(), invitation)

removed_guests = guests.pop(2)
print(removed_guests.title(), invitation)

removed_guests = guests.pop(3)
print(removed_guests.title(), invitation)

removed_guests = guests.pop(4)
print(removed_guests.title(), invitation)


for guest in guests:
    print(guests.title(), invitation)

