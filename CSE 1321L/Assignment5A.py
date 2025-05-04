
def pairDifferences(numbers):
    if len(numbers) < 2:
        print("Not enough numbers to calculate differences.")
        return ()

    differences = tuple(abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1))
    return differences

user_input = input("Enter a list of numbers: ").strip()
try:
    number_list = list(map(int, user_input.split(',')))

    result = pairDifferences(number_list)

    if result:
        print(f"The absolute differences between consecutive numbers: {result}")
except ValueError:
    print("Invalid input. Please enter a comma-separated list of integers.")
