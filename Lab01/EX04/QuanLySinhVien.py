from SinhVien import SinhVien 
class QuanLySinhVien:
    listSinhVien = []

    def themSinhVien(self, id, name, sex, major, diemTB):
        sv = SinhVien(id, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def xepLoaiHocLuc(self, sv):
        if sv.diemTB >= 8.0:
            sv.hocLuc = "Gioi"
        elif sv.diemTB >= 6.5:
            sv.hocLuc = "Kha"
        elif sv.diemTB >= 5.0:
            sv.hocLuc = "Trung binh"
        else:
            sv.hocLuc = "Yeu"

    def hienThiDanhSach(self):
        for sv in self.listSinhVien:
            print(f"ID: {sv.id}, Name: {sv.name}, Sex: {sv.sex}, Major: {sv.major}, DiemTB: {sv.diemTB}, HocLuc: {sv.hocLuc}")

    def sapXepTheoDiem(self, reverse=False):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse=reverse)

    def sapXepTheoTen(self):
        self.listSinhVien.sort(key=lambda x: x.name)

    def timKiemSinhVien(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.lower() in sv.name.lower()]

    def xoaSinhVien(self, id):
        self.listSinhVien = [sv for sv in self.listSinhVien if sv.id != id]

# Test chương trình
qlsv = QuanLySinhVien()
qlsv.themSinhVien(1, "Nguyen Van A", "Nam", "CNTT", 7.5)
qlsv.themSinhVien(2, "Tran Thi B", "Nu", "Kinh te", 8.2)
qlsv.themSinhVien(3, "Le Van C", "Nam", "CNTT", 5.8)

print("Danh sách sinh viên:")
qlsv.hienThiDanhSach()

print("\nSắp xếp theo điểm trung bình:")
qlsv.sapXepTheoDiem()
qlsv.hienThiDanhSach()

print("\nTìm kiếm sinh viên tên 'Nguyen':")
kq = qlsv.timKiemSinhVien("Nguyen")
for sv in kq:
    print(f"ID: {sv.id}, Name: {sv.name}, DiemTB: {sv.diemTB}")