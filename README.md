# stock-portfolio-tracker_1
A simple Python-based Stock Portfolio Tracker that calculates total investment value using predefined stock prices and user-entered quantities. Includes investment summaries and optional CSV file export for record-keeping. Built using dictionaries, lists, basic arithmetic, input/output, and file handling.
Here’s a GitHub-ready brief description of your Stock Portfolio Tracker with its CSV file functionality and code explanation.

# Python Stock Portfolio Tracker 📈

## Description

A simple Python-based Stock Portfolio Tracker that calculates the total investment value using predefined stock prices. Users can enter stock symbols and quantities, view individual stock values and total investment, and optionally save the portfolio report to a CSV file.

## Features

- Predefined stock prices stored in a Python dictionary.
- Accepts stock symbols and share quantities from users.
- Calculates individual and total investment values.
- Validates stock symbols and quantities.
- Exports portfolio details to a CSV file for future reference.

## Technologies Used

- Python
- Dictionary and lists
- Loops and conditional statements
- Basic arithmetic
- CSV file handling

## Code Explanation

- **Dictionary (`stock_prices`):** Stores stock symbols and their predefined prices.
- **`input()`:** Accepts stock symbols and quantities from the user.
- **`while` loop:** Allows users to enter multiple stocks until they type `done`.
- **Conditional statements:** Validate stock symbols and quantities.
- **Arithmetic operations:** Calculate investment value using `stock price × quantity`.
- **List (`investments`):** Stores stock names, quantities, prices, and investment values.
- **CSV module:** Writes the portfolio summary to `stock_report.csv`.
- **`open()` and `csv.writer()`:** Create the CSV file and save the investment records and total.

## CSV File Output

The generated `stock_report.csv` contains the following columns:

| Stock | Quantity | Price | Investment Value |
| ----- | -------- | ----- | ---------------- |
| AAPL  | 10       | 180   | 1800             |
| TSLA  | 5        | 250   | 1250             |
| <br>  | <br>     | Total | 3050             |

The CSV file can be opened in Microsoft Excel, Google Sheets, or any compatible spreadsheet application.

## How to Run

1. Install Python.
2. Save the code as `stock_tracker.py`.
3. Open a terminal in the project folder.
4. Run:

```
python stock_tracker.py
```

5. Enter stock symbols and quantities.
6. Type `done` to view the portfolio summary.
7. Choose `yes` when prompted to save the CSV report.

## Learning Outcome

This project demonstrates Python dictionaries, lists, loops, input validation, arithmetic calculations, and CSV file handling.

**Note:** Stock prices are hardcoded examples and do not represent live market prices.

Suggested GitHub repository name: `python-stock-portfolio-tracker`

Short GitHub tagline: `A beginner-friendly Python stock portfolio tracker that calculates investment values and exports reports to CSV.`

code : 


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
