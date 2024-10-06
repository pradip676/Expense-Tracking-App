#from expense import Expense

def main():
    print(f"🧝🏼 Running expense Tracker: ")

    #Get user input for expenses
    expense = get_user_expense()
    print(expense)

    #Write it to the file.
    write_expenses_to_file()

    # Read the file amd summerize expenses.
    summerize_expenses()

def get_user_expense():
    print(f"🧝🏼 Running expense Tracker: ")
    expense_name=input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "🍕 Food",
        "🏠 Home", 
        "👨‍💻 Work",
        "🎮 Fun",
        "💡 Miscellaneous"
    ]

    while True:
        print("Select the category: ")
        for i,category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1-{len(expense_categories)}]" 
        
        selected_index = int(input(f"Enter the category number{value_range}: ")) - 1  #need to add for conditions if user enters a b c or other things
        selected_category = expense_categories[selected_index]
        
        if selected_index in range(len(expense_categories)):
                return Expense(
                name=expense_name,category = selected_category,amount = expense_amount
                )
        else:
            print("Invalid category. Please try again")

        break    

def write_expenses_to_file():
    print(f"🧝🏼 Running expense Tracker: ") 

def summerize_expenses():
    print(f"🧝🏼 Running expense Tracker: ")     

if __name__ == "__main__":    
    main()