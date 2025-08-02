#Forecast till July 2027 (24 months from now)
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Step 1: Load and clean dataset
dataset.columns = dataset.columns.str.strip().str.lower()  # make all lowercase
df = dataset.copy()

# Check column names
print(df.columns)  # <- This helps in debugging

# Fix column names
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date', 'total'])
    df = df.rename(columns={'date': 'ds', 'total': 'y'})
else:
    raise KeyError("Column 'date' not found")

# Step 2: Prophet model
model = Prophet()
model.fit(df)

# Step 3: Forecast till July 2027 (24 months from now)
future = model.make_future_dataframe(periods=24, freq='M')
forecast = model.predict(future)

# Step 4: Plot
fig = model.plot(forecast)
plt.title("Forecast: Total Sales Until July 2027")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# This script implements a predictive modelling approach using Facebook’s Prophet library to forecast total sales until July 2027. Integrated within Power BI, it enhances business intelligence dashboards with future projections based on historical data.
# ✅ Key Workflow:
# Data Preprocessing
# Cleans and standardizes column names.
# Converts date to datetime.
# Renames date → ds, and total → y to match Prophet’s input format.
# Model Training
# Fits the Prophet time series model on the sales data.
# Future Forecasting
# Generates a 24-month monthly forecast extending to July 2027.
# Visualization
# Plots historical and forecasted values with 95% confidence intervals using matplotlib.