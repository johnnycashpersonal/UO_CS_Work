# Collections and loops

#digging deeper into the basics of collections and loops 

# a collection type (or collection class) is a kind of data that can contain other data as elements. 
# for example, 

["alpha", "beta", "gamma"]

#is a list of strings, while 

[1, 2, 3] #is a list of integers

# in general, a collection type will have
    # a syntax for literals, ie a way to write down a value and indicate that we intend a collection of a certain kind
        # that means if we write [1, 2, 3], we intend a list of integers,
        # and if we write ["alpha", "beta", "gamma"], we intend a list of strings
        # but if we write (1, 2, 3), we intend a tuple of integers, and if we write {1, 2, 3}, we intend a set or dictionary of integers.

    #operations for building or extending values, 
        # for example if we have a list m = [1, 2, 3], 
        # we can extend it with m.append(4), 
        # which will add 4 to the end of the list.
        # we can also build a list from scratch with m = [] and then extend it with m.append(1), m.append(2), m.append(3), m.append(4)

list = []

user = "ian sidman"

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    list.append(i)
    
print(list, user) 

#operations for accessing elements, like
    # we can index a list (we kind of did it above anyways)
    # we can also iterate over a list with a for loop, like above
    # but anyways, we can index through a list with 
    # 
    # list[access number], 
    # 
    # keeping in mind python counts from 0, not 1.

#here are our basics:
    # lists
        # a lists's type, list, is a collection of values, called elements or items.
        # the elements can be any type, and they can all be different types. shockingly. Somehow.

        # a list is a mutable type, meaning that we can change its elements.

        #to write a list literal, we use string brackets, like this:

["a", "b", "c", 1, 2, 3, 4]

#or (lmao)

m = []

m.append("a")
m.append("b")
m.append("c")

#lmfao

#ellements of lists have indexes, or positions, starting with 0:

print(m[2])
print(m[0])
print(m[1])

#if we have two lists, we can double index:

m = [[1, 2], [3, 4]]

print(m[0][1])

#should give us 2

#determine how many things are in a list with len function:

len(m)

#we can also iterate over a list with a for loop:

for i in m:
    print(i)

#it's remarkably, remarkably easy.

#later we might use other approaches because we may need to know where semething is.

#for example something like

for s_index in range(len(m)):
    s = m[s_index]
    print(s_index, s)

#but we'll get to that later.
# 

#if we have a nested list, IE a list within a list, we will need nested loops, IE loops within loops. 
# 
# Here's an example:

m = [["a", "b"], ["c", "d"]]
for row in m:
    for s in row:
        print(s)

#this will print out a, b, c, d, each on a new line. The point is that we get each value inside each list.


# the order of access is called row-major order. We might wonder whether we can iterate trhough m in column-major order.

#column major order is doable, but less common, and much more complex:

for col_index in range(len(m[0])):
    for row_index in range(len(m)):
        print(row_index, col_index, m[row_index][col_index])

# this column-looping approach will only work if the matrix is rectangular, 
# IE if all the rows have the same length.

#if every row doesn't have the same length, we'll get an error.

"""Tuples"""

#the term tuple comes from generalizing sequences of some fixed size - IE doubles, triples, quintuples, etc.

#tupples are very similar to lists, but they are immutable. 

#we can create new tuples based on the contents of other tuples, but we cannot change the value or length of a tuple.

#to write a tuple literal, we use parentheses:

(1, 2, 3, 4)

("a", "b", "c", "d")

#tuples can be indexed like lists, but we usually do this by destructuring, aka assigning the elements of a tuple to variables:

character = ("Wesley", "Dread pirate Roberts", "As you wish")
name, alias, phrase = character
print(name)
print(alias)
print(phrase)

#this assigns a variable name to each element of the tuple, which we can then interact with. 

#it's infrequent and unrealistic, thought, to actually index through a tuple, even a nested tuple:

#we still want to deconstruct it. 

pdx = ("Portland International", (45.589,-122.596))
name, (lat, lon) = pdx #this line deconstructs the inside of the tuple we've just created - it's immutable, so we cannot change it, but we can assign variable values to specific elements.
print(name)
print(lat)
print(lon)

"""Dictionaries"""

