if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    li = set(arr)
    li.remove(max(li))
    print(max(li))
