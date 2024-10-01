def count_positive_numbers(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

numbers = [5, 4, -3, 2, 1]
positive_count = count_positive_numbers(numbers)
print("Количество положительных чисел:", positive_count)




