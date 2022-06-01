# Problem Statement
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
# Solution Description
I have created a function birthdayCakeCandles which requires the following parameter:
1. candles: list of the candle heights

and returns the number of candles that are tallest.

>In short we have to find the occurence of the largest number in the given array.

```python
def birthdayCakeCandles(candles):
    tallest_candle=max(candles)
    units=candles.count(tallest_candle)
    return units
```
Let's understand the this with an example.
```python
candles = [4, 4, 1, 3]
# The maximum height candles are 4 units high.                                    There are 2 of them, so our output should be 2.
```
To find the tallest candle in the array of candle heights(i.e largest element in the given array) we can use the following function: 
```python
max = 0
for i in candles:
    if i > max:
        max = i
```
But to make code shorter I've used an existing function of python (max) which functions the similarly.
```python
tallest_candle= max(candles) 
#tallest_candle=4
```
To count the occurence of the tallest candle(i.e the cout of the largest number of the array) we can use the following block of code:
```python
count = 0
for i in candles:
    if i == max:
        count += 1
```
But to make code shorter I've used an existing function of python (count) which functions the similarly.
```python
units = candles.count(tallest_candle)
#units=2
```
Hence our code return 2 which is the number of tallest candles to be blown.

>This problem can also be solved using a lambda function as follows:
```python
a=lambda arr:arr.count(max(arr))
print(a(candles))                             
```
