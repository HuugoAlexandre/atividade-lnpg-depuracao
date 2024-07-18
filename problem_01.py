def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers) if numbers else None # fix: retorna None caso a lista esteja vazia

def find_max(numbers):
    if not numbers: return None # fix: retorna None caso a lista esteja vazia 
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    try: # fix: tratamento de exceção para casos em que não há entrada ou entrada inválida
        numbers = input("Enter numbers separated by spaces: ").split()
        if not numbers:
            print("No numbers entered.")
            return []
        numbers = [float(num) for num in numbers] # fix: permite que floats sejam calculados
        return numbers
    except ValueError:
        print("Please enter valid numbers separated by spaces.")
        return []

def main():
    numbers = get_numbers()
    if numbers:
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_max(numbers))

if __name__ == "__main__":
    main()