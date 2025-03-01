def chia_het_cho_5(so_nhi_phan) :
    so_thap_phan = int(so_nhi_phan, 2)
    
    if so_thap_phan % 5 == 0 :
        return True
    return False

so_nhi_phan = input("Nhập số nhị phân: ");
if chia_het_cho_5(so_nhi_phan) :
    print(f"{so_nhi_phan} chia hết cho 5")
else :
    print(f"{so_nhi_phan} không chia hết cho 5")