import sys

def add(a,b):
    return a+b

def main(argv):
    if len(argv)>=2:
        print('Sum of two numbers:',add(int(argv[0]),int(argv[1])),'\n')
    else:
        print('Enter the required number:')

if __name__=='__main__':
    main(sys.argv[1:])
