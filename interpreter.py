import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

# DEFINE PROGRAM STRUCTURES HERE ======

class Program():
    def __init__(self,program):
        # set the program id
        # HOLD THE VARIBALES FOR THE PROGRAM
        # set the Randauszug string
        # set the lines of the program (list with result logic?)
        # you're probably gonna need a class for a line of the program
        # probably each line gets assigned
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

class Expr(Program):
    pass

# DEFINE OPERATORS HERE ===============

# find a way to have the symbol passed to Operators class and automatically pick the right one
# that's probably not done here because this is just for operator definitions

class MathOps(Expr):
    # these need to be stored in a third Z variable
    # V0 + V1 => Z0 handles like:
    # MathOps.add(V0, V1)
    # V0 + V1 + V2 => handles like:
    # MathOps.add(V0, MathOps.add(V1, V2))
    def __init__(self,l,r):
        self.l = l
        self.r = r
        pass

    def multiply():
        return(self.l*self.r)

    def divide():
        return(self.l/self.r)

    def add():
        return(self.l+self.r)

    def subtract():
        return(self.l-self.r)

    def guard():
        # defined as ->
        # l is always going to be bool
        # r is always going to be an operation, there must be a way to check this
        # probably raise an error here otherwise
        # also probably raise an error for wrong types elsewhere
        if l:
            return r
        else:
            pass

class BoolOps(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    # these ones assess two vars OR a bit from each var, which is treated as bool ==========
    # ex: V0[:8.0] | V1[:8.0]
    # ex: V0[0:8.0] & V1[1:8.0]
    # the best way to do this might literally be to compare strings

    def conjunction():
        # &
        return (l and r)

    def disconjunction():
        # |
        return (l or r)

    def negation():
        # you may have to place this one in a seperate class
        # !
        return (not r)

    def xor():
        # /~
        return ((not l and r) or (l and not r))

    # these ones produce bools from two variables ===========
    # this might be a problem if we go the string comparison route, because these return bools

    def greaterthan():
        # >
        return(l>r)

    def lessthan():
        # <
        return(l<r)

    def equalto():
        # =
        # this works for both variables and constants
        return(l==r)


# DEFINE LOGIC HERE ===================

class Assign(Expr):
    # defined as =>
    # takes a variable and assigns its binary value to the binary value of another Z or R variable
    # maybe this creates the Z variable on command? no previous dictionary store?
    def __init__(self,l,r):
        self.l = l
        self.r = r
        # get the binary value of l from the dictionary
        # set the binary value of r as that of l
        pass

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
    # what should be happening here is we split by program and send each program
    # to the program class, which then sends all the jobs elsewhere
    x = Randauszug('R(V0[:8.0],V1[:8.0])=>(R0[:8.0],R1[:8.0])')




if __name__ == '__main__':
    main()

# TODO: create while class with i0 variable
# TODO: create string splitter
# TODO: R auto outputs
