import sys
def ladder(n):
    cache = [1, 0, 0, 0, 0, 0]
    """ ladder(n) = ladder(n-1) + ladder(n-3) + ladder(n-5) """
    #print "ladder: ", minimumIndexOfCache, n, maximumIndexOfCache
    if (0 > n):
        return 0
    for i in range(1, n+1):
        cache[i%6] = cache[(i-1)%6] + cache[(i-3)%6] + cache[(i-5)%6]
    return cache[n%6]
def main(argv = None):
    if argv is None:
        argv = sys.argv
    print "step " + argv[1] + " is: " + str(ladder(int(argv[1])))
if __name__ == "__main__":
    main()