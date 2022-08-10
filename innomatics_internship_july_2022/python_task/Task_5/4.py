# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
consonants = '[qwrtypsdfghjklzxcvbnm]'

a = re.findall('(?<=' + consonants +')([aeiou]{2,})' + consonants, input(), re.I)
print('\n'.join(a or ['-1']))
