import time
sec=int(input("Enter time in seconds:"))
while sec>0:
    print(sec)
    time.sleep(1)
    sec=sec-1 
print("Time over")
