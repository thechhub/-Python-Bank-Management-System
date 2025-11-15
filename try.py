def show_menu():
    print("1. Create a new account")
    print("2. Deposit balance")
    print("3. Check balance")
    print("4. Withdaw balance")
    print("5. Exit")


def open_account():
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    initial_deposit =float(input("Enter your Intial depoit:"))
    account_type = input("Enter Account type (savings/checling): ")
    
    x = 0
    with open("bank_data.txt", "r") as file:
        for line in file:
            x += 1
    
    account_number = x
    print("Account created suceesfully")
    
    with open("bank_data.txt", "a") as file:
        file.write(f"{first_name},{last_name},{initial_deposit},{account_type},{account_number}\n")
    print(f"Your account number is: {account_number}")

    return first_name, last_name, initial_deposit, account_type, account_number
    


def deposit_balance():
    x = input("Enter your account Number: ")
    new_deposit = float(input("Enter amount to deposit: "))

    with open("bank_data.txt", "r") as file:
        lines = file.readlines()

    updated_lines = []        
    account_found = False     

    for line in lines:
        data = line.strip()

        if data[4] == x:               
            account_found = True
            print("Account Found")

            current_balance = float(data[2])
            updated_balance = current_balance + new_deposit

            updated_line = f"{data[0]},{data[1]},{updated_balance},{data[3]},{data[4]}\n"
            updated_lines.append(updated_line)

        else:
            updated_lines.append(line)   # keep old line

    with open("bank_data.txt", "w") as file:
        file.writelines(updated_lines)

    if account_found:
        print("Deposit Successful.")
        print("New balance is:", updated_balance)
    else:
        print("Account not found.")

def check_balance():
    x = input("Enter your account Number: ")

    account_found = False   # Track if account exists

    with open("bank_data.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            data = line.strip()

            if data[4] == x:
                account_found = True
                print("Account Found")
                current_balance = float(data[2])
                print("Your current balance is:", current_balance)
                break   

    if not account_found:
        print("Account not found.")


def withdraw_balance():
    x = input("Enter your account Number: ")
    new_deposit = float(input("Enter amount to withdraw: "))

    with open("bank_data.txt", "r") as file:
        lines = file.readlines()

    updated_lines = []        
    account_found = False     

    for line in lines:
        data = line.strip()

        if data[4] == x:               
            account_found = True
            print("Account Found")

            current_balance = float(data[2])
            updated_balance = current_balance - new_deposit

            updated_line = f"{data[0]},{data[1]},{updated_balance},{data[3]},{data[4]}\n"
            updated_lines.append(updated_line)

def main():
    show_menu()
    choice = input("Enter your choice (1-5):")
    if choice == '1':
        open_account()
    elif choice == '2':
        deposit_balance()
    elif choice == '3':
        check_balance()
    elif choice == '4':
        withdraw_balance()
    elif choice == '5':
        print ('Exiting the program. Goodbye!')
        exit()
    else:
        print("Invalid choice. Please try again")

if __name__ == "__main__":
    while True:
        main()
