import csv
from pathlib import Path

FILE_NAME = "medicines.csv"
LOW_STOCK_LIMIT = 10


def load_medicines():
    medicines = []

    if not Path(FILE_NAME).exists():
        return medicines

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            medicines.append({
                "ID": row["ID"],
                "Name": row["Name"],
                "Quantity": int(row["Quantity"]),
                "Price": float(row["Price"])
            })

    return medicines


def save_medicines(medicines):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        fields = ["ID", "Name", "Quantity", "Price"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for medicine in medicines:
            writer.writerow({
                "ID": medicine["ID"],
                "Name": medicine["Name"],
                "Quantity": medicine["Quantity"],
                "Price": f'{medicine["Price"]:.2f}'
            })


def get_next_id(medicines):
    if not medicines:
        return "M1"

    highest = max(int(medicine["ID"][1:]) for medicine in medicines)
    return f"M{highest + 1}"


def get_positive_number(prompt, number_type=int):
    while True:
        value = input(prompt).strip()

        try:
            number = number_type(value)
            if number > 0:
                return number
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def find_medicine(medicines, medicine_id):
    for medicine in medicines:
        if medicine["ID"].lower() == medicine_id.lower():
            return medicine
    return None


def add_medicine(medicines):
    name = input("Name: ").strip()

    if not name:
        print("Medicine name cannot be empty.")
        return

    quantity = get_positive_number("Quantity: ")
    price = get_positive_number("Price: ", float)

    medicine_id = get_next_id(medicines)
    medicines.append({
        "ID": medicine_id,
        "Name": name,
        "Quantity": quantity,
        "Price": price
    })

    save_medicines(medicines)
    print(
        f"Medicine added. ID: {medicine_id} | {name} | "
        f"Qty: {quantity} | Price: {price:.2f}"
    )


def sell_medicine(medicines):
    medicine_id = input("ID: ").strip()
    medicine = find_medicine(medicines, medicine_id)

    if medicine is None:
        print("Medicine not found.")
        return

    quantity = get_positive_number("Quantity: ")

    if quantity > medicine["Quantity"]:
        print(f'Insufficient stock. Available: {medicine["Quantity"]}')
        return

    total = quantity * medicine["Price"]
    medicine["Quantity"] -= quantity
    save_medicines(medicines)

    print(f"Sold {quantity} units. Bill: {total:.2f}")
    print(f'Stock left: {medicine["Quantity"]}', end="")

    if medicine["Quantity"] == 0:
        print(" | Out of stock")
    else:
        print()


def show_low_stock(medicines):
    low_stock = [
        medicine for medicine in medicines
        if medicine["Quantity"] < LOW_STOCK_LIMIT
    ]

    if not low_stock:
        print("No low-stock medicines.")
        return

    print("\nLow-stock report:")
    for medicine in low_stock:
        print(
            f'{medicine["ID"]} | {medicine["Name"]} | '
            f'Qty: {medicine["Quantity"]} (Low stock)'
        )


def show_inventory(medicines):
    if not medicines:
        print("Inventory is empty.")
        return

    print("\nCurrent inventory:")
    print("-" * 50)

    total_value = 0
    for medicine in medicines:
        value = medicine["Quantity"] * medicine["Price"]
        total_value += value
        print(
            f'{medicine["ID"]} | {medicine["Name"]} | '
            f'Qty: {medicine["Quantity"]} | Price: {medicine["Price"]:.2f}'
        )

    print("-" * 50)
    print(f"Total inventory value: {total_value:.2f}")


def delete_medicine(medicines):
    medicine_id = input("ID: ").strip()
    medicine = find_medicine(medicines, medicine_id)

    if medicine is None:
        print("Medicine not found.")
        return

    medicines.remove(medicine)
    save_medicines(medicines)
    print(f'Medicine deleted: {medicine["ID"]} | {medicine["Name"]}')


def show_menu():
    print("\nPharmacy Inventory System")
    print("1. Add medicine")
    print("2. Sell medicine")
    print("3. Low-stock report")
    print("4. Inventory value")
    print("5. Delete medicine")
    print("6. Exit")


def main():
    medicines = load_medicines()

    while True:
        show_menu()
        choice = input("Menu option: ").strip()

        if choice == "1":
            add_medicine(medicines)
        elif choice == "2":
            sell_medicine(medicines)
        elif choice == "3":
            show_low_stock(medicines)
        elif choice == "4":
            show_inventory(medicines)
        elif choice == "5":
            delete_medicine(medicines)
        elif choice == "6":
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Please choose a valid menu option (1-6).")

if __name__ == "__main__":
    main()
