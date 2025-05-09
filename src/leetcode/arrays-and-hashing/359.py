class Logger:

    def __init__(self):
        self.limit = defaultdict(int) # { message: timestamp }
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.limit or self.limit[message] <= timestamp:
            self.limit[message] = timestamp + 10 # Update the message's timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
