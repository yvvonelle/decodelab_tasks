# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# %%
df = pd.read_csv(r"cleaned_dataset.csv",parse_dates=["date"])

# %%
# Bar chart for  orders per product
orders_per_product = df['product'].value_counts().reset_index()
orders_per_product.columns = ['product', 'total_orders']
orders_per_product

# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=orders_per_product, x='product', y='total_orders',hue ='product', palette='viridis',legend =False)

plt.title('Total Orders per Product', fontsize=16)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.tight_layout()
plt.show()

# %%
# Bar chart for revenue per payment method
revenue_by_payment = df.groupby('payment_method')['total_price'].sum().reset_index()
revenue_by_payment.columns = ['payment_method', 'total_revenue']
revenue_by_payment = revenue_by_payment.sort_values('total_revenue', ascending=False)
revenue_by_payment

# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=revenue_by_payment, x='payment_method', y='total_revenue', 
            hue='payment_method', palette='magma', legend=False)

plt.title('Total Revenue per Payment Method', fontsize=16)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.show()

# %%
# Bar chart for average  order value per referral source
avg_by_referral = df.groupby('referral_source')['total_price'].mean().reset_index()
avg_by_referral.columns = ['referral_source', 'avg_order_value']
avg_by_referral = avg_by_referral.sort_values('avg_order_value', ascending=False)
avg_by_referral

# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_by_referral, x='avg_order_value', y='referral_source',
            hue='referral_source', palette='coolwarm', legend=False)

plt.title('Average Order Value by Referral Source', fontsize=16)
plt.xlabel('Average Order Value ($)', fontsize=12)
plt.ylabel('Referral Source', fontsize=12)
plt.tight_layout()
plt.show()

# %%
# Line chart for sales over time
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')
sales_over_time = df.groupby('year_month')['total_price'].sum().reset_index()
sales_over_time['year_month'] = sales_over_time['year_month'].astype(str)
sales_over_time

# %%
plt.figure(figsize=(14, 6))
plt.plot(sales_over_time['year_month'], sales_over_time['total_price'], 
         marker='o', color='steelblue', linewidth=2)

plt.title('Monthly Sales Revenue Over Time', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# %%
# Pie chart for order status breakdown
order_status = df['order_status'].value_counts().reset_index()
order_status.columns = ['order_status', 'count']
order_status

# %%
plt.figure(figsize=(8, 8))
plt.pie(order_status['count'], 
        labels=order_status['order_status'],
        autopct='%1.1f%%',
        colors=sns.color_palette('viridis', len(order_status)),
        startangle=140)

plt.title('Order Status Breakdown', fontsize=16)
plt.tight_layout()
plt.show()

# %%
# Bar chart for revenue by product
revenue_by_product = df.groupby('product')['total_price'].sum().reset_index()
revenue_by_product.columns = ['product', 'total_revenue']
revenue_by_product = revenue_by_product.sort_values('total_revenue', ascending=False)
revenue_by_product

# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=revenue_by_product, x='product', y='total_revenue',
            hue='product', palette='Blues_d', legend=False)

plt.title('Total Revenue by Product', fontsize=16)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.show()


