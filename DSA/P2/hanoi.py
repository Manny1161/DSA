def calcTowers(space, n, src, dest):
    try:
        if n<0:
            raise ValueError('Import must not be negative!')
        elif not type(n) or not type(src) or not type(dest):
            raise TypeError('Import must be an integer!')
        else:
            return _towers(space, n, src, dest)
    except Exception as err:
        print('ERROR:', err) 

def _towers(space, n, src, dest):
    if n==1:
        move(src, dest)
    else:
        tmp = 6 - src - dest
        _towers(space, n-1, src, tmp)
        move(src, dest)
        _towers(space, n-1, tmp, dest)
    
def move(src, dest):
    print('moving disk from', src, 'to', dest, src);

if __name__ == "__main__":
    calcTowers(' ',3,1,3);
