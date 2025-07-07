
Below are the SQL queries I have executed in my project Retail Perfomance:


# distinct rows within the dataset

select distinct * from unified_data;



# SQL query you can run in Amazon Athena to merge the two tables (month_05 and sales_data_csv) and create a unified view called unified_data.

CREATE OR REPLACE VIEW unified_data AS
SELECT *
FROM month_05

UNION ALL

SELECT *
FROM sales_data_csv;


# Frequency distribution of branch

SELECT branch, COUNT(*) AS total
FROM unified_data
GROUP BY branch
ORDER BY total DESC;


# Detect duplicates by invoiceid

SELECT invoiceid, COUNT(*) AS count
FROM unified_data
GROUP BY invoiceid
HAVING COUNT(*) > 1;


# Monthly trend (if you have a date or month column)
SELECT month, SUM(total) AS total_sales
FROM unified_data
GROUP BY month
ORDER BY month;


#  Total sales by branch
SELECT branch, SUM(total) AS total_sales
FROM unified_data
GROUP BY branch
ORDER BY total_sales DESC;


# Rows with negative or zero quantity

SELECT *
FROM unified_data
WHERE quantity <= 0;





# This will return all rows where gender has invalid, misspelled, or unexpected values like fsdf, prap, rear, etc.,

SELECT *
FROM unified_data
WHERE (gender NOT IN ('Male', 'Female', 'Others') OR gender IS NULL OR TRIM(gender) = '');



# Clean dataset: Keep only valid rows, You can invert the filters and create a cleaned view:

CREATE OR REPLACE VIEW cleaned_data AS
SELECT *
FROM unified_data
WHERE gender IN ('Male', 'Female', 'Others')
  AND branch IN ('A', 'B', 'C', 'Main')
  AND city IN ('Sydney', 'Perth', 'Pokhara', 'Yangon')
  AND customertype IN ('Member', 'Normal', 'Regular')
  AND quantity > 0
  AND unitprice > 0;


#Create a cleaned table (CTAS – Create Table As Select), Write the cleaned data back into a new S3 location as a proper table:

CREATE TABLE cleaned_unified_data
WITH (
  format = 'Parquet',
  external_location = 's3://data-lake/cleaned_unified_data/'
) AS
SELECT *
FROM unified_data
WHERE gender IN ('Male', 'Female', 'Others')
  AND branch IN ('A', 'B', 'C', 'Main')
  AND city IN ('Sydney', 'Perth', 'Pokhara', 'Yangon')
  AND customertype IN ('Member', 'Normal', 'Regular')
  AND quantity > 0
  AND unitprice > 0;


# Drop Table or View
DROP TABLE cleaned_unified_data;
or
DROP VIEW cleaned_unified_view;


# If your underlying S3 files changed (like new partitions were added), I can repair the table metadata:

MSCK REPAIR TABLE cleaned_unified_data;


