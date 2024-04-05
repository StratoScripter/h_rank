'''
TASK
You are given a set A and N number of other sets. These number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
'''

n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    operation,  _ = input().split()
    new_element = set(map(int, input().split()))
    perform = f'A.{operation}({new_element})'
    eval(perform)
print(sum(A))