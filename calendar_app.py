import calendar
import datetime

def run():
    print("\n--- Interactive Calendar ---")

    # get cur date
    now = datetime.datetime.now()
    curr_year = now.year
    curr_month = now.month

    while True:
        print(f"\n1. View Current Month ({calendar.month_name[curr_month]})")
        print("2. View a Specific Month/Year")
        print("3. View a Full Year")
        print("q. Return to Main Menu")

        choice = input("\nSelect an option: ").lower()
        
        if choice == 'q':
            break

        elif choice == '1':
            #dis cur month
            print("\n" + calendar.month(curr_year, curr_month))

        elif choice == '2':
            try:
                year = int(input("Enter Year (e.g. 2024): "))
                month = int(input("Enter Month (1-12): "))
                if 1 <= month <= 12:
                    print("\n" + calendar.month(year, month))
                
                else:
                    print("Invalid month! Use 1-12.")
            except ValueError:
                print("Invalid input! Please use numbers.")
        elif choice == '3':
            try:
                year = int(input("Enter Year: "))
                print("\n" + calendar.calendar(year)) # Displays full yr
            except ValueError:
                print("Invalid input!")
    
    input("\nPress Enter to return to menu...")