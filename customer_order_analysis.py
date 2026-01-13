"""
Customer Order Analysis Using Python
=====================================
This script analyzes customer orders to classify products, identify purchasing patterns,
and generate business insights for an e-commerce company.
"""

# ============================================================================
# TASK 1: STORE CUSTOMER ORDERS
# ============================================================================

# List of customer names
customer_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah"]

# Order details stored as tuples: (customer_name, product, price, category)
orders = [
    ("Alice", "Laptop", 899.99, "Electronics"),
    ("Alice", "Mouse", 29.99, "Electronics"),
    ("Alice", "T-Shirt", 19.99, "Clothing"),
    ("Bob", "Headphones", 149.99, "Electronics"),
    ("Bob", "Jeans", 49.99, "Clothing"),
    ("Bob", "Blender", 79.99, "Home Essentials"),
    ("Charlie", "Smartphone", 699.99, "Electronics"),
    ("Charlie", "Phone Case", 15.99, "Electronics"),
    ("Diana", "Dress", 89.99, "Clothing"),
    ("Diana", "Shoes", 69.99, "Clothing"),
    ("Diana", "Handbag", 120.00, "Clothing"),
    ("Edward", "Tablet", 399.99, "Electronics"),
    ("Edward", "Keyboard", 89.99, "Electronics"),
    ("Edward", "Desk Lamp", 34.99, "Home Essentials"),
    ("Fiona", "Coffee Maker", 99.99, "Home Essentials"),
    ("Fiona", "Toaster", 45.99, "Home Essentials"),
    ("Fiona", "Sweater", 55.99, "Clothing"),
    ("George", "Monitor", 299.99, "Electronics"),
    ("George", "USB Cable", 9.99, "Electronics"),
    ("George", "Curtains", 39.99, "Home Essentials"),
    ("Hannah", "Jacket", 129.99, "Clothing"),
    ("Hannah", "Scarf", 24.99, "Clothing"),
    ("Hannah", "Vacuum Cleaner", 189.99, "Home Essentials"),
]

# Dictionary mapping customers to their ordered products
customer_orders = {}
for name, product, price, category in orders:
    if name not in customer_orders:
        customer_orders[name] = []
    customer_orders[name].append(product)

print("=" * 70)
print("TASK 1: CUSTOMER ORDER DATA")
print("=" * 70)
print(f"\nCustomer Names: {customer_names}")
print(f"\nTotal Orders: {len(orders)}")
print("\nCustomer Orders Dictionary:")
for customer, products in customer_orders.items():
    print(f"  {customer}: {products}")


# ============================================================================
# TASK 2: CLASSIFY PRODUCTS BY CATEGORY
# ============================================================================

# Dictionary mapping each product to its category
product_categories = {}
for name, product, price, category in orders:
    product_categories[product] = category

# Set of unique product categories
unique_categories = set(category for _, _, _, category in orders)

print("\n" + "=" * 70)
print("TASK 2: PRODUCT CLASSIFICATION BY CATEGORY")
print("=" * 70)
print(f"\nUnique Product Categories: {unique_categories}")
print("\nProduct to Category Mapping:")
for product, category in product_categories.items():
    print(f"  {product} -> {category}")


# ============================================================================
# TASK 3: ANALYZE CUSTOMER ORDERS
# ============================================================================

# Calculate total spending per customer
customer_spending = {}
for name, product, price, category in orders:
    if name not in customer_spending:
        customer_spending[name] = 0
    customer_spending[name] += price

# Classify customers based on spending
customer_classification = {}
for customer, total in customer_spending.items():
    if total > 100:
        customer_classification[customer] = "High-Value Buyer"
    elif 50 <= total <= 100:
        customer_classification[customer] = "Moderate Buyer"
    else:
        customer_classification[customer] = "Low-Value Buyer"

print("\n" + "=" * 70)
print("TASK 3: CUSTOMER SPENDING ANALYSIS")
print("=" * 70)
print("\nCustomer Spending and Classification:")
print("-" * 50)
for customer in customer_names:
    if customer in customer_spending:
        total = customer_spending[customer]
        classification = customer_classification[customer]
        print(f"  {customer}: ${total:.2f} - {classification}")


# ============================================================================
# TASK 4: GENERATE BUSINESS INSIGHTS
# ============================================================================

# Calculate total revenue per category
category_revenue = {}
for name, product, price, category in orders:
    if category not in category_revenue:
        category_revenue[category] = 0
    category_revenue[category] += price

# Extract unique products using a set
unique_products = set(product for _, product, _, _ in orders)

