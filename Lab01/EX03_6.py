def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

# Ví dụ sử dụng
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Nhập key cần xóa từ người dùng
key_to_delete = input("Nhập key cần xóa: ")

# Gọi hàm xóa phần tử
result = xoa_phan_tu(my_dict, key_to_delete)

# In kết quả
if result:
    print("Phần tử đã được xóa, Dictionary sau khi xóa:", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")
