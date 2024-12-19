def find_min_max(arr):
    def divide_and_conquer(start, end):
        # Базовий випадок: якщо масив має один елемент
        if start == end:
            return arr[start], arr[start]
        
        # Базовий випадок: якщо масив має два елементи
        if end == start + 1:
            return (min(arr[start], arr[end]), max(arr[start], arr[end]))
        
        # Розділення масиву на дві частини
        mid = (start + end) // 2
        left_min, left_max = divide_and_conquer(start, mid)
        right_min, right_max = divide_and_conquer(mid + 1, end)
        
        # Об'єднання результатів
        overall_min = min(left_min, right_min)
        overall_max = max(left_max, right_max)
        return overall_min, overall_max
    
    # Перевірка на порожній масив
    if not arr:
        raise ValueError("Array must not be empty")
    
    return divide_and_conquer(0, len(arr) - 1)

# Приклад 
array = [3, 1, 9, 4, 7, -5, 8]
result = find_min_max(array)
print("Мінімум:", result[0])
print("Максимум:", result[1])
