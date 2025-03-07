import pandas as pd

class InventoryManager:
    def __init__(self, inventory_file):
        """Initialize InventoryManager with the given inventory CSV file."""
        self.inventory_file = inventory_file
        self.inventory_data = None

    def load_inventory(self):
        """Loads inventory data from the CSV file, ensuring correct headers."""

        # Read first few rows to inspect structure
        preview = pd.read_csv(self.inventory_file, nrows=5, header=None)
        print("\n🔍 CSV Preview (First 5 Rows):\n", preview)

        # ✅ Read CSV with second row (index 1) as header, skipping first row
        df_inventory = pd.read_csv(self.inventory_file, header=1)

        # Force lowercase and remove extra spaces
        df_inventory.columns = [str(col).strip().lower() for col in df_inventory.columns]

        # Print modified column names
        print("✅ Corrected Inventory Column Names:", df_inventory.columns.tolist())

        # Expected SKU column variations
        possible_sku_columns = ["sku", "product name", "msku"]

        # Find the first matching column
        sku_column = next((col for col in possible_sku_columns if col in df_inventory.columns), None)

        if sku_column is None:
            raise ValueError(
                f"❌ No SKU-like column found in {self.inventory_file}.\n"
                f"Found Columns: {df_inventory.columns.tolist()}\n"
                f"🔍 CSV Preview (First 5 Rows):\n{preview}"
            )

        # Rename detected SKU column to 'sku' for consistency
        df_inventory.rename(columns={sku_column: "sku"}, inplace=True)

        # Store inventory data
        self.inventory_data = df_inventory
        print(f"✅ Using '{sku_column}' as SKU Column")
        print("✅ Loaded Inventory Data Successfully")
