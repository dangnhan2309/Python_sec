
from QuanLySinhVien import QuanLySinhVien

def main():
    qlsv = QuanLySinhVien()
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Sắp xếp danh sách sinh viên theo điểm trung bình")
        print("4. Sắp xếp danh sách sinh viên theo tên")
        print("5. Xóa sinh viên theo ID")
        print("6. Tìm kiếm sinh viên theo tên")
        print("7. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == "1":
            qlsv.addSinhVien()
        elif choice == "2":
            qlsv.showSinhVien()
        elif choice == "3":
            qlsv.sortByDiem()
            print("Đã sắp xếp theo điểm trung bình!")
        elif choice == "4":
            qlsv.sortByName()
            print("Đã sắp xếp theo tên!")
        elif choice == "5":
            id_sv = input("Nhập ID sinh viên cần xóa: ")
            if qlsv.deleteByID(id_sv):
                print("Đã xóa sinh viên thành công!")
            else:
                print("Không tìm thấy sinh viên có ID này!")
        elif choice == "6":
            keyword = input("Nhập tên sinh viên cần tìm: ")
            results = qlsv.findByName(keyword)
            if results:
                for sv in results:
                    print(sv)
            else:
                print("Không tìm thấy sinh viên nào!")
        elif choice == "7":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()
