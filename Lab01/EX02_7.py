def bai7():
    items = input("Nhập danh sách chuỗi, cách nhau bởi dấu phẩy: ").split(",")
    upper_items = [item.upper() for item in items]
    print(", ".join(upper_items))
# Chạy từng bài tập
if __name__ == "__main__":
    bai7()
        