import time

start = time.time()
  
num = str(2 ** 1000)
sumNum = 0
 
for i in range(len(num)):
   sumNum += int(num[i])
  
print(int(sumNum))
elapsed = time.time() - start
 
print(elapsed, "seconds")   
