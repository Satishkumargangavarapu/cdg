
def management_system(tickets):
    category_count = {}
    category_expenses = {}
    total_expenses = 0

    for ticket in tickets:
        category = ticket["category"]
        expense = ticket["expense"]

        category_count[category] = category_count.get(category, 0) + 1
        category_expenses[category] = category_expenses.get(category, 0) + expense
        total_expenses += expense

    highest_category = max(
        category_expenses, key=category_expenses.get
    ) if category_expenses else None

    highest_cost = category_expenses.get(highest_category, 0)

    return (
        len(tickets),
        total_expenses,
        category_count,
        category_expenses,
        highest_category,
        highest_cost
    )


tickets = []
n = int(input("Enter the number of tickets: "))

for i in range(n):
    print(f"\nEnter details for ticket {i + 1}")
    category = input("Enter category: ")
    expense = float(input("Enter expense amount: "))

    tickets.append({
        "category": category,
        "expense": expense
    })

total_tickets, total_expenses, category_count, category_expenses, highest_category, highest_cost = management_system(tickets)

print("\n--- Management System Report ---")
print("Total tickets:", total_tickets)
print("Total expenses:", total_expenses)
print("Tickets by category:", category_count)
print("Expenses by category:", category_expenses)
print("Highest expense category:", highest_category)
print("Highest category expense:", highest_cost)

