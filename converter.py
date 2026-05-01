def run():
    print("\n--- Converter App ---")
    print("Type 'q' at any time to return to the Main Menu.")

    while True:
        print("\nCategories: 1) Length 2) Weight 3) Temperature")
        cat = input("Choose a category (or 'q'): ")

        if cat.lower() == 'q': break

        # length conversions
        if cat == '1':
            print("\n: Inches to cm | 2: cm to Inches")
            print("3: Feet to Meters | 4: Meters to Feet")
            choice = input("Select conversion: ")
            val = input("Enter value: ")
            if val.lower() == 'q': break

            try:
                num = float(val)
                if choice == '1': print(f"{num} in = {num * 2.54:.2f} cm")
                elif choice == '2': print(f"{num} cm = {num / 2.54:.2f} in")
                elif choice == '3': print(f"{num} ft = {num * 0.3048:.2f} m")
                elif choice == '4': print(f"{num} m = {num / 0.3048:.2f} ft")
            except ValueError: print("Invalid number.")

        # Weight conversions
        elif cat == '2':
            print("\n1: lbs to kg | 2: kg lbs")
            choice = input("Select conversion: ")
            val = input("Enter value: ")

            try:
                num = float(val)
                if choice == '1': print(f"{num} lbs = {num * 0.45359:.2f} kg")
                elif choice == '2': print(f"{num} kg = {num / 0.45359:.2f} lbs")
            except ValueError: print("Invalid number.")

        # Temp conversions
        if cat == '3':
            print("\n1: Farenheit to Celsius | 2: Celsius to Fahrenheit")
            choice = input("Select conversion: ")
            val = input("Enter value: ")

            try:
                num = float(val)
                if choice == '1': print(f"{num}°F = {(num-32) * 5/9:.2f}°C")
                elif choice == '2': print(f"{num}°C = {(num * 9/5) + 32:.2f}°F")
            except ValueError:print("Invalid number.")