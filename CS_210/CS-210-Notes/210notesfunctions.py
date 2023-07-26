# on functions

# Functions are a way to group code together and give it a name.  This allows you to reuse code and make your code more readable.

# The global namespace (or scope) of your program is distinct from the namespace of modules you import. 
# When you import random, the name “random” refers to the whole module, 
# and is distinct from any names that occur within that module, like random.randint.

#the thing before a . is the namespace of your program and thus refers to the module.
#the thing after a . is the namespace of the module and thus refers to the function. 

#module.function() is the notation. 


### MAJOR TERM REVIEW

# NAMESPACE - may also be called a symbol table or frame.

# frame is a structure inside py interpreter to implement a namespace but are so close together they can be treated like synonyms. 

# scope and namespace are very similar, except that local scope refers to the namespace of the currently executing function.

# The technical distinctions may matter to you someday if you build your own programming language interpreter.
# For now you can treat namespace, scope, and frame as synonyms.

### LOCAL VS GLOBAL VARIABLES

# A local variable is a variable in the namespace (scope) of a function, whereas a global variable is in the global namespace (scope) of your program.
# global variable are accessable from within a function and outside of it.

#parameters and arguments are the exact same thing. It's what you pass into a function. disappointing. 
# we're going to try and stay consistent and use " arguement" as often as possible. 

#to find useful modules, we could probably just google it. I also saved a copy of the link of standard py import modules.

#let's write a basic function to find absolute difference between two numbers.

x = int(input("X: "))
y = int(input("Y: "))


def abs_difference(x: int, y: int): #two arguments, x and y, that both must be integers. This just alerts us that we must legally assign non-fp numbers here.
    """Returns the absolute difference between two numbers"""
    
    if x > y:
        return x - y
    else:
        return y - x 
    
print(abs_difference(x, y))

#scope

#we saw that when we call a function, the values we "pass" to the function are assigned to the formal arguements. which may have different names than the actual arguements.
    
# in terms of scope: Apparently, once you define a function, you can call it with different variable names if they are type-matching. 

# for example a function with two arguements a and b will work for variables x, y in the format

# function(x, y). However, a and b aren't defined anymore, so they won't get recognized if we try and call a now while meaning x. 

# the value of x has been assigned to formal arguement a. 

# the value of y has been assigned to formal arguement b. 

"""If you assign to a variable within a function, 
that variable will likewise exist only as long as the function is executing."""

#here's a good example:

# Global scope (global frame or namespace)
x = 23
y = 42
m = 19

def example(m: int): #example is our function here. Wahoowa. 
    """Example to illustrate scope"""
    y = 77
    print(f"x is bound to {x} within example")
    print(f"y is bound to {y} within example")
    print(f"m is bound to {m} within example")

# Executing "example" creates the new local scope
example(x)
# When "example" finishes, the new scope is deleted

print(f"After example, x is bound to {x}")
print(f"After example, y is bound to {y}")
print(f"After example, m is bound to {m}")

#when this print, it will print the global x and y, not the local x and y. thus we will see that y changes inside and outside of the function space.

# We say that the “actual argument” x is bound to the “formal argument” m in example(m: int). 
# This is always how values are passed to functions in Python.

#when you bind one value to more than one name, that's called aliasing - it will become important when we bwgin to consider objects like lists that can be modified. 

#GLOBAL VARIABLES

#so, when we write code, we never ever want to change a global varibale inside of a function. It's unhygenic and confusing.

def bad_bad_bad(x: int):
    """Don't do this!"""
    s.append(x)   # s is not local to bad_bad_bad. s is a global cvariable from outside of function bad bad bad. 
    
s = [1, 2]
bad_bad_bad(3)    # Not obvious that we are changing s! 
print(s)

#python convention is to use all uppercase letters for a global variable.

#if the global variable is a fixed cosnatnt or configuration, it's okay to use it inside of a function. We may have to do this in the future.

DICT = "shortdict.txt"    # Short version for testing & debugging
# DICT = "dict.txt"       # Full dictionary word list

# ... other code ... 

def find(anagram: str):
    """Print words in DICT that match anagram.
    ... test cases here ... 
    """
    dict_file = open(DICT, "r") 
    #  Reference to DICT is better than burying
    #  the configuration setting here in the function.
    for line in dict_file:
          word = line.strip()
          if word == anagram:
              print(word)

#we can also use global variables to count the number of times a function is called.

"""Very rarely we might need to update a global variable from within a function. 
This is quite unusual, and never something to be done without first considering alternatives."""

#for example if we needed to keep track of the number of times a function is called, we could do this.

count_foo = 0

def foo() -> int: 
    
    """This will work.  That doesn't make it a good idea."""
    global count_foo #we can use the global keyword to access the global variable and specifically note that this is a global variable as well as change it.
    count_foo = count_foo + 1
    return count_foo
  
print(foo())
print(foo())
print(foo())

#okay. keep in myinf there are many things to focus on in function hygiene, and this is just a small example - the next section will focus more on fucntion hygiene. 

