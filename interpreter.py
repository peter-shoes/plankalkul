import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

class Expr():
    pass

# DEFINE OPERATORS HERE ===============

class Mult(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r

class Plus(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r

# DEFINE LOGIC HERE ===================

class Guard(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r


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

class Constanten(Expr):
    def __init__(self,val):
        self.val = val

x = Variablen(lines[0])
# print(x.var_whole)
print(x.component)
