class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

if __name__ == "__main__":
    counter = Counter()

    print("Welcome to the Python Counter App!")
    print("Commands: 'inc' to increment, 'dec' to decrement, 'get' to get value, 'quit' to exit")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == 'inc':
            counter.increment()
            print(f"Incremented. Current value: {counter.get_value()}")
        elif command == 'dec':
            counter.decrement()
            print(f"Decremented. Current value: {counter.get_value()}")
        elif command == 'get':
            print(f"Current value: {counter.get_value()}")
        elif command == 'quit':
            print("Exiting. Final value:", counter.get_value())
            break
        else:
            print("Invalid command. Use 'inc', 'dec', 'get', or 'quit'.")

    print("Counter runs properly!")
