

#  zadanie 1

#  zaimplementuj algorytm insertion sort

def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        current_element = numbers[index]
        j = index - 1
        while j >= 0 and current_element < numbers[j]:
            print(numbers)
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = current_element
    return numbers
