while True:
    try:
        n = int(input())
        sum = 0
        for i in range (1,n+1):
            if i%3==0:
                sum += i
        print(sum)
    except:
        break