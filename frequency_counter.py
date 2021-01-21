
def has_same_digit_frequency(list1, list2):
    frequency_dict = {
    } 
    
    for num in list1:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    print(frequency_dict)


list1 = [1, 2, 3, 4, 5, 6, 4, 4]
list2 = [4, 3, 2, 1]












