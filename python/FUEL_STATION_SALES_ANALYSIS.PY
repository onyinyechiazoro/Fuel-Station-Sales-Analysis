import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": ["monday", "tuesday", "monday", "monday", "tuesday", "tuesday",
            "wednesday", "wednesday", "thursday", "wednesday", "friday",
            "friday", "saturday", "saturday", "sunday", "sunday", "friday",
            "thursday", "thursday", "sunday"],
    
    "fuel_type": ["PMS", "AGO", "DPK", "jet_AI", "LPG", "CNG", "premium_petrol",
                  "regular_petrol", "super_unleaded_petrol", "biodiesel", "ethanol_fuel",
                  "E10_fuel", "E85_fuel", "bioethanol", "LNG", "hydrogen_fuel",
                  "methanol_fuel", "propane", "butane", "HFO"],
    
    "cost_price": [885, 1050, 1100, 1200, 1100, 1050, 1300, 1000, 900, 1080,
                   1300, 1200, 1050, 1000, 910, 1400, 1500, 1320, 1260, 1100],
    
    "selling_price": [950, 1150, 1200, 1300, 1200, 1150, 1450, 1150, 1000, 1200,
                      1400, 1300, 1200, 1150, 1100, 1550, 1650, 1420, 1340, 1210],
    
    "quantity_sold": [1200, 850, 450, 300, 1400, 900, 500, 300, 1350, 800,
                      450, 320, 1500, 870, 460, 340, 1250, 910, 490, 310],
    
    "pump_number": ["pump_1", "pump_2", "pump_1", "pump_3", "pump_4", "pump_1",
                    "pump_2", "pump_4", "pump_1", "pump_3", "pump_2", "pump_1",
                    "pump_4", "pump_2", "pump_3", "pump_1", "pump_2", "pump_4",
                    "pump_1", "pump_3"]
            
}

df = pd.DataFrame(data)

# Adding a column for Profit
df["profit"] =  (df["selling_price"] - df["cost_price"]) * df["quantity_sold"]

# Adding a column for Sales_Amount
df["sales_amount"] = df["selling_price"] * df["quantity_sold"]
print(df)

# saving my dataframe to csv file because the dataset will be used in powerBI
df.to_csv("fuel_station_data.csv", index=False)

# Which fuel type generated the highest profit?
highest_profit_fuel_type = df.groupby("fuel_type")["profit"].sum().idxmax()
print("\n Fuel_type with Highsest Profit")
print(highest_profit_fuel_type)

# Insight:
# E85_fuel generated the highest total profit among all fuel types,
# indicating that it was the most profitable fuel in the dataset.

#Which day recorded the highest sales amount?
highest_sales_amount = df.groupby("day")["sales_amount"].sum().idxmax()
print("\n Day with Highest Sales_amount")
print(highest_sales_amount)

# Insight:
# Tuesday recorded the highest sales amount, indicating that it was
# the strongest sales day in the dataset.

# which pump number generated the highest revenue?
pump_number_with_highest_revenue = df.groupby("pump_number")["sales_amount"].sum().idxmax()
print("\n Pump number with Highest Revenue")
print(pump_number_with_highest_revenue)

# Insight:
# Pump_1 generated the highest revenue among all pumps,
# indicating that it contributed the most to the fuel station's total sales.

# which fuel type sold the highest quantity
fuel_type_with_highest_sold_quantity = df.groupby("fuel_type")["quantity_sold"].sum().idxmax()
print("\n Fuel type with highest Quantity sold")
print(fuel_type_with_highest_sold_quantity)

# Insight:
# E85_fuel recorded the highest quantity sold among all fuel types,
# indicating that it had the highest sales volume in the dataset.

#what is the total sales amount
print("\n Total Sales Amount")
print(f"{df['sales_amount'].sum():,.2f}")

# Insight
# The fuel station generated a total sales amount of ₦18,408,400 across
# all recorded transactions, representing the overall revenue generated during the period covered by the dataset.

# which fuel type performed worst based on sales mount
fuel_type_with_worst_performance = df.groupby("fuel_type")["sales_amount"].sum().idxmin()
print("\n Fuel type that performed worst based on sales amount")
print(fuel_type_with_worst_performance)

# Insight
# Regular Petrol performed worst based on sales amount, generating the
# lowest total sales among all the fuel types recorded in the dataset.

# what is the average quantity of fuel sold per day.
average_quantity_sold_per_day = df.groupby("day")["quantity_sold"].sum().mean()
print("\n Average Quantity of Fuel Sold Per Day")
print(f"{average_quantity_sold_per_day:,.2f}")

# Insight
# The fuel station sold an average of 2,135.71 units of fuel per day across
# the period covered by the dataset.

