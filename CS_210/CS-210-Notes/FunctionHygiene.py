"""Pythonic function hygiene"""

#function headers and docstrings are the first thing in a function.

# hygenic function headers will follow python naming conventions: 
    #all lowercase letters unless a global variable
    #also, solely underscores for spaces. use speced where you would in a traditional word or title

#names matter - we choose names that are descriptive and meaningful, but also short. IE abs_diff for absolute difference

#names should be distinctive - avoid those that can be confused for one another like hours_weekend_worked and hours_weekday_worked

"""Arguements"""

#arguements are the variables that are passed into a function.

#arguements are also called formal parameters.

#a functions header along with a docstring is called a function signature - an agreement between the function and the user.

#Why do we care about this “contract”, if the code works? Because the contract determines what the author of the function is permitted to change without notice.

#it's much too easy to make a small change to some part of the function and not realize you may have just broken some other piece of code much down the line.

"""Information Hiding"""

#information hiding is the idea that we should hide the inner workings of a function from the user.

#we treat the body of the function as if it were a black box. we don't care how it works, we just care that it works.

#essentially, it can be invisible to the caller of the function.

### Students and beginning programmers often find information hiding unintuitive and bothersome.
### Understandably so, because as a beginner they write most code individually, and seldom work on the same project 
### for more than a few weeks. This is apt to change as you tackle larger and more complex projects.

#humans are generally poor at remembering large strings of numbers in perfect short-term working memory, so we can hide function details to save processing ability.

###Information hiding is an essential tool for controlling complexity by giving us permission to ignore most 
# details most of the time, focusing in on just a few at a time.

"""Docstrings"""

#docstrings are the first line of a function, and they are a string that describes what the function does. It's just a definition.

#python makes the docstring available to the user through the help function. if you're unclear how a function works, you can call help(function) for info. Pretty dope

"""Arguement names"""

#def relative_error(est: float, expected: float) -> float:
    #"""Relative error of estimate (est) as non-negative fraction of expected value."""

#the above is an example of a function header with arguement names. Arguement names, should they serve a certain purpose, should be more distinct than simply x and y.

# above we have two formal parameters, est and expected. est is the estimate, and expected is the expected value.

#these are mnemonic - they help us remember what the arguements are for. They sound like what they do.

#these parameters are NOT interchangable - and reversing them would provide incorrect results. This is why we use the names.

#it's pretty likely that we mess up the order of the arguements if they are vague like x and y, so we use the names to help us remember.

#names that are generic, like your v1, v2, or v3, are unhelpful - they don't tell us anything about what the arguements are for.


"""Results, Effects, and Side Effects"""

#a function normally does one of two things -
    # returns a result (well documented)
    # returns an effect on the arguements it was passed (well documented)
#however, it doesn't typically do both things. 

#For example, here is a function that returns a list containing just the positive elements from a list of integers:

def select_pos(m: list[int]) -> list[int]:
    """Returns a list of the positive elements from m."""
    result = []
    for el in m: 
        if el > 0:
            result.append(el)
    return result
    
li = [1, 0, 2, 0, 3, 0]
li_selection = select_pos(li)
print(f"li after selection is {li}")
print(f"selection is {li_selection}")

#the above function returns a result, but it doesn't change the original list. It's a pure function. 
# it also has no effect on anything outside of the function - what's called it's local scope. It's a pure function.

#here's an example of a function that changes one of it's arguements - IE it has an effect: 

def append_pos(src: list[int], dest: list[int]):
    """Positive elements of src are appended to dest."""
    for el in src: 
        if el > 0:
            dest.append(el)
    
li = [1, 0, 2, 0, 3, 0]
li_selection = []
append_pos(li, li_selection)
print(f"li after selection is {li}")
print(f"li_selection is {li_selection}")

#this is also fine. it has an effect on the list, but it doesn't return anything. It's a pure function.

# a function that does both things is called an impure function - it's just fucking confusing and stays messing stuff up. It's confusing. 

# try to stay away from a function that both returns a result and has an effect on it's arguements.

# For example, the built-in function sorted returns a sorted list without changing the list it is given, 
# while the list method sort puts the list into sorted order but does not return a result.

"""Side Effects"""

#if a function or method affects something other than it's arguements or the object on which a method is called, it's called a side effect. 

#side effects make it easy to create program bugs - and hard to find them to correct. One case where side effects may be justifiable is in output, 

#eg printing something, logging something to a file, or presenting a graphic. 

#the more obvious and well-documented such a side-effect ism the less chance it will lead to a super shiity debug session. 

"""Summary of Function guidelines for hygeinic functions"""

###Make the function header and docstring a contract between the author and user of the function. 
# The user should not depend on details of the body of the function, or even have to read the body of the function to know how to use it correctly.


###Use descriptive names for functions and their parameters. These names should not be too long but should be understandable in their contexts.

###Generic names like x are ok only for generic purposes like “some number”, never for something specific like “the number of sides of the polygon.”
# The names of your pets or siblings are only acceptable if the program computing something about your pets or siblings.

### A function (or method) should either return a result or have an effect.
# Very seldom should a function or method have both an effect and a result, and those rare cases must be carefully documented.

### Side effects are particularly dangerous. Avoid them when practical, and particularly avoid side effects that could go unnoticed, unless you love long and confusing debugging sessions.

### You may be tempted to ignore these guidelines because you will be the only user of the functions you write. The you of next week will be angry at the you of this week if you do.