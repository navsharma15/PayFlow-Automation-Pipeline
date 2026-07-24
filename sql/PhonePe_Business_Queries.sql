USE PhonePeDB;

SELECT * FROM INFORMATION_SCHEMA.TABLES;

-- Business Question With Answers

-- 1 : Show All records

select * from Transactions;

-- 2 : What is the total transaction amount generated?

select sum(Amount) as total_amount from Transactions;

-- 3 : How many transactions were completed successfully vs failed?

 select count(Payment_Status) as Sucessfull_Status from Transactions where Payment_Status = 'Successful';

 -- 4 : What is the success percentage of all transactions?

select count(case when payment_status = 'successful' then 1 end) * 100 / count(transaction_id) as successful_percentage from Transactions;

-- 5 : Which recharge service type generates the highest revenue?

select top 1 service_type as service_type , sum(amount) from Transactions group by Service_Type order by sum(amount) desc; 

-- 6 : Which recharge service type has the highest number of transactions?

select top 1 service_type as recharge_service , count(transaction_id) as transactions from Transactions group by service_type order by count(transaction_id) desc;

-- 7 : What is the average recharge amount for each service type?

select service_type as service_type , avg(amount) as avg_recharge_amount from Transactions group by service_type order by avg(amount) desc;

-- 8 : Which users spend the most on recharges?

select top 1 user_id as user_id , sum(amount) as total_spend , service_type from Transactions group by user_id , Service_type order by sum(amount) desc;

-- 9 : How many unique users used the platform?

select count(distinct user_id) from Transactions;

-- 10 : Which dates recorded the highest transaction volume?

select top 5 transaction_date as date , count(transaction_id) as transactions from transactions group by transaction_date order by count(transaction_id) desc;

-- 11 : Which payment failure reason occurs most frequently?

select top 1 count(payment_status) as failed_count  , reason from transactions where payment_status = 'failed' group by reason order by count(payment_status) desc;

-- 12 : Which month generated the highest revenue?

select top 1 month(transaction_date) as month , sum(amount) as total_revenue from transactions group by month(transaction_date) order by total_revenue desc;


