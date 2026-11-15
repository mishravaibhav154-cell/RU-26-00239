# Pharmacy Inventory System

A simple console application for managing a pharmacy's medicine stock.

The program stores medicine details in a CSV file and allows medicines to be added, sold, deleted, and checked for low stock.

## Features

- Add new medicines
- Sell medicines and generate the bill amount
- Prevent selling more than the available stock
- Show medicines with low stock (quantity below 10)
- View the current inventory and its total value
- Delete medicines
- Save changes to `medicines.csv`

## Files

```text
.
├── main.py
├── medicines.csv
└── README.md
```

## Requirements

- Python 3

No external libraries are required.

## Running the program

Clone or download the project, then open a terminal in the project folder.

```bash
python main.py
```

## Medicine data

The CSV file uses the following columns:

| ID | Name | Quantity | Price |
|----|------|----------|-------|

Medicine IDs start from `M1`. New medicines are assigned the next available ID.

## Menu

```text
1. Add medicine
2. Sell medicine
3. Low-stock report
4. Inventory value
5. Delete medicine
6. Exit
```

## Notes

- Quantity and price must be greater than zero when adding a medicine.
- A sale cannot exceed the available quantity.
- A medicine is considered low stock when its quantity is below 10.
- All changes are written back to the CSV file after an add, sale, or delete operation.
