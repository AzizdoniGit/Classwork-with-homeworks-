import time

count = int(input(">> ")) + 1
i = 1
while i <= count:
    count -= 1
    time.sleep(1)
    print(f"{count}")
