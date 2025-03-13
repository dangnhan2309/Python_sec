def bai8():
    binaries = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ").split(",")
    divisible_by_5 = [b for b in binaries if int(b, 2) % 5 == 0]
    print(", ".join(divisible_by_5))
# Chạy từng bài tập
if __name__ == "__main__":
    bai8()