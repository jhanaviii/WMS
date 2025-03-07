import pandas as pd

class SKUMapper:
    def __init__(self, mapping_file):
        """Initialize SKUMapper with the given SKU-to-MSKU mapping file."""
        self.mapping_file = mapping_file
        self.sku_msku_map = {}

    def load_mappings(self):
        """Loads SKU to MSKU mappings from the CSV file."""
        if not self.mapping_file:
            raise ValueError("Error: No mapping file provided to SKUMapper.")

        df_sku = pd.read_csv(self.mapping_file)

        # Force all column names to lowercase
        df_sku.columns = [col.strip().lower() for col in df_sku.columns]

        # Debugging print to verify changes
        print("Modified Column Names:", df_sku.columns.tolist())

        # Ensure expected columns exist (using lowercase keys)
        expected_cols = ["sku", "msku"]
        for col in expected_cols:
            if col not in df_sku.columns:
                raise ValueError(f"Column '{col}' not found in {self.mapping_file}. Found columns: {df_sku.columns}")

        # Convert to dictionary
        self.sku_msku_map = dict(zip(df_sku["sku"], df_sku["msku"]))

        print("✅ Loaded SKU mappings successfully")