# which day generated the highest profit
day_with_highest_profit = df.groupby("day")["profit"].sum().idxmax()
print("\n Day with highest profit")
print(day_with_highest_profit)

# Insight
# Saturday recorded the highest profit among all the days in the dataset,
# making it the most profitable day for the fuel station.

# which pump sold the highest quantity of fuel
pump_with_highest_quantity_sold = df.groupby("pump_number")["quantity_sold"].sum().idxmax()
print("\n Pump that sold highest Quantity of fuel")
print(pump_with_highest_quantity_sold)

# Insight
# Pump 1 sold the highest quantity of fuel among all the pumps, making it
# the best-performing pump based on quantity sold.

# what is the total profit generated by the fuel station
print("\n Total profit generated by the fuel station")
print(f"{df['profit'].sum():,.2f}")

# Insight
# The fuel station generated a total profit of ₦1,741,700.00 from all recorded
# transactions during the period covered by the dataset.

# VISUALIZATION
# BARCHART
# plotting profit by fuel_type
profit_by_fuel = df.groupby("fuel_type")["profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(profit_by_fuel.index, profit_by_fuel.values)
plt.title("Total Profit by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Total Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("profit_by_fuel.png", dpi=300, bbox_inches="tight")
plt.show()

# BARCHART
# plotting sales_amount by day
sales_by_day = df.groupby("day")["sales_amount"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(sales_by_day.index, sales_by_day.values)
plt.title("Total Sales Amount by Day")
plt.xlabel("Day")
plt.ylabel("Total Sales Amount")
plt.tight_layout()
plt.savefig("sales_by_day.png", dpi=300, bbox_inches="tight")
plt.show()

# BARCHART
# plotting Revenue by pump
revenue_by_pump = df.groupby("pump_number")["sales_amount"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(revenue_by_pump.index, revenue_by_pump.values)
plt.title("Total Revenue by Pump Number")
plt.xlabel("Pump Number")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("revenue_by_pump.png", dpi=300, bbox_inches="tight")
plt.show()

# plotting quauntity by fuel
quantity_by_fuel = df.groupby("fuel_type")["quantity_sold"].sum().sort_values(ascending=True)
plt.figure(figsize=(12, 8))
plt.barh(quantity_by_fuel.index, quantity_by_fuel.values)
plt.title("Total Quantity Sold by Fuel Type")
plt.xlabel("Quantity Sold")
plt.ylabel("Fuel Type")
plt.tight_layout()
plt.savefig("quantity_by_fuel.png", dpi=300, bbox_inches="tight")
plt.show()

# plotting sales_amount by fuel type
sales_by_fuel = df.groupby("fuel_type")["sales_amount"].sum().sort_values(ascending=True)
plt.figure(figsize=(12, 8))
plt.barh(sales_by_fuel.index, sales_by_fuel.values)
plt.title("Total Sales Amount by Fuel Type")
plt.xlabel("Sales Amount")
plt.ylabel("Fuel Type")
plt.tight_layout()
plt.savefig("sales_by_fuel.png", dpi=300, bbox_inches="tight")
plt.show()

# plotting profit by day
profit_by_day = df.groupby("day")["profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(profit_by_day.index, profit_by_day.values)
plt.title("Total Profit by Day")
plt.xlabel("Day")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("profit_by_day.png", dpi=300, bbox_inches="tight")
plt.show()

# plotting quantity sold by pump number
quantity_by_pump = df.groupby("pump_number")["quantity_sold"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(quantity_by_pump.index, quantity_by_pump.values)
plt.title("Total Quantity Sold by Pump Number")
plt.xlabel("Pump Number")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("quantity_by_pump.png", dpi=300, bbox_inches="tight")
plt.show()

# KPI = Key Performance Indicator.
# A KPI is simply an important number that tells you how a business is performing.
# E.g Total Sales Amount → How much money came from sales?
# Total Profit → How much profit did the station make?
# Average Quantity Sold per Day → How much fuel is sold on an average day?
# A KPI Card is a visual that displays one important number in a very simple way.
# KPI is used to visualize important numbers while charts are used when theres comparison.

# adding the whole sales column to get the exact figure for our KPI
# KPI 1
total_sales = df["sales_amount"].sum()
print(f"\n Total Sales Amount: ₦{total_sales:,.2f}")

# KPI 2
avg_quantity_per_day = df.groupby("day")["quantity_sold"].sum().mean()
print(f"\n Average Quantity Sold per Day: {avg_quantity_per_day:,.2f}")

# KPI 3
total_profit = df["profit"].sum()
print(f"\n Total Profit: ₦{total_profit:,.2f}")
