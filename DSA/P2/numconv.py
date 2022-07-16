def calcNConv(a, x):
    try:
        if not type(a) or not type(x) is int:
            raise TypeError('Import must be an integer only!')
        elif a<0 or x<0:
            raise ValueError('Import must not be negative!')
        else:
            return _numConv(a, x)
    except Exception as err:
        print('ERROR:', err)

def _numConv(a, x):
    base = "" # store base output as string literal
    while a>0 and x <17: # logical check for correct inputttt
        b = int(a%x) # use variable to store remainder of modulo of function parameters
        if b<10: 
            base += str(b) #convert int value to string if less than 10, appending to base variable
        else:
            base += chr(ord('A')+b-10) # convert int value to char otherwise, using ord inbuilt
        a //= x
        base = base[::-1] # reverse string 
    return base

if __name__ == "__main__":
    print(calcNConv(44, 'aa'));
