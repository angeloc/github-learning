#!/usr/bin/python


for i in range(1,100):
  if i%3==0 and i%5==0:
    print (i, ": fizzbuzz")
    continue
  if i%3==0:
    print (i, ": fizz")
  if i%5==0:
    print (i, ": buzz")
  


