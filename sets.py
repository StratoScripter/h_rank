'''
You are given a set and other sets.
Your job is to find whether set is a strict superset of each of the

sets.

Print True, if
is a strict superset of each of the

sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set
is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set

.

Input Format

The first line contains the space separated elements of set
.
The second line contains integer , the number of other sets.
The next

lines contains the space separated elements of the other sets.

Constraints
'''

s = []
t = 'False'
A  = set(input().split())
N = int(input())
for i in range(N):
    B = set(input().split())
    x = A.issuperset(B)
    s.append(x)
if t in s:
    print('True')
else:
    print('False')