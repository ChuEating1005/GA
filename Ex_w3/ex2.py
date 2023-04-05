def squareSum():
    sum = 0
    str = input()
    a = str.split()
    for i in a:
        sum += int(i) * int(i)
    print(sum)

squareSum()
    