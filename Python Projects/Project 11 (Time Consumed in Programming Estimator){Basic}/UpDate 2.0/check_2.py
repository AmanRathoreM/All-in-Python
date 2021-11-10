import time


print("Day =", time.strftime("%A"))
print("Date =", time.strftime("%d"))
print("Month =", time.strftime("%B"))
print("Year =", time.strftime("%Y"))
print("Time =", time.strftime("%H:%M:%S"))

print("Proper Date =", time.strftime("%d:%m:%Y"))
print("Unix Time =", time.time())
print("Epoch Time = ", str(time.gmtime(0)))


print("Time Zone = ", time.strftime("%z"))
print("Time Zone Name", time.strftime("%Z"))
