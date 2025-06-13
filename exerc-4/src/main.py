input_number =  int(input("DigiteDigite o número desejado: "))

def multiplos(input_number:int):

    list_number = []
    for number in range(1, input_number):
        if number % 3 == 0 or number % 5 == 0:
            list_number.append(number)
    return sum(list_number)

print(multiplos(input_number))