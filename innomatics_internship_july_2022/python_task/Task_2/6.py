if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = []
    for i in integer_list:
        t.append(i)
    t = tuple(t)
    print(hash(t))