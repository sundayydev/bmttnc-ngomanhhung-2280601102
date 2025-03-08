#Câu 01: Viết một chương trình để tính tổng của tất cả các số chẵn trong một List.
def tinh_tong_so_chan (lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("Tống các số chẵn trong List: ", tong_chan)
