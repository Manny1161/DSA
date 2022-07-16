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
    if n==0:
        f=1
    else:
        f=n*_fact(n-1)   
    return f # return output depending on base cases
    
def calcNFib(n):
    try:
        if not type(n) is int:
            raise TypeError(str(n), 'Import must be an integer only!')
        elif n < 0:
            raise ValueError(str(n), 'Import must not be negative!')
        else:
            return _fib(n)
    except Exception as err:
        print('ERROR:', err)


def _fib(n):
    if n==0:
        f=0
    elif n == 1:
        f=1
    else:
        f=_fib(n-1)+_fib(n-2)
    return f

if __name__ == "__main__":
    i = 'a'
    print(calcNFib(i))
    #print(calcNFactorial(i))
   
