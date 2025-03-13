def bai4():
    numbers = [x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
    print(", ".join(map(str, numbers)))
# Chạy từng bài tập
if __name__ == "__main__":
    bai4()