import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

# DEFINE PROGRAM STRUCTURES HERE ======

class Program():
    pass

class Randauszug(Program):
    def __init__(self, v_args, r_args):
        self.v_args = v_args.split(',')
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
        # if component returns an empty string, this is taken to mean we are //
        # referencing the whole variable, not a specific component
        self.type = var[var.index(':')+1:var.index(']')]
    def bin_setter(self,val):
        binval = bin(val)
        if len(binval)-2 < int(self.type[:-2]):
            diff = int(self.type[:-2])-len(binval)+2
            binval = binval[:2] + ('0'*diff) + binval[2:]
        self.binval = binval
        print(binval)
        pass
    # new function that gets the type and converts it into a real number as well as a binary
    # creating binval would look like:
    # binval = bin(NUMBER)
    # if len(binval)-2 < self.type[2:]:
        # get the difference between what it is and what it should be
        # insert that many 0's at index 2
        # binval = that new thing
    # dictionary entry would look like:
    # {structure+subindex : binval}

class Constanten(Expr):
    def __init__(self,val):
        self.val = val
        pass

# DEFINE CODE SPLITTER HERE ===========

def main():
    # operators = ['*','/','+','-','->','=>','&','|','!','<','>']
    # variables_in_program = {}
    # linevars = []
    # working = lines[0]
    # # while 'V' in working:
    # if 'V' in working:
    #     linevars.append(working[working.index('V'):working.index(']')+1])
    #     working = working.replace(working[working.index('V'):working.index(']')+1],'')
    # print(working)
    # print(linevars)
    x = Variablen('V0[:8.0]')
    x.bin_setter(5)




if __name__ == '__main__':
    main()

# because of the way variables work here, we're gonna have to use a dictionary
# we will store all the variables in full in the dictionary in binary
# to reference a specific bit we may need to convert to string???
# TODO: create while class with i0 variable
# TODO: create string splitter
# TODO: R auto outputs
