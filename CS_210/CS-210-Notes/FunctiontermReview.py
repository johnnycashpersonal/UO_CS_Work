
"""Scope, Namespace, Frame, Symbol Table"""

# A namespace may be called a symbol table or a frame. (frame is technically a structure in the python interpreter designed to implement a namespace)

#local scope - the namespace of the currently executing function.

#global scope - the namespace of the module in which the function is defined.

# outside of a function, the global scope and local scope may be - and often are - the same namespace.

#for noe, though (unless I build my own interpreter) they are basically the same.

"""Local VS Global variables"""

# A local variable is a variable in the namespace (scope) of a function, which is accessabile ONLY WHEN THAT FUNCTION IS EXECUTING. 

#A global variable is a variable in the global namespace, which is accessable from anywhere in the program.

"""Formal and Actual Arguements (parameters)"""

# okay, parameters and arguements are synonymous terms. Completely synonymous.

# When we use the term argument in the context of defining a function, we mean formal argument, that is, the name that will be used within the function body. 
# VERSUS
# When we use the term argument in the context of calling a function, we mean actual argument, that is, the value transmitted to the function.