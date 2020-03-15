def classify(number):
    if number <= 0: 
        raise ValueError("El número debe ser positivo")
    sums = sum(num for num in range(1, number) if number % num == 0) 
    if sums > number: 
        return "abundant"
    elif sums < number: 
        return "deficient"
    return "perfect"
