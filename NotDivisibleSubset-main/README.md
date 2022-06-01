# Problem Statement
Given a set of distinct integers(s), print the size of a maximal subset of  where the sum of any pair in it isn't evenly divisible by specified integer(k).

# Solution Description
I have created a function named  'nonDivisibleSubset' which requires the following parameter(s):
1. s : an array of integers
2. k : the divisor

and returns the length of the longest subset of s in which sum of any pair isn't multiple of the given divisor(k)
```python
def nonDivisibleSubset(k, s):
    count=[0 for i in range(k)]
    for i in s:
        count[i%k]+=1
    final=0
    if (k % 2 == 0):
        count[k//2] = min(count[k//2], 1)
    if count[0]!=0:
            final+=1
    f=1
    while f<=len(count)//2 :
        final+=max(count[f],count[k-f])
        f+=1
    return(final)
```

**Lets understand solution to this problem using one example**

s = [19, 10, 12, 10, 24, 25, 22] 

k = 4

Hence nonDivisibleSubset(k, s) will follow the following steps:
1. First it will create a remainder list of length k-1 
>The possible remainder when a dividend divided by divisor lies between the range 0 to divisor-1.
```python
# Array for storing frequency of modulo values
count=[0 for i in range(k)]
#This is known as list comprehension
#In the Considered example k = 4. Therefore
count=[0,0,0,0]
```

2. Then we loop through the given array (s) and update the remainder list(count) by incrementing the respective indexes where the remainder(formed after dividing every element of given array(s) with given divisor(k)) match the indexes of the remainder list(i.e.count).
```python
# Fill frequency array with values modulo K
for i in s:
    count[i%k]+=1
# In the taken example we have :             >2 elements which when divided by the divisor(k) gives remainder 0.           Therefore count[0]=2                     (i.e. the element at 0th index of list count will have the value 2)                                                                                        >3 elements which when divided by the edivisor(k) gives remainder 1.       Therefore count[1]=1                     (i.e. the element at 0th index of list count will have the value 1)                       >3 elements which when divided by the divisor(k) gives remainder 2.        Therefore count[2]=3                     (i.e. the element at 0th index of list count will have the value 3)                       >1 element which when divided by the divisor(k) gives remainder 3.          Therefore count[3]=3                     (i.e. the element at 3th index of list count will have the value 3)

# Therefore 
count=[2,1,3,1]

```
>When elements giving the same remainder after being divided by the given divisor are added their sum isn't evenly divisible by the given integer
3. Now we will loop through the updated remainder list starting from index 1.

We will make pair of elements at index i and index k-i.

Out of these two elements we will pickup the largest value,

i.e. the count of elements of array in which sum of any pair of the elements isn't evenly divisible by given integer.
we have to output the sum of these maximum values. 

So lets store it into a variable.
```python
final=0
```

Firstly, we have to add two conditional blocks as following:

1.For element at 0th index of the remainder list.
```python
#If we have more than one element giving remainder as 0 when divided by the divisor(k) we will only take 1 of it.                                    If there are none we cannot take any element
if count[0]!=0:
    final+=1
#In the considered example count[0]!=0.
# Therefore final=0+1=1

```


2.If k is even then for the element at the k//2(i.e.the centre element):
```python
# if K is even, then update f[K//2] to the value of min between count[k//2] and 1.       Basically we will take atmost 1 count if we have more than one element giving remainder as k//2.                                     If there are none we cannot take any element
if (k % 2 == 0):
        count[k//2] = min(count[k//2], 1)
# In the considered example k is even. Therefore count[2]=min(3,1)=1               
```
Now lets the run the code for general elements:
```python
f=1
while f<=len(count)//2 :
        final+=max(count[f],count[k-f])
        f+=1
```
Dry run:

length of count//2 = 2

therefore this loop will run until f<=2 

1. f=1

    final+=max(3,1)

    therefore final=1+3 =4

1. f=2
final += max(1,1)

    therefore 
    
    final=4+1 =5
>We take the element of largest value as we have to find the **MAXIMAL** subset

**OUTPUT**

5

Hence the maximal subset in which any pair of elements will never sum up to multiple of the given divisor(k).

>This solution is based on the Brute Force algorithm principle.[(Click to see the reference used) ](https://medium.com/@mrunankmistry52/non-divisible-subset-problem-comprehensive-explanation-c878a752f057)

