def print_formatted(number):
    results = []

    for i in range(1, number+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexa = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal, octal, hexa, binary])

    width = len(results[-1][3])  # largest binary number

    for i in results:
        print(*(s.rjust(width) for s in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)