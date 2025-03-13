def bai5():
    hours = float(input("Nhập số giờ làm việc: "))
    rate = float(input("Nhập lương trên giờ: "))
    salary = hours * rate
    print(f"Lương nhận được: {salary:.2f}")
# Chạy từng bài tập
if __name__ == "__main__":
    bai5()