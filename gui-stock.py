import tkinter as tk
import yfinance as yf

# Create the main window
window = tk.Tk()
window.title("Stock Movement")

# Retrieve the stock data
stock = yf.Ticker("AAPL")
data = stock.history(period="1d")
# Get the current price and the change in price
price = data["Close"][-1]
change = data["Close"][-1] - data["Open"][-1]

# Create a label to display the current price
price_label = tk.Label(window, text=f"Price: ${price:.2f}")
price_label.pack()

# Create a label to display the change in price
change_label = tk.Label(window, text=f"Change: ${change:.2f}")
change_label.pack()

# Run the main loop
window.mainloop()
