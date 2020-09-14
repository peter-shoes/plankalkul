import re
import sys

file = open(str(sys.argv[1]), 'r')
lines = file.read().splitlines()

class Token():
    def __init__(type,text,literal,line):
        self.type = type
        self.text = text
        self.literal = literal
        self.line = line
        pass

def main():
    line_num = 0
    tokens = []
    # this is some beautiful fucking regex i tell you what
    var_regex = '[VZR]\d+\[(?:\d+\.+)*\d*\:(?:\d+\.+)*0\]'
    for line in lines:
        vars_in_line = re.findall(var_regex,line)
        
        # lex = Token(type,text,literal,line_num)
        # tokens.append(lex)
        line_num += 1

if __name__ == '__main__':
    main()
