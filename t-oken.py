import re
import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

class Operators():
    def __init__(self):
        self.ops = {
            '(':AddToken('OPEN_PARENTHESES'),
            ')':AddToken('CLOSE_PARENTHESES'),
            ',':AddToken('COMMA'),
            '+':AddToken('ADD'),
            '-':AddToken('GUARD' if match('>') else 'SUBTRACT'),
            '*':AddToken('MULTIPLY'),
            '/':AddToken('XOR' if match('~') else 'DIVIDE'),
            '&':AddToken('CONJUNCTION'),
            '|':AddToken('DISCONJUNCTION'),
            '!':AddToken('NEGATION'),
            '>':AddToken('GREATER_THAN'),
            '<':AddToken('LESS_THAN'),
            '=':AddToken('ASSIGNMENT' if match('>') else 'EQUAL_TO'),
        }



def match(expected):
    if line[pointer+1]==expected:
        pointer += 1
        return True
    else:
        return False

# this is some beautiful fucking regex i'll tell you what
var_pattern = '[VZRi]\d+\[(?:\d+\.+)*\d*\:(?:\d+\.+)*0\]'
var_re = re.compile(var_pattern)
single_tokens = ['(',')',',','+','*','&','|','!','>','<']


tokens = []
line_num = 0
for line in lines:
    vars_inline = re.findall(var_re,line)
    line_tokens = []
    pointer = 0
    while pointer < len(line)-1:
        char = line[pointer]
        if char in single_tokens:
            line_tokens.append(char)
            pointer +=1
        elif re.match('[-=]',char):
            if re.match('>',line[pointer+1]):
                full_token = char+'>'
                line_tokens.append(full_token)
                pointer +=2
            else:
                line_tokens.append(char)
                pointer +=1
        elif re.match()
        elif re.match('[VZRi]',char):
            # here we need to check if it matches a variable in the line
            # if yes, append to tokens
            # if no, throw error
            pass
        elif re.match('P',char):
            if
        else:
            pointer +=1

    print(line_tokens)
    tokens.append(line_tokens)
    line_num+=1
