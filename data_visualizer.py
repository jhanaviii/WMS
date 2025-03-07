import matplotlib
matplotlib.use("TkAgg")  # Ensures Matplotlib works properly

import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, inventory_df):
        self.inventory_df = inventory_df

    def generate_visuals(self):
        try:
            # Identify the correct columns
            if "sku" in self.inventory_df.columns and "opening stock" in self.inventory_df.columns:
                sku_col = "sku"
                stock_col = "opening stock"
            else:
                print(f"⚠️ Warning: Could not find expected 'sku' and 'opening stock' columns.")
                print(f"Available columns: {self.inventory_df.columns}")
                return

            plt.figure(figsize=(12, 6))
            plt.bar(self.inventory_df[sku_col], self.inventory_df[stock_col], color='blue')
            plt.xlabel("SKU")
            plt.ylabel("Stock")
            plt.title("Inventory Stock Levels")
            plt.xticks(rotation=45)

            # Save instead of show
            plt.savefig("inventory_visual.png")
            print("✅ Visualization saved as 'inventory_visual.png'")

        except Exception as e:
            print(f"❌ Error generating visualization: {e}")
