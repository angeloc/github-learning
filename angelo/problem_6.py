#!/usr/bin/python

r = range(1, 101)
print (sum(r) ** 2 - sum(x ** 2 for x in r))
