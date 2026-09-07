# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOGL": 140,
    "AMZN": 145
}

print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(stock, "-", price)

portfolio = {}
total_investment = 0

while True:
    symbol = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if symbol == "DONE":
        break

    if symbol in stock_prices:
        qty = int(input("Enter quantity: "))
        cost = stock_prices[symbol] * qty
        total_investment += cost
        portfolio[symbol] = qty
        print(f"Added {qty} shares of {symbol}, cost = {cost}")
    else:
        print("Stock not found in list!")
              