#Dictionaries are a massively important part of writing code. 

#dictionaries are a collection of key-value pairs.

#their type is dict, and they are mutable.

#dictionaries represent associateions between a set of keys and a set of values. We can think of them as "Lookup tables" - we can look up a value by its key.

#for example:

state_dict = {"WA": "Washington", 
 "OR": "Oregon", 
 "CA": "California", 
 "AK": "Alaska"} #this is a dictionary literal. It can be on one line or many lines, but it's usually on one line. I'm just himmy.

#we can write a dict literal by using curly braces and associating each key to a value with :

#we can then "look up" an association by treatinf the key as an index. 

#THAT RIGHT THERE IS WHERE THE POWER OF DICTS COMES FROM.

oregon = state_dict["OR"] #we index into the dictionary with it's key, and it returns the value.

print(oregon)

#We can add a new (key, value) pair to a dictionary by assigning a value to a new key:

state_dict["NV"] = "Nevada"

print(state_dict) #----->fuckin neat.

#the values in a dictionary are unique - this means if we add a new value to an old key it will replace the old value, It won't list it twice.

#the values in a dict must be hashable.
    #the fuck is that?
        #in practice, it means we need to use immutable values as dictionary keys.
        #usually we use strings as dictionary keys, but we can also use int and tuple types.

        #lists, however, cannot be dictionary keys.

good_dict = { (1, "Alpha"): "A", (2, "Beta"): "B" }
print(good_dict[(2, "Beta")]) #this is weird, but works -- they're lists of tuples, so they're mutable.

# bad_dict = { [1, "Alpha"]: "A", [2, "Beta"]: "B" }
# print(bad_dict[[2, "Beta"]])

#this would give us a type error --- type "list" is unhashable.

# we can use the "in" operator to test whether a dict contains a key: 

if "TX" in state_dict:
    print(state_dict["TX"])

else:
    print("TX expansion not found")

#we can't directly iterate a dict, but we can obtain a list of key-value pairs with the keys method or 
# a list of (key,value) pairs (tuples) with the `items` method of type `dict`

for abbrev in state_dict.keys(): #.keys() will give us all the keys, .values() probably gives us all the values.
    print(abbrev)

#since the elements in the list returned by the (items) methodare tuples, it's common to destructure them 
#into seperate variables for each key and value:

for kv_pair in state_dict.items():
    abbrev, name = kv_pair #this is destructing a key value pair, which is usually in the form of a tuple.
    print(abbrev, name)

#however, fun fact - we can even destruct while in the for statement:

for abbrev, name in state_dict.items():
    print(abbrev, name) #this is the same as the above, but it's more concise -- just destructing the key-value pair right in the for statement.

#we can also use the `get` method to look up a key in a dictionary, but it will return None if the key is not found.

"""Loops and Comprehensions"""

###Counting

#It's a very common counting task to want to count elements within a collection - dictionary, list, tuple, or whatever.

#for example, suppose we wanted to determine how many elements in a list of strings are state abbreviations.

#if all we want is the count of the collections size, we can just use `len`:

print(len(state_dict))

#but if we want to count the number of elements that satisfy some condition, we can use a loop:

abbrevs = ["WA", "OR", "CA", "NV", "AK", "MT", "ID", "UT", "AZ", "HI"]

count = 0

for abbrev in abbrevs:
    if len(abbrev) == 2:
        #count = count +1 #one easier way is to do count += 1
        count += 1

print(count)


#this is a SUPER common pattern - we initialize the count prior to the loop. 

# add to it within the loop, and then do something (print) after the loop is run.

###COUNTING MULTIPLE VALUES

#so we are pretty good at counting one thing, but we can also count multiple, even without knowing what or when they might occur:

#if we don;t know what values we will encounter, we can create an empty dict to store the counts:

animals = ["cat", "dog", "cat", "bird", "dog", "cat", "dog", "dog", "fish", "cat", "dog"]

counts = {}

for animal in animals: #for each value in the list of animals
    if animal in counts: #if the animal is already in the counts dict:
        counts[animal] += 1 #add one to the count of the animal
    else: #if this is the first time we see the animal:
        counts[animal] = 1 #set the count of that specifica animal to one

