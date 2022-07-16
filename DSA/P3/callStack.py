from DSAStack import *

c = DSAStack()

def display():
    print(c.stack[:c.count])

def calcNFactorial(n):
    try:
        if not type(n) is int:
            raise TypeError(str(n), 'Import must be an integer only!') 
        elif n < 0:
            raise ValueError(str(n), 'Import must not be negative!')
        else:
            return _fact(n)
    except Exception as err:
        print('ERROR:', err)

def _fact(n):
    c.push('1')
    display()     
    if n==0:
        f=1
    else:
        f=n*_fact(n-1)
        c.pop()   
    return f # return output depending on base cases

if __name__ == "__main__":
    print(calcNFactorial(5))

