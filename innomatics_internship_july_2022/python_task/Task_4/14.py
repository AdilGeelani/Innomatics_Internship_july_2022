def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        unique = ''
        for c in string[i : i+k]:
            if (c not in unique):
                unique+=c
        print(unique)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)