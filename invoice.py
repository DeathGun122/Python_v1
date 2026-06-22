def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"You bill of ${amount:.2f} is due on {due_date}")

display_invoice("BroCode", 56223524.25, "01/01")