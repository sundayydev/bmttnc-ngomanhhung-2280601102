list = []

for x in range(2000, 3200) :
    if (x % 7 == 0) & (x % 5 != 0) :
        list.append(x)

print("Danh sách các số chia hết cho 7 ko chia hết cho 5: ", list)  