portfolio = {}
def add_stk(logo, shares):
    """Add stock to the portfolio."""
    portfolio[logo] = shares
    print(f'Added {shares} shares of {logo} to your portfolio.')

def view_port():
    """View the current stock portfolio."""
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        print("Your Stock Portfolio:")
        for logo, shares in portfolio.items():
            print(f"{logo}: {shares} shares")

def myFunction():
    """Main function to run the portfolio tracker."""
    while True:
        print("\nOptions: ")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            logo = input("Enter stock logo: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stk(logo, shares)
        elif choice == '2':
            view_port()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    myFunction()
