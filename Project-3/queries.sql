select * from cleaned_dataset;

-- where filtering showing only completed orders
select 
*
from cleaned_dataset 
where order_status = "DELIVERED";

-- order by to show top 10 highest value orders
select
order_id,
product,
total_price
from cleaned_dataset
order by total_price desc;

-- group by and count to show number of orders per product
select
count(*) as no_of_orders,
product
from cleaned_dataset
group by product
order by no_of_orders desc;

-- group by and sum to show revenue per payment method
select
payment_method,
sum(total_price) as total_revenue
from cleaned_dataset
group by payment_method
order by total_revenue desc;

-- group by and average to show the average  order value per referral source
select
referral_source,
avg(total_price) as average_order_value
from cleaned_dataset
group by referral_source
order by average_order_value desc;

-- having to show the orders exceed 100
select
product,
count(*) as orders
from cleaned_dataset
group by product
having orders > 100;
