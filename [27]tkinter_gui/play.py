def add(*args):
    summ = args[0]
    for i in args:
        if args.index(i) != 0:
            summ += i
    return summ

print(add(1,2,3,4,1))