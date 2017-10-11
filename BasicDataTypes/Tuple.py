if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

'''
튜블은 리스트와 유사하지만 수정이 불가능하다
처음 이자는 ,를 포함한다.
t = tupe('BinSin')
print t
('B', 'i', 'n', 'S', 'i', 'n')

hash는 어떤 종류던간에 값을 받아서 정수를 돌려주는 함수다.
키-값 쌍을 저장하고 조회하는데 사용한다.
튜플과 함께 사용하므로써 키를 수정 불가능하게 하면
키를 잃어버리지 않아 정상적으로 작동하게 된다.
'''
