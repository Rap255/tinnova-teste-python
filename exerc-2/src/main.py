input_vetor = [5,3,2,4,7,1,0,6]
print("Input Inicio: ", input_vetor)


def bubble_sort(list_input:list = input_vetor):

    for n,item in enumerate(list_input):
        if n == len(list_input)-1:
            return list_input
        if list_input[n]> list_input[n+1]:
            list_input[n], list_input[n+1] = list_input[n+1], list_input[n]       

    return list_input

for i in input_vetor:
    input_vetor = bubble_sort()

print("Input Saída: ", input_vetor)