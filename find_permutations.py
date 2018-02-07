"""
Problem Description:
    Given two integers: N, K where N is a Natural number l = [1, N],
    arrange j = [1, N] in such lexographically smallest list that when abs(l(i) - j(i)) == K
    If it is not possible for all the elements in l then print 'Not Possible'

    e.g
    if N = 100 and K = 2
    then the output will be 
    [3 4 1 2 7 8 5 6 11 12 9 10 15 16 13 14 19 20 17 18 23 24 21 22 27 28 25 26 31 32 29 30 
    35 36 33 34 39 40 37 38 43 44 41 42 47 48 45 46 51 52 49 50 55 56 53 54 59 60 57 58 63 
    64 61 62 67 68 65 66 71 72 69 70 75 76 73 74 79 80 77 78 83 84 81 82 87 88 85 86 91 92 
    89 90 95 96 93 94 99 100 97 98]

    Explanation:
        N = 100 which is [1,2,3,4,5.....100]
        K = 2
        Lets say output is J
        when we subtract N(i) - J(i), result will be |2| and this should be true for all values in N, J
    The task is to find J
Arguments:
    Two Integers= N, K
How to run:
    python find_permutations.py 100 2
Result:
    List of number printed as string or Not possible
Tested On:
    100 2 
    2 1
    3 2
"""

def calculate(N, K):
    temp = []
    for v in range(1, N+1):
        m = v + K
        p = v - K
        if p > 0 and p <= N:
            if len(temp) > (p-K) -1 and (p-K) > 0:
                if temp[(p-K)-1] != p:
                    temp.append(p)
                else:
                    if m <= N:
                        temp.append(m)
            else:
                temp.append(p)
        else:
            if m <= N:
                temp.append(m)
    if len(temp) == N:
        print(' '.join(str(e) for e in temp))
    else:
        print('not possible')

def main(args):
    if len(args) < 2:
        print('Required 2 arguments')
    else:
        calculate(int(args[0]), int(args[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])