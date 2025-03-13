def bai6():
    X, Y = map(int, input("Nhập X, Y cách nhau bởi dấu phẩy: ").split(","))
    matrix = [[i * j for j in range(Y)] for i in range(X)]
    for row in matrix:
        print(row)
# Chạy từng bài tập
if __name__ == "__main__":
    bai6()