# List comprehension to find customers who purchased electronics
electronics_buyers = list(set([name for name, product, price, category in orders if category == "Electronics"]))

# Identify top 3 highest-spending customers
sorted_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)
top_3_customers = sorted_customers[:3]

print("\n" + "=" * 70)
print("TASK 4: BUSINESS INSIGHTS")
print("=" * 70)

print("\n1. Total Revenue per Category:")
print("-" * 40)
for category, revenue in sorted(category_revenue.items(), key=lambda x: x[1], reverse=True):
    print(f"   {category}: ${revenue:.2f}")

total_revenue = sum(category_revenue.values())
print(f"\n   TOTAL REVENUE: ${total_revenue:.2f}")

print(f"\n2. Unique Products ({len(unique_products)} items):")
print("-" * 40)
for product in sorted(unique_products):
    print(f"   - {product}")

print(f"\n3. Customers Who Purchased Electronics:")
print("-" * 40)
for buyer in sorted(electronics_buyers):
    print(f"   - {buyer}")

print(f"\n4. Top 3 Highest-Spending Customers:")
print("-" * 40)
for rank, (customer, spending) in enumerate(top_3_customers, 1):
    print(f"   #{rank}: {customer} - ${spending:.2f}")


# ============================================================================
# TASK 5: ORGANIZE AND DISPLAY DATA
# ============================================================================

# Find customers who purchased from each category
customers_by_category = {}
for name, product, price, category in orders:
    if category not in customers_by_category:
        customers_by_category[category] = set()
    customers_by_category[category].add(name)

# Customers who purchased from multiple categories
multi_category_shoppers = set()
customer_categories = {}
for name, product, price, category in orders:
    if name not in customer_categories:
        customer_categories[name] = set()
    customer_categories[name].add(category)

for customer, categories in customer_categories.items():
    if len(categories) > 1:
        multi_category_shoppers.add(customer)

# Customers who bought both electronics AND clothing (set intersection)
electronics_customers = customers_by_category.get("Electronics", set())
clothing_customers = customers_by_category.get("Clothing", set())
electronics_and_clothing = electronics_customers & clothing_customers

print("\n" + "=" * 70)
print("TASK 5: ADVANCED DATA ANALYSIS")
print("=" * 70)

print("\n1. Customer Spending Summary:")
print("-" * 60)
print(f"{'Customer':<12} {'Total Spent':>12} {'Classification':<20} {'Categories'}")
print("-" * 60)
for customer in sorted(customer_names):
    if customer in customer_spending:
        total = customer_spending[customer]
        classification = customer_classification[customer]
        categories = ", ".join(sorted(customer_categories.get(customer, set())))
        print(f"{customer:<12} ${total:>10.2f}  {classification:<20} {categories}")

print(f"\n2. Multi-Category Shoppers (bought from 2+ categories):")
print("-" * 40)
for customer in sorted(multi_category_shoppers):
    categories = ", ".join(sorted(customer_categories[customer]))
    print(f"   - {customer}: {categories}")

print(f"\n3. Customers Who Bought Both Electronics AND Clothing:")
print("-" * 40)
for customer in sorted(electronics_and_clothing):
    print(f"   - {customer}")


# ============================================================================
# FINAL SUMMARY REPORT
# ============================================================================

print("\n" + "=" * 70)
print("FINAL BUSINESS REPORT SUMMARY")
print("=" * 70)

# Count customers by classification
classification_counts = {}
for classification in customer_classification.values():
    classification_counts[classification] = classification_counts.get(classification, 0) + 1

print("\n📊 CUSTOMER CLASSIFICATION BREAKDOWN:")
for classification, count in sorted(classification_counts.items()):
    print(f"   • {classification}: {count} customer(s)")

print(f"\n💰 REVENUE INSIGHTS:")
print(f"   • Total Revenue: ${total_revenue:.2f}")
print(f"   • Top Category: {max(category_revenue, key=category_revenue.get)} (${max(category_revenue.values()):.2f})")
print(f"   • Number of Unique Products: {len(unique_products)}")

print(f"\n👥 CUSTOMER INSIGHTS:")
print(f"   • Total Customers: {len(customer_names)}")
print(f"   • Active Customers (with orders): {len(customer_spending)}")
print(f"   • Multi-Category Shoppers: {len(multi_category_shoppers)}")
print(f"   • Electronics & Clothing Buyers: {len(electronics_and_clothing)}")

print(f"\n🏆 TOP PERFORMER:")
top_customer, top_spending = top_3_customers[0]
print(f"   • Highest Spender: {top_customer} (${top_spending:.2f})")

print("\n" + "=" * 70)
print("END OF REPORT")
print("=" * 70)
