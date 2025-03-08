#Câu 06: Viết chương trình để xóa một phần tử từ Dictionary theo key đã cho.

def xoa_phan_tu(dic, key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False

my_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4};
key_to_delete = 'b'
result = xoa_phan_tu(my_dic, key_to_delete)

if result:
    print("Phần tử đã được xóa từ Dictionary: ", my_dic)
else:
    print("Không tìm thấy phẩn từ xóa: ", my_dic)