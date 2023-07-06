from models import Inventory
from rich.console import Console
from rich.table import Table

console = Console()


class InventoryService:
    def add(self, name: str, price: int, quantity: int):
        item = Inventory.create(name=name, price=price, quantity=quantity)

    def remove(self, name: str):
        item = Inventory.get(name=name)
        item.delete_instance()

    def display(self):
        items = Inventory.select()
        table = Table(
            "sl. No",
            "Name",
            "Price",
            "Avl. Quantity",
        )
        for i, item in enumerate(items):
            table.add_row(
                str(i + 1),
                item.name,
                f"Rs. {item.price}",
                str(item.quantity),
            )

        console.print(table)
