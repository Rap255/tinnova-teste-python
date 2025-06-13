input_number = int(input('Digite o número desejado: '))


def factorial(input_number:int):
    output_number = 1

    if input_number>=2:
        for i in range(1,input_number+1):
            output_number *= i
        return output_number
    
    if input_number == 0:
        return 1

print(factorial(input_number))