
import csv

# Hardcoded stock prices (example prices in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

investments = []
total_investment = 0

print("===== STOCK TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found! Please choose an available stock.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment_value = price * quantity
    total_investment += investment_value

    investments.append([
        stock_name, quantity, price, investment_value
    ])

    print(f"{stock_name}: {quantity} shares x ${price} "
          f"= ${investment_value}")

# Display the investment summary
print("\n===== INVESTMENT SUMMARY =====")

if investments:
    for stock, quantity, price, value in investments:
        print(
            f"{stock}: {quantity} shares | "
            f"Price: ${price} | Value: ${value}"
        )

    print(f"\nTotal Investment: ${total_investment}")

    # Save results to a CSV file
    save_file = input("Save results to CSV? (yes/no): ").lower()

    if save_file == "yes":
        with open("stock_report.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Stock", "Quantity", "Price", "Investment Value"
            ])
            writer.writerows(investments)
            writer.writerow(["", "", "Total", total_investment])

        print("Report saved as stock_report.csv")

else:
    print("No investments entered.")

print("===== THANK YOU =====")
