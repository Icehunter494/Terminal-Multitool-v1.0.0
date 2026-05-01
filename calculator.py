def run():
    print("Welcome to the calculator app!")
    print("Type 'q' at any time to return to the Main Menu.")
    

    while True:
        
        num1_raw = input("\nEnter first number: ").lower()
        if num1_raw == 'q':
            break

        op = input("Enter operator (+, -, *, /): ")
        if op == 'q':
            break

        num2_raw = input("Enter second number: ").lower()
        if op == 'q':
            break

        # Logic
        try:
            n1 = float(num1_raw)
            n2 = float(num2_raw)

            if op == "+":
                result = n1 + n2
            elif op == "-":
                result = n1 - n2
            elif op == "*":
                result = n1 * n2
            elif op == "/":
                if n2 == 0:
                    result = "Error: Cannot divide by zero!"
                else:
                    result = n1 / n2
            else:
                result = "Invalid operator!"
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numbers.")
            
    print("Exiting Calculator")