print(counts) #this works because it prints out a dictionary - the key is the animal, the count is how many times it was called. 

"""Summing"""

#we also have common patterns to sum values or datasets.

#to count items, we always just add one if the item satisfies some condition, but 

#to sum values, we add the value of the item if it satisfies some condition.

#here's an example with some towns and their populations in a dictionary

populations = {
    "Portland":   641_162,
    "Salem":      177_723,
    "Eugene":	  175_096,
    "Gresham":	  113_103,
    "Hillsboro":  106_633,
    "Bend":       102_059,
    "Beaverton":   98_216,
    "Medford":	   86_367,
    "Springfield": 62_256,
    "Corvallis":   59_864,
    "Albany":	   56_828,
    "Tigard":	   55_767,
    "Aloha":	   53_724
}

we_gaf_about = ["Eugene", "Corvallis", "Albany", "Salem", "Hillsboro"]

pop_sum = 0 #init w 0 again

for town in we_gaf_about:
    pop_sum += populations[town] #this means "look through the dictionary, find the key (in this case town), and add the associated sum to the pop_sum variable."
print(pop_sum)

#we can also use the `sum` function to sum a list of values:

print(sum([1, 2, 3, 4, 5])) #this is the same as the above, but it's a lot more concise.


#for both counting and summing, it's "idiomatic",meaning it's a common pattern, to use a comprehension to do the work in a single expression:

print(sum([populations[town] for town in we_gaf_about])) #this is the same as the above, but it's a lot more concise.

#if we do want to go the for loop route, we should use the += operator to add the sum to the variable, rather than the + operator.

"""Scanning"""

#another common task in loops is to determine if some or all elements of a collection satisfy some condition. For example, 
#if we wanted to determine if all the towns in an itinerary were included in a table, we might write:

all_present = True

for town in state_dict: 
    if town not in we_gaf_about: 
        all_present = False
        break

print(all_present)

#the code above is an easy way to determine if all the elements in something satisfy another condition.


#here's the pattern: 
    #Initially, we assume the condition is true (all_present = True)

    #if we find an element that does not satisfy the condition, 
    # we set the condition to false (all_present = False)
    # after that, we don't need to check any more elements, so we break out of the loop.

    #after the loop body, we display the final answer, which is now known.

#If we write a for all scan as a function, the logic is similar, 
# but we don't need an explicit `boolean` variable:

def all_in_table(li: list, table: dict) -> bool:
    """Return True if all elements of li are keys in table."""
    for elem in li: 
        if elem not in table:
            return False
    return True

print(all_in_table(we_gaf_about, populations)) #this checks that every element in list we gaf about is also in the populations dictionary.

#in this version of the `for all` scan, we return False as soon as we find an element that does not satisfy the condition.

#in terms of mathematical logic, we call this a "there exists" scan, because we are looking for an element that does not satisfy the condition.

#there exists scans are the opposite of like an all exists -- a for all:

# we can scan to see if any elements of a collection satisfy some condition. For example,

reach_big_city = False #we init the case as false

for town in we_gaf_about: 
    if town in populations: #this says (if any of these towns are in the populations dictionary)
        reach_big_city = True #print true and give it a true value
        break #now we can break out, we good. 

print(reach_big_city)

#In there exists scans, we can break from the loop as soon as we find an element that satisfies the criteria.

#we can formalize this pattern as a function as well much like for_all:

def exists_in_table(li: list, table: dict) -> bool: 

    """True if any elements of li are keys in table""" #always throw that docstring in there
    for elem in li: 
        if elem in table: 
            return True
    return False
   
print(exists_in_table(we_gaf_about, populations))

# we just replace assigned boolean values with return staments in the appropriate places and we're good.

"""Other Iteratables"""

# we can also loop through the charachters in a string:

s = "What the fuck are you talking about bruh? lol"

for char in s:
    print(char)

#in python, "things you can loop through" are called iterables.

#when we loop through indexes for a list 1 using range(len(1)), 

#we actually are iterating through elements of a range object:

for e in range(3):
    print(e)

#that means for e "each number" in a range of the first three numbers python counts from, print it.

# it will return 0, 1, 2 
# not 1, 2, 3