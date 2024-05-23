import checkers

def game():
    while True:
        try:
            size = int(input("Enter the size of the board (between 4 and 16): "))
            if 4 <= size <= 16:
                break
            else:
                print("Size must be between 4 and 16.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    board = checkers.build_board(size)
    print("Generated board: ")
    print(board)

    empty_count = checkers.get_count(board, 'Empty')
    red_count = checkers.get_count(board, 'Red')
    black_count = checkers.get_count(board, 'Black')

    print(f'Empty cells: {empty_count}')
    print(f'Red cells: {red_count}')
    print(f'Black cells: {black_count}')

if __name__ == "__main__":
    game()