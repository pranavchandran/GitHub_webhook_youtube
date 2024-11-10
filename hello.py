import sys

def call_func(*args):
    print(args)
    
if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    call_func(arg1, arg2)
