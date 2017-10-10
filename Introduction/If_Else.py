if __name__ == '__main__' :
    '''
    n = int(input())
    if(n % 2 == 1) :
        print("Weird")
    elif(n>=2 and n<=5) :
        print("Not Weird")
    elif(n>=6 and n<=20) :
        print("Weird")
    else:
        print("Not Weird")
        '''
    import sys

    # strip() : 좌우 공백을 없앰
    n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}

    print(check[
                n%2 == 0 and (
                    n in range(2, 6) or
                    n > 20)
    ])
