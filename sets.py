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

a_set = set(input().split())
n = int(input())
sol = True
for _ in range(n):
    n_set = set(input().split())
    if not (a_set.issuperset(n_set)):
        sol = "False"
        break
print(sol)


'''If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.

Example

>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])


Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of

country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next lines contains the name of the country where the stamp is from. '''  

N = int(input())
a = set()
for i in range(N):
    a.add(input())
print(len(a))

'''
.remove(x)

This operation removes element x from the set.
If element x does not exist, it raises a KeyError.
The .remove(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0

.discard(x)

This operation also removes element x from the set.
If element x does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])

.pop()

This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

Example

>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set

Task

You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard. 
'''

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    entry = input().split()
    if entry[0] == 'pop':
        s.pop()
    elif entry[0] == 'discard':
        s.discard(int(entry[1]))
    elif entry[0] == 'remove':
        s.remove(int(entry[1]))
print(sum(s))

'''
.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Example

>>> s = set("Hacker")
>>> print s.union("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(set(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(['R', 'a', 'n', 'k'])
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>>> print s.union({"Rank":1})
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format

The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students. 
'''

a = int(input())
set_a = set(input().split())
b = int(input())
set_b = set(input().split())
print(len(set_a.union(set_b)))




'''
.intersection()

The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])

Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
'''
a = int(input())
set_a = set(input().split())
b = int(input())
set_b = set(input().split())
print(len(set_a.intersection(set_b)))