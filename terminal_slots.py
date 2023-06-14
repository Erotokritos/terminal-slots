import random


MAX_LINES = 3
MAX_BET = 20
MIN_BET = 0.1

ROWS = 3
COLS = 3

symbols_count = {" A ": 2, " K ": 3, " Q ": 5, " J ": 6, "10 ": 10}
symbols_values = {" A ": 5, " K ": 1, " Q ": 0.8, " J ": 0.5, "10 ": 0.2}


def check_winings(columns, lines, bet, values):
    winings = 0
    wining_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winings += values[symbol] * bet
            wining_lines.append(lines + 1)

    return winings, wining_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Make your deposit: EU ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number for a deposit")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Lines to bet must be between 1 and " + str(MAX_LINES) + "!")
        else:
            print("Please enter a number for a lines")
    return lines


def get_bet():
    while True:
        amount = input("Place your bet: EU ")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} EU - {MAX_BET} EU")
        else:
            print("Please enter a number for a bet")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(
                f"Not enough money! Your current balance is ${balance} EU. Please make a new bet!"
            )
        else:
            break
    print(
        f"You are bettting {bet} EU on {lines} lines. Total bet is equal for {total_bet} EU !"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slots(slots)
    winings, wining_lines = check_winings(slots, lines, bet, symbols_values)
    print(f"You won {winings} EU! ")
    print("on line ", *wining_lines)
    return winings - total_bet


def main():
    balance = deposit()
    while True:
        if balance == 0:
            print("You dont have any money!")
            answer = input("Do you want to make a new deposit ? y/n  : ")
            if answer == "y":
                balance = deposit()
            else:
                print("Thanks for playing ! ")
                quit()
        print(f"Current balance is : {balance}")
        answer = input("Press enter to spin (q to quit).")
        if spin == "q":
            quit()
        balance += spin(balance)

    print(f"You left with {balance}")


main()
