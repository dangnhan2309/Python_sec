import re

def sum_numbers_from_string(s):
    numbers = re.findall(r'-?\d+', s)  # Tìm tất cả các số nguyên, bao gồm cả số âm
    positive_sum = sum(int(num) for num in numbers if int(num) > 0)
    negative_sum = sum(int(num) for num in numbers if int(num) < 0)
    return positive_sum, negative_sum

input_str = "-100#^sdfkj8902w3ir021@swf-20"
pos_sum, neg_sum = sum_numbers_from_string(input_str)

print(f"Giá trị dương: {pos_sum}. Giá trị âm: {neg_sum}.")
