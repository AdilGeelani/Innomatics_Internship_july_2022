import re
n = int(input())
no_repeats = r"(?!.*(.).*\1)"
two_or_more_upper = r"(?=(?:.*[A-Z]){2,})"
three_or_more_digits = r"(?=(?:.*\d){3,})"
ten_alphanumerics = r"[\w]{10}"
filters = [no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics]

for i in range(n):
    uid = input()
    if all([re.match(f, uid) for f in filters]):
        print('Valid')  
    else:
        print('Invalid')