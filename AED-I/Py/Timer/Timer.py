import time

count = 0

while True:
    while count <= 1200:
        time.sleep(1)
        count += 1
        print(count, "WORK")
        
    while count <= 1500 and count > 1200:
        time.sleep(1)
        count += 1
        print(count, "RELAX")
    if count > 1500:
        count = 0
