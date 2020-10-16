Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 1
y = 1
z = 0
result = 0

while z < 4000000:
   z = (x+y)         
   if z%2 == 0:
       result = result + z

   #next iteration

   x = y
   y = z

print result