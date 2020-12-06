import logging
import sys
# you're supposed to treat these as binary but for now int is fine

def add(l,r):
    return(l+r)

def subtract(l,r):
    return(l-r)

def multiply(l,r):
    return(l*r)

def divide(l,r):
    try:
        return(l/r)
    except ZeroDivisionError:
        if type(r) != bool:
            sys.exit('ERROR: Divide by zero')
        pass

def equal_to(l,r):
    return(l==r)

def greater_than(l,r):
    return(l>r)

def less_than(l,r):
    return(l<r)

def conjunction(l,r):
    return(l and r)

def disconjunction(l,r):
    return(l or r)

def xor(l,r):
    return((l and not r) or (r and not l))

def negation(l,r=None):
    return (not l)

def guard(l,r):
    # if l resolves to true, do r
    # currently, this will return None if not l
    if l:
        return r

def assign(l,r):
    # not exactly sure how to do this
    pass


# apparently you should wrap these function calls in a lambda in order to avoid calling on initialization
# so i can close the tab, lambda functions look like this:
# x = lambda a,b:a+b
# x(1,2)
def run_op(l,r,sym):
    ops_dict = {
    '+':add(l,r),
    '-':subtract(l,r),
    '*':multiply(l,r),
    '/':divide(l,r),
    '=':equal_to(l,r),
    '>':greater_than(l,r),
    '<':less_than(l,r),
    '&':conjunction(l,r),
    '|':disconjunction(l,r),
    '/~':xor(l,r),
    '!':negation(l,r),
    '->':guard(l,r),
    '=>':assign(l,r)
    }
    # if r is ever 0, even if you're not calling divide(), it will throw the error

    return(ops_dict[sym])

x = run_op(9,0,'->')
print(x)
