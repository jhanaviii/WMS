import os
import logging
from sku_mapper import SKUMapper
from inventory_manager import InventoryManager
from sales_processor import SalesProcessor
from data_visualizer import DataVisualizer

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Update file paths correctly before running
sku_mapping_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/data/WMS-04-02 - Msku With Skus.csv"
inventory_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/data/WMS-04-02 - Current Inventory .csv"
sales_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/data/Orders_2025-01-26_2025-02-01_2025-02-04_12_12-12_17_528114.csv"


# Function to check if files exist
def check_file_exists(file_path):
    if not os.path.exists(file_path):
        logging.error(f"❌ File not found: {file_path}")
        exit(1)


# Validate all required files
for file in [sku_mapping_file, inventory_file, sales_file]:
    check_file_exists(file)

try:
    # Initialize modules
    sku_mapper = SKUMapper(sku_mapping_file)
    sku_mapper.load_mappings()

    inventory_manager = InventoryManager(inventory_file)
    inventory_manager.load_inventory()

    sales_processor = SalesProcessor(sales_file)
    sales_processor.process_sales()

    # Generate and save visualizations
    data_visualizer = DataVisualizer(inventory_manager.inventory_data)
    visualization_path = data_visualizer.generate_visuals()

    logging.info(f"✅ Visualization saved at: {visualization_path}")

    logging.info("✅ Warehouse Management System execution completed successfully.")

except Exception as e:
    logging.error(f"❌ An error occurred: {e}")
    exit(1)
