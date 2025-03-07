import pandas as pd

class SalesProcessor:
    def __init__(self, sales_file):
        """Initialize SalesProcessor with the given sales CSV file."""
        self.sales_file = sales_file
        self.sales_data = None

    def process_sales(self):
        """Loads and processes sales data from the CSV file."""

        # Read sales data
        df_sales = pd.read_csv(self.sales_file)

        # Force lowercase and remove extra spaces in column names
        df_sales.columns = [col.strip().lower() for col in df_sales.columns]

        # Print detected column names
        print("✅ Columns in Sales CSV:", df_sales.columns.tolist())

        # Expected column variations
        expected_columns = {
            "order_id": ["orderid", "sub order no", "packet id"],  # Possible alternatives
            "sku": ["sku", "product name"],  # If SKU mapping differs
        }

        # Map expected columns to actual columns in the CSV
        column_mapping = {}
        for key, alternatives in expected_columns.items():
            found_column = next((col for col in alternatives if col in df_sales.columns), None)
            if found_column:
                column_mapping[key] = found_column
            else:
                raise ValueError(
                    f"❌ Required column '{key}' missing in {self.sales_file}. Found: {df_sales.columns.tolist()}"
                )

        # Rename columns to a standard format
        df_sales.rename(columns=column_mapping, inplace=True)

        # Store processed sales data
        self.sales_data = df_sales
        print(f"✅ Using '{column_mapping['order_id']}' as Order ID Column")
        print(f"✅ Using '{column_mapping['sku']}' as SKU Column")
        print("✅ Loaded Sales Data Successfully")
