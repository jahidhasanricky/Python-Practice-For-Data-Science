import matplotlib.pyplot as plt

def make_graph(stock_data, stock_symbol):
    plt.figure(figsize=(10,5))
    plt.plot(stock_data.index, stock_data['Close'], label=stock_symbol)
    plt.title(f"{stock_symbol} Stock Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

make_graph(tesla_data, "TSLA")
