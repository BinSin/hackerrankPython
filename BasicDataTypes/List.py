if __name__ == '__main__':
    '''
    n = int(input())
    # arr = list()
    arr =[]
    for _ in range(n) :
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print" :
            cmd += "(" + ",".join(args) +")"
            # eval은 문자열을 입력받아 문자열을 실행한 결과값을 리턴
            eval("l."+cmd)
        else :
            print(arr)
    '''
    l = []
    for _ in range(int(input())) :
        s = input().split()
        # operation 있는지 검사
        if hasattr(l, s[0]) :
            # 1: 에서 :는 1다음 모든 수 의미
            # operation을 가져와 실행한다.
            getattr(l, s[0]) (*map(int, s[1:]))
        else :
            print(l)

'''
l = [] or l = []
insert i e : i 위치에 e 삽입
print : print
remove e : 처음 발생한 e 삭제
append e : 뒤에 e 추가
sort : 정렬
pop : 뒤에 것 팝
reverse : reverse
'''
