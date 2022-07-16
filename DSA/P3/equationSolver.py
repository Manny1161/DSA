import numpy as np
from DSAStack import *
from DSAQueue import *

class infix:

    def __init__(self):
        self.output = np.empty(1, dtype=object)

    def solve(self, equation):
        self.parseinfixToPostfix(equation)
        #return _evaluatePostfix(_parseinfixToPostfix(equation))
        

    def parseinfixToPostfix(self, equation):
        postfix = ' '
        opstack = DSAStack()
        for i in equation:
            if self._evaluatePostfix(i):
                self.output = np.append(self.output, i)
            elif i == '(':
                opstack.push(exp)
            elif i == ')':
                while not opstack.top() != '(':
                    postfix = postfix + opstack.pop()
                opstack.pop()
            elif i == '+' or i == '-' or i == '*' or i == '/':
                while not opstack.isEmpty() and opstack.top != '(' and self._precedenceOf(opstack.top()) >= self._precedenceOf(i):
                    postfix = postfix + opstack.pop()

                opstack.push(i)
            else:
                postfix = postfix + i
        while not opstack.isEmpty():
            postfix = postfix + opstack.pop()
        return postfix

    def _evaluatePostfix(self, postfixQueue):
        return postfixQueue.isalpha()
    
    def _precedenceOf(self, val):
        if val == '+' or val == '-':
            return 1
        elif val == '*' or val == '/':
            return 2

    def _evaluatePostfix(self, postfixQueue):
        operandStack = DSAStack(postfixQueue.getCount())
        while not postfixQueue.isEmpty():
            x = postfixQueue.dequeue()
            if _precedenceOf(x) > 0:
                op2, op1 = (operandStack.pop(), operandStack.pop())
                operandStack.push(_executeOperation(x, op1, op2))
            else:
                operandStack.push(x)
        return operandStack.pop()

    def _executeOperation(self, op, op1, op2):
        if op1 == '+' or op2 == '+':
            return op1 + op2
        elif op1 == '-' or op2 == '-':
            return op1 - op2
        elif op1 == '*' or op2 == '*':
            return op1 * op2
        elif op1 == '/' or op2 == '/':
            return op1 / op2

if __name__ == "__main__":
    s = infix()
    print(s.parseinfixToPostfix('1 + 3'))
