class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        days = 1

        i = len(self.prices) - 1 
        while i >= 0 and self.prices[i] <= price:
            consec = self.stack.pop()
            days += consec
            i -= consec

        self.stack.append(days)
        self.prices.append(price)

        return self.stack[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
