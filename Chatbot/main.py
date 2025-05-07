import time

catalog = {
    "alchemist": 499,
    "mockingbird": 599,
    "1984": 449,
    "gatsby": 399,
    "harry potter": 699,
    "lotr": 799,
    "sapiens": 599,
}

# Payment options
payments = ["cash", "online", "upi", "card"]

def order_book():
    print("\nWelcome to Bright Minds Bookstore!")
    print("Available books:")
    for book, price in catalog.items():
        print(f"- {book.title()} : Rs.{price}")
    
    book = input("\nEnter book name: ").lower()
    while book not in catalog:
        book = input("Book not found. Try again: ").lower()

    method = input("Enter payment method (cash/online/upi/card): ").lower()
    while method not in payments:
        method = input("Invalid method. Try again: ").lower()

    print("\nGenerating receipt...")
    time.sleep(1)
    print(f"\nYou bought '{book.title()}' for Rs.{catalog[book]}")
    print(f"Payment: {method.title()}")
    print("Thank you for shopping with us!")

order_book()
