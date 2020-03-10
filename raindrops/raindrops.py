def convert(number):
    sound = ''
    if number % 3 is 0: sound += 'Pling'
    if number % 5 is 0: sound += 'Plang'
    if number % 7 is 0: sound += 'Plong'
    
    return str(number) if not sound else sound