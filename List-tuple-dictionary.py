
from collections import Counter
def list_tongsochan(list):
    tong = 0 ;
    for i in list :
        if i %2 == 0 :
            tong +=i
    return tong
def take_input():
    input_list = input("Nhap vao chuoi cac so ex: 2,3,5,34 \n list : ")
    numbers = list(map(int, input_list.split(',')))
    return numbers
def reverse_list(list):
    return list[::-1]
def create_tuple(list):
    return tuple(list)
def getlist():
    list = [2,1,1,5,8,9,78,7]
    return list
def printFirstAndLastTupleElement(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    print(f"Phan tu : {first_element} and {last_element} ")

def count_element(list):
    dict_element = Counter(list)
    for items,countnum in dict_element.items():
        print(f"{items} : {countnum}")
def manual_frenquency_count(list):
    count_dict = {}
    for item in list :
        if item in count_dict: \
            count_dict[item] +=1
        else:
            count_dict[item] =1
    return  count_dict
def getDictionaryExample():
    dict = {
        'apple': {
            'color': 'red or green',
            'taste': 'sweet or tart',
            'season': 'fall',
        },
        'banana': {
            'color': 'yellow',
            'taste': 'sweet',
            'season': 'year-round',
        },
        'orange': {
            'color': 'orange',
            'taste': 'sweet and tangy',
            'season': 'winter',
        },
        'kiwi': {
            'color': 'brown (outside), green (inside)',
            'taste': 'sweet and tangy',
            'season': 'year-round',
        },
        'strawberry': {
            'color': 'red',
            'taste': 'sweet',
            'season': 'spring and summer',
        }
    }
    return dict
def remove_by_key(dict,key):
    if key in dict :
        del dict[key]
        print(f"Remove {key} successfully")
    else:
        raise KeyError(f"The key '{key}' does not exist in dict ")


def main():
     # print(list_tongsochan(take_input()))
    #print(reverse_list(take_input()))
    # print(create_tuple(getlist()))
    # printFirstAndLastTupleElement(getlist())
    # count_element(getlist())
     remove_by_key(getDictionaryExample(),'banana')

if __name__ =="__main__":
    main()