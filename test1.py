import matplotlib.pyplot as plt



def draw_benin_flag():
    GREEN = "\033[48;2;0;150;57m"   # RGB for #009639
    YELLOW = "\033[48;2;252;209;22m"  # RGB for #FCD116
    RED = "\033[48;2;239;51;64m"     # RGB for #EF3340
    RESET = "\033[0m"

    for _ in range(3):  # Green vertical stripe
        print(GREEN + " " * 9 + RESET + YELLOW + " " * 16 + RESET)
    for _ in range(3):  # Red horizontal stripe
        print(GREEN + " " * 9 + RESET + RED + " " * 16 + RESET)



def draw_diamond_pattern():
    size = 4

    for row in range(-size, size + 1):
        line = ""
        for col in range(-3 * size, 3 * size + 1):

            if abs(row) + abs(col) <= size or abs(row) + abs(col - 2 * size) <= size:
                line += "*"
            else:
                line += " "
        print(line)


def raw_graphic():
    height = 10
    width = 10

    for y in range(height, -1, -1):
        line = ""
        for x in range(width + 1):
            if y == 0 and x == 0:
                line += "+"
            elif y == 0:
                line += "-"
            elif x == 0:
                line += "|"
            elif y == x:
                line += "*"
            else:
                line += " "
        print(line)

def draw_percentage():
    with open('sequence.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file]

    filtered_numbers = [num for num in numbers if -5 <= num <= 5]

    count_0_to_5 = sum(1 for num in filtered_numbers if 0 <= num <= 5)
    count_minus5_to_0 = sum(1 for num in filtered_numbers if -5 <= num < 0)
    total = len(filtered_numbers)

    percent_0_to_5 = (count_0_to_5 / total) * 100 if total > 0 else 0
    percent_minus5_to_0 = (count_minus5_to_0 / total) * 100 if total > 0 else 0

    labels = ['0 to 5', '-5 to 0']
    sizes = [percent_0_to_5, percent_minus5_to_0]
    colors = ['blue', 'red']
    explode = (0.1, 0)

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Percentage Distribution: 0 to 5 vs -5 to 0')
    plt.show()

    print(f"Percentage 0 to 5: {percent_0_to_5}%")
    print(f"Percentage -5 to 0: {percent_minus5_to_0}%")


# Menu for Running Tasks
def main():
    print("Lab 1 Tasks")
    while True:
        print("\nSelect a task to run:")
        print("1. Draw Flag")
        print("2. Draw Patterns")
        print("3. Draw Function Graph")
        print("4. Draw Percentage")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            draw_benin_flag()
        elif choice == "2":
            draw_diamond_pattern()

        elif choice == "3":
            raw_graphic()

        elif choice == "4":
            draw_percentage()

        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()