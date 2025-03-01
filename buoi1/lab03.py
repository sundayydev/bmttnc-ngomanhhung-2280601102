def kiem_tra_so_nguyen(): 
    gia_tri = input("Nhập một giá trị: ") 
    try:
        so_nguyen = int(gia_tri) 
        print(f"{gia_tri} là một số nguyên.") 
    except ValueError: 
        print(f"{gia_tri} không phải là số nguyên.") 

kiem_tra_so_nguyen()