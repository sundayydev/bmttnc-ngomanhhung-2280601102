from QuanLySinhVien import QuanLySinhVien


qlsv = QuanLySinhVien()
while (1 == 1):
    print("           CHƯƠNG TRÌNH QUẢN LY SINH VIÊN            ")
    print("***********************MENU**************************")
    print("**  1. Thêm sinh viên.                             **")
    print("**  2. Cập nhập sinh viên bởi ID.                  **")
    print("**  3. Xóa sinh viên bởi ID.                       **")
    print("**  4. Tìm kiếm sinh viên theo tên.                **")
    print("**  5. Sắp xếp sinh viên theo điểm trung bình.     **")
    print("**  6. Sắp xếp sinh viên theo tên chuyên ngành.    **")
    print("**  7. Hiện thị danh sách siên viên.               **")
    print("**  8. Thoát                                       **")
    print("*****************************************************")

    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhập thông tin sinh viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có id =", ID, " đã bị xóa.")
            else:
                print("\nSinh viên có id =", ID, " không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiện thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình")
        break
    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng có trong menu.")