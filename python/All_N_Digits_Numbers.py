def print_single_number(l):
    for digit in l:
        print digit,

def inc_number(l):
    index = len(l)-1
    while l[index] == 9 and index>=0:
        index -= 1
    if index<len(l)-1:
        l[index] += 1
        for ind in xrange(index+1,len(l)):
            l[ind] = 0
    else:
        l[index] += 1

def if_last_number(l):
    for digit in l:
        if digit!=9:
            return False
    return True

if __name__ == '__main__':
    n = 4
    l = []
    l.append(1)
    for i in xrange(1,n):
        l.append(0)
    print_single_number(l)
    print
    while not if_last_number(l):
        inc_number(l)
        print_single_number(l)
        print