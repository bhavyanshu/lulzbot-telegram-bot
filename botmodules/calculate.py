#!/usr/bin/env python

import re,math

def calculate(expression):
    expression = re.sub('\s', '', expression)
    exp = re.split('[\+\-\*\/%\^]', expression)
    expression = re.sub('^' + exp[0], '', expression)
    if len(exp) == 1:
        l = 2
    else:
        l = len(exp) - 1
    for i in range(l):
        if expression.startswith('+'):
            expression = re.sub('^'+'\+'+str(exp[i+1]), '', expression)
            exp[i] = re.sub(r"\D", "", exp[i])
            exp[i+1] = re.sub(r"\D", "", exp[i+1])
            exp[i+1] = float(exp[i]) + float(exp[i+1])
        elif expression.startswith('-'):
            expression = re.sub('^'+'\-'+str(exp[i+1]), '', expression)
            exp[i] = re.sub(r"\D", "", exp[i])
            exp[i+1] = re.sub(r"\D", "", exp[i+1])
            exp[i+1] = float(exp[i]) - float(exp[i+1])
        elif expression.startswith('*'):
            expression = re.sub('^'+'\*'+str(exp[i+1]), '', expression)
            exp[i] = re.sub(r"\D", "", exp[i])
            exp[i+1] = re.sub(r"\D", "", exp[i+1])
            exp[i+1] = float(exp[i]) * float(exp[i+1])
        elif expression.startswith('/'):
            if exp[i+1] == '0':
                return 'Troll -_-'
            else:
                expression = re.sub('^'+'\/'+str(exp[i+1]), '', expression)
                exp[i] = re.sub(r"\D", "", exp[i])
                exp[i+1] = re.sub(r"\D", "", exp[i+1])
                exp[i+1] = float(exp[i]) / float(exp[i+1])
        elif expression.startswith('^'):
            expression = re.sub('^'+'\^'+str(exp[i+1]), '', expression)
            exp[i] = re.sub(r"\D", "", exp[i])
            exp[i+1] = re.sub(r"\D", "", exp[i+1])
            if int(exp[i+1]) <= 512:
                print re.sub(r"\D", "", exp[i+1])
                exp[i+1] = float(exp[i]) ** float(exp[i+1])
            else:
                return """Botserv: That's too long and hard....
                          lulzbot: That's what she said!"""
        elif expression.startswith('%'):
            exp[i] = re.sub(r"\D", "", exp[i])
            exp[i+1] = re.sub(r"\D", "", exp[i+1])
            exp[i+1] = float(exp[i]) % int(exp[i+1])
        elif expression.startswith('sqrt'):
            exp = re.sub('\\)', '', re.sub('sqrt\(', '', expression))
            return str(math.sqrt(float(exp)))
        else:
            return 'Wrong input'
    return exp[len(exp)-1]