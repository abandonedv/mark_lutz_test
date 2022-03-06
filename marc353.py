with open('script1.txt') as fl, open('script2.txt') as f2:
    for pair in zip(fl, f2):
        print(pair)

with open('script1.txt') as fl, open('script2.txt') as f2:
    for (linenum, (linel, line2)) in enumerate(zip(fl, f2)):
        if linel != line2:
            print('%s\n%r\n%r' % (linenum, linel, line2))
