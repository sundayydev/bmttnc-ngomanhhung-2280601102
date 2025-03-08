#Câu 04: Viết chương trình để truy cập các phần tử đầu tiên và cuối cùng trong một Tuple.
def truy_cap_phan_tu(tuple_data):
    frist_element = tuple_data[0]
    last_element = tuple_data[-1]
    return frist_element, last_element

input_tuple = eval(input("Nhập tuple, ví dụ (1, 2, 4): "))
frist, last = truy_cap_phan_tu(input_tuple)

print("Phần tử đầu tiên: ", frist)
print("Phần tử cuối cùng: ", last)