import collections
#initialize a deque

d= collections.deque()

#insert elements in a deque

for _ in range(int(input())):
  d.append(input())

#count the distinct elements
x=len(set(list(d)))
print(x)
#count elements

d_counter = collections.Counter(d)

for v,k in d_counter.items():
  print(k,end=" ")