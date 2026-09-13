from .lib import add_numbers, multiply_numbers


def main():
    """Demonstrates the use of functions imported from the lib module."""
    number1 = 5
    number2 = 3

    sum_result = add_numbers(number1, number2)
    product_result = multiply_numbers(number1, number2)

    print("Sum:", sum_result)
    print("Product:", product_result)


if __name__ == "__main__":
    main()
    