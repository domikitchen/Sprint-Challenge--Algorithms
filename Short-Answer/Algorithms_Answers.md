#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) will run depending on the value of n


b) O(n^2) nested loops dependant on a changing variable


c) O(n) will run recursively

## Exercise II

O(n log n)

n = list of stories
f = safe story

while len(n) > 1:
    mid = len(n) // 2
    
    if n[mid] == safe:
      n = [n[:mid:]]
    elif n[mid] > safe:
        n = n[:mid]
    elif n[mid] < safe:
        n = n[mid:]
