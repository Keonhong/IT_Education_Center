from itertools import zip_longest

def compare(left, right):
    left_vars = map(int, left.split('.'))
    right_vars = map(int, right.split('.'))
    for a, b in zip_longest(left_vars, right_vars, fillvalue = 0):
        if a > b:
            return '>' #핵심포인트!
        elif a < b:
            return '<' #부등호에 리턴!!
    return '='

CASES = [['0.0.2', '0.0.1'],
         ['1.0.10', '1.0.3'],
         ['1.2.0', '1.1.99'],
         ['1.1', '1.0.1']]

if __name__ == '__main__':
    for case in CASES:
        print('{0[0]} {1} {0[1]}'.format(case, compare(*case)))

#zip_longest와 itertools의 자세한 사항 아래 링크참고할 것! and 이해할 때 까지 정리할 것!
# http://excelsior-cjh.tistory.com/entry/%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98-zip-%EA%B3%BC-itertoolsziplongest-%ED%95%A8%EC%88%98