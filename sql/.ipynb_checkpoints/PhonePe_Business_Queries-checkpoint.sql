USE PhonePeDB;

SELECT * FROM INFORMATION_SCHEMA.TABLES;

-- Business Question With Answers

-- Show All records
select * from Transactions;

-- What is the total transaction amount generated?
select sum(Amount) as total_amount from Transactions;

-- How many transactions were completed successfully vs failed?
 select Payment_Statusas Sucessful_Status from Transactions where Payment_Status = 'Successful';
