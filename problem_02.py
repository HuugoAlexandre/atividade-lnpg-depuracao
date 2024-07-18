#Declaração do problema: Dada uma matriz de números inteiros, encontre a soma máxima de uma submatriz de tamanho k.
import math

def max_subarr_sum(arr, k): # fix : função modificada para lidar com matriz bidimensional
    rows = len(arr)
    cols = len(arr[0])
    if rows < k or cols < k or k <= 0: # fix : verifica se a submatriz é válida (se ela "cabe" na matriz de entrada)
        print("Invalid input")
        return -1
    max_sum = float('-inf')
    for i in range(rows - k + 1): # fix : calcula a soma da submatriz k x k
        for j in range(cols - k + 1):
            current_sum = 0
            for p in range(i, i + k):
                for q in range(j, j + k):
                    current_sum += arr[p][q]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def read_input(): # fix : função modificada para lidar com formatos diferentes de array
    try:
        arr_input = input("Enter the array elements separated by spaces: ").strip()
        if not arr_input:
            print("Empty array.")
            return [], 0
        elements = list(map(int, arr_input.split()))
        
        num_elements = len(elements)
        rows = int(input("Enter the number of rows: ")) # fix : pede obrigatoriamente o número de linhas para verificar se é possível formar a matriz desejada
        cols = int(input("Enter the number of columns: ")) # fix : pede obrigatoriamente o número de colunas para verificar se é possível formar a matriz desejada
        
        if rows * cols != num_elements: # fix : se o produto das linhas por colunas não coincidir a quantidade de elementos, não será possível construir a matriz 
            print("The number of elements does not match the provided dimensions.")
            return [], 0
        
        arr = [elements[i:i + cols] for i in range(0, num_elements, cols)] # fix : a matriz é construída dividindo a lista em sublistas de tamanho 'cols' (cada sublista é uma linha da matriz)
        
        k = int(input("Enter the size of the subarray (k): ")) 
        return arr, k
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return [], 0
    
def main():
    arr, k = read_input()
    if arr: # fix : exibe resultado apenas se forem dadas entradas
        result = max_subarr_sum(arr, k)
        if result != -1:
            print("Maximum sum of a subarray of size {} is {}".format(k, result))

if __name__ == "__main__":
    main()