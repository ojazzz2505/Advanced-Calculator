import math

while True:
    # Define the calculator function
    def calculator():
        # Display the menu
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Square root")
        print("7. Trigonometric functions")
        print("8. Quit")

        # Ask the user to enter their choice
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        # Initialize result
        result = None

        # Ask the user to enter one or two numbers, depending on the operation
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice == '6':
            num = float(input("Enter number: "))
        elif choice == '7':
            angle = float(input("Enter angle in degrees: "))
        elif choice == '8':
            # End the program if '8' is chosen
            exit()
        else:
            print('INVALID CHOICE')
            return

        # Perform the selected operation
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            result = num1 / num2
        elif choice == '5':
            result = num1 ** num2
        elif choice == '6':
            result = math.sqrt(num)
        elif choice == '7':
            radian = math.radians(angle)
            result_sin = math.sin(radian)
            result_cos = math.cos(radian)
            result_tan = math.tan(radian)
            result = f"sin({angle}) = {result_sin}, cos({angle}) = {result_cos}, tan({angle}) = {result_tan}"


        # Print the result
        if result is not None:
            print("Result: ", result)
            print(choice)

    # Call the calculator function
    calculator()

    # Ask if the user wants to continue
    continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("Goodbye!")
        break
