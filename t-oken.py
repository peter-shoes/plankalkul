import re
import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

class AddToken():
    def __init__(self,type):
        self.type = type
        # self.line_num = line_num
        # add the other handlers here
        pass

def match(expected):
    if line[pointer+1]==expected:
        pointer += 1
        return True
    else:
        return False

def main():
    tokens = []
    # this is some beautiful fucking regex i'll tell you what
    var_pattern = '[VZR]\d+\[(?:\d+\.+)*\d*\:(?:\d+\.+)*0\]'
    var_re = re.compile(var_pattern)

    ops_dict = {
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

    line_num = 0
    for line in lines:
        vars_in_line = var_re.findall(line)
        line_tokens = []
        pointer = 0
        while pointer <= len(line):
            if line[pointer] in ops_dict.keys():
                line_tokens.append(ops_dict[line[pointer]])
                pointer+=1
            elif line[pointer] == ('V' or 'Z' or 'R'):
                line_tokens.append(AddToken(vars_in_line[0]))
                pointer+=len(vars_in_line[0])
                vars_in_line.pop(0)
            else:
                print(line[pointer])
                pointer+=1
        line_num += 1
        tokens.append(line_tokens)
    print(tokens)

if __name__ == '__main__':
    main()
