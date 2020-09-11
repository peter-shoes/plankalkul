import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

# DEFINE PROGRAM STRUCTURES HERE ======

class Program():
    def __init__(self,program):
        # set the program id
        # set the Randauszug string
        # set the lines of the program
        pass

class Randauszug(Program):
    def __init__(self, arg):
        self.name = arg[:arg.index('(')]
        param_string = arg[arg.index('(')+1:arg.index(')')]
        self.parameters = param_string.split(',')
        # this is clearly a bad way to do this
        returns_string = arg[arg.index('R0'):]
        returns_temp_list = returns_string.split(',')
        if ')' in returns_temp_list[-1]:
            returns_temp_list[-1] = returns_temp_list[-1][:-1]
        self.returns = returns_temp_list
        pass

# the basic structure goes like this:
# P0 R (V0[etc], V1[etc]) => R0[etc]
# do your stuff here
# END

# P is the program with assigned number, it starts the definition for a program
# R is like the name of the function itself, starts the arg/output definition
# inside the parentheses you have your input variables, always V
# the [etc] is like your variable definition stuff
# R0 is like your expected return, and you can have more than one
# the stuff in the middle is the process for your program
# you must give a resulting R0 or Rwhatever
# END is obviously the end of the program

class Expr(Program):
    pass

# DEFINE OPERATORS HERE ===============

class Multiply(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l*r

class Divide(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l/r

class Add(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l+r

class Subtract(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l-r

# DEFINE LOGIC HERE ===================

class Guard(Expr):
    def __init__(self,l,r):
        # defined as ->
        # l is always going to be bool
        # probably raise an error here otherwise
        # also probably raise an error for wrong types elsewhere
        self.l = l
        self.r = r
        if l:
            return r
        else:
            pass

class Conjunction(Expr):
    # defined as &
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return (l and r)

class Disconjunction(Expr):
    # defined as |
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return (l or r)

class Negation(Expr):
    # defined as !
    def __init__(self,var):
        self.var = var
        return (not var)

class Assign(Expr):
    # defined as =>
    def __init__(self,l,r):
        self.l = l
        self.r = r
        # get the binary value of l from the dictionary
        # set the binary value of r as that of l
        pass

class GreaterThan(Expr):
    # defined as >
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l>r

class LessThan(Expr):
    # defined as <
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l<r

class EqualTo(Expr):
    # defined as =
    # this works for any two structures of any type apparently
    def __init__(self,l,r):
        self.l = l
        self.r = r
        return l==r

# DEFINE VARIABLE TYPES HERE ==========

class Variablen(Expr):
    def __init__(self, var):
        self.var_whole = var
        self.structure = var[0]
        # V for input, read only
        # Z for temp values, read/write
        # R for output values, write only
        self.subindex = var[1:var.index('[')]
        self.component = var[var.index('[')+1:var.index(':')]
        # if component returns an empty string, this is taken to mean we are
        # referencing the whole variable, not a specific component
        self.type = var[var.index(':')+1:var.index(']')]
        pass

    def bin_setter(self,val):
        binval = bin(val)[2:]
        if len(binval) < int(self.type[:-2]):
            diff = int(self.type[:-2])-len(binval)
            binval = ('0'*diff) + binval
        self.binval = binval
        print(int(binval,2))
        pass
    # this is probably not going to work, it should be taking the binval initially
    # not the int val; this doesn't actualy work with the language the way i have it set up
    # dictionary entry would look like:
    # {structure+subindex : binval}

class Constanten(Expr):
    def __init__(self,val):
        self.val = val
        pass

# DEFINE CODE SPLITTER HERE ===========

def main():
    # operators = ['*','/','+','-','->','=>','&','|','!','<','>']
    # what should be happening here is we split by program and send each program
    # to the program class, which then sends all the jobs elsewhere
    x = Randauszug('R(V0[:8.0],V1[:8.0])=>(R0[:8.0],R1[:8.0])')




if __name__ == '__main__':
    main()

# because of the way variables work here, we're gonna have to use a dictionary
# we will store all the variables in full in the dictionary in binary
# to reference a specific bit we may need to convert to string???
# TODO: create while class with i0 variable
# TODO: create string splitter
# TODO: R auto outputs
