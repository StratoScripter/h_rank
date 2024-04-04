'''You and Fredrick are good friends. Yesterday, Fredrick received

credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a
, or .
► It must contain exactly digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have

or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
'''

import re

pattern = r"(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$"
for i in range(int(input())):
    print('Valid' if re.match(pattern, input()) else 'Invalid')
    
'''
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:

regex_integer_in_range should match only integers range from 100000
to 999999

inclusive

regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string

is a valid postal code using the following expression:

(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

Input Format

Locked stub code in the editor reads a single string denoting
from stdin and uses provided expression and your regular expressions to validate if

is a valid postal code.

Output Format

You are not responsible for printing anything to stdout. Locked stub code in the editor does that.
'''

regex_integer_in_range = r"^[1-9]\d{3,5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


'''
Neo has a complex matrix script. The matrix script is a N X M

grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

[Capture.JPG]

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers
N(rows) and M(columns) respectively.
The next N lines contain the row elements of the matrix script.

Constraints
0 < N, M < 100
Note: A score will be awarded for using 'if' conditions in your code.
'''
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix = list(zip(*matrix))
sample = str()
for x in matrix:
    for char in x:
        sample += char
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ',sample))
    
