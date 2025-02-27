from sympy.codegen.fnodes import dimension


def print_funtion(text):
    print(text)
def print_ten_tuoi():
    name = input("Type your name  : ")
    age = input("Type your age : ")
    print(f"Your name is {name}"
          f"\nYou are {age}")
def Dientichhinhtron():
    radius = int(input("Nhap ban kinh: "))
    if type(radius) =="str":
        print("Sai datatype")
    else :
        print(f"dien tinh hinh tron la :",int(radius**2))

def check_if_even() :
    num = 2
    if num %2 ==0 :
        return True
    else:
        return False


def check_7_5():
    a= []
    for i in range(2000,3200):
        if (i%7==0) and (i%5 !=0):
            a.append(i)
    return a
def print_7_5(a):
    n = len(a)-1
    print("Cac so chia het cho 7 va khong phai boi cua 5 : ")
    print(a)
def baitoan_tinhluong():
    hours = float(input("Nhap so gio lam : "))
    salary_per_hours = float(input("Nhap so tien luong moi hou: "))
    hours_atleast = 40.0
    extrahours = max(0,hours - hours_atleast)
    print("So tien luong la :",hours_atleast * salary_per_hours + extrahours*salary_per_hours*1.5)

def mang2chieu():
    input_str= input("Nhap x , y :  ")
    dimensions= [int(x) for x in input_str.split(',')]
    rowNum = dimensions[0]
    colNUm = dimensions[1]
    multilist = [[0 for colNum in range(colNUm)] for row in range(rowNum) ]
    for row in range(rowNum):
            for col in range(colNUm):
                multilist[row][col] = row*col
    print(multilist)
def print_uppercase():

    print("Nhap vao chuoi , done khi xong: ")
    lines=[]
    while True:
        line = input()
        if line.lower() =="done":
            break
        else:
            lines.append(line)
    print("Van ban da nhap la : \n ")
    for line in lines :
        print(line.upper())

def binary_string():
    print("Nhan '.' khi xong chuoi")
    lines=[]
    while True:
        line = input()
        if line==".":
            break
        else:
            lines.append(line)
    n = len(lines)
    dec= []
    for line in lines:
        if(int(line,2) % 5 == 0 ):
            dec.append(line)
    for i in dec :
        print(int(i,2))

def check_if_element_num(n):
    if n <=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n %1 == 0 :
            return False
    return True
def print_reusult_element():
    k=29
    print(f"So {k} la so : {check_if_element_num(k)}")
def doinguoichuoi():
    input_string = input("Nhap vao chuoi : ")
    print(input_string[::-1])
    #xem lai :  input_string[start:stop:step]
def main():

    # print_funtion("Dannglamthenhan")
    # print_ten_tuoi()
    # Dientichhinhtron()
    # print(check_if_even())
    # print_7_5(check_7_5())
    # baitoan_tinhluong()
    # mang2chieu()
    # print_uppercase()
    # binary_string()
    # print_reusult_element()
    doinguoichuoi()

if __name__ =="__main__":
    main()
