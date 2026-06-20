def main():
    from functools import reduce

    categories = []
    sp_amount = []

    print("Please enter your monthly expenses. Type 'done' when you are finished.")

    # 1. Dynamically gather categories and amounts
    while True:
        category = input("\nEnter expense category (or type 'done'): ").strip().lower()
        if category == 'done':
            break

        amount = float(input(f"How much did you spend on '{category}'? "))

        categories.append(category)
        sp_amount.append(amount)

    # Check if the user actually entered anything before running calculations
    if len(sp_amount) > 0:
        print("\n--- Expense Summary ---")
        for category, amount in zip(categories, sp_amount):
            print(f"You spent ${amount:.2f} on {category} this month.")

        # 2. Calculations using reduce and lambda (remains the same)
        total_expense = reduce(lambda acc, curr: acc + curr, sp_amount, 0)

        expense_pairs = list(zip(categories, sp_amount))
        highest_expense = reduce(lambda acc, curr: curr if curr[1] > acc[1] else acc, expense_pairs)
        lowest_expense = reduce(lambda acc, curr: curr if curr[1] < acc[1] else acc, expense_pairs)

        # 3. Display final results
        print(f"Total Monthly Expense: ${total_expense:.2f}")
        print(f"Highest Expense Label: {highest_expense[0]} (${highest_expense[1]:.2f})")
        print(f"Lowest Expense Label: {lowest_expense[0]} (${lowest_expense[1]:.2f})")
    else:
        print("\nNo expenses were entered.")

if __name__ == "__main__":
    main()