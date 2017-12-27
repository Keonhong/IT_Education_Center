total=0
index=1
while True:
    if index % 3 == 0 or index % 5 == 0:
        total=index+total
    if index >= 999:
        break
    index+=1
print(total)




total=0
for index in range(1,1000):
    if index % 3 == 0 or index % 5 == 0:
        total=index+total
print(total)
