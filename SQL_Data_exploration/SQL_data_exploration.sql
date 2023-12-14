-- DATA CLEANING IN SQL


-- creating a new database

Create database projects;
use projects;

-- then we imported the excel file using table data import wizard

SELECT * FROM housedata;

-- Standardizing the date column
UPDATE housedata
SET Saledate = STR_TO_DATE(Saledate,'%M %e,%Y');

-- Splitting the address column to individual columns(House number , city etc)
SELECT substring_index(propertyaddress,' ',1) as house_number,
substring_index(propertyaddress,' ',-1) as city,
TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(propertyaddress, ',', 1), ' ', -3)) AS street_name,
propertyaddress
FROM housedata;
 
-- Creating the house_number column (Text is used since it may contain blank values)
ALTER TABLE housedata
ADD house_number TEXT ;

UPDATE housedata
SET house_number = substring_index(propertyaddress,' ',1);

-- converting the text datatype to integers and converting blank to nulls
UPDATE housedata
SET house_number = NULLIF(CAST(house_number AS SIGNED), 0)
WHERE house_number REGEXP '^[0-9]+$';

-- creating the street address column and setting the values
ALTER TABLE housedata
ADD street_address VARCHAR(100);

UPDATE housedata
SET street_address = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(propertyaddress, ',', 1), ' ', -3));

-- creating the city column and setting the values
ALTER TABLE housedata
ADD city VARCHAR(50);

UPDATE housedata
SET city = substring_index(propertyaddress,' ',-1);


-- Replacing values in the soldasvacant column
-- first we are just finding the values and checking it


SELECT * FROM (SELECT soldasvacant,
CASE
WHEN soldasvacant = 'Y' THEN 'Yes'
WHEN soldasvacant ='N' THEN 'No'
END as newsold
FROM housedata)a
WHERE newsold IS NOT NULL;

-- now updating it
UPDATE housedata
SET soldasvacant = CASE
WHEN soldasvacant = 'Y' THEN 'Yes'
WHEN soldasvacant ='N' THEN 'No'
ELSE soldasvacant
END ;


SELECT * FROM housedata;

-- finding the details of houses having top 5 highest sale prices
SELECT * FROM housedata
ORDER BY Saleprice DESC
LIMIT 5;

-- finding the average salesprice of each landuse
SELECT Landuse,AVG(Saleprice) AS avg_price
FROM housedata
GROUP BY Landuse
ORDER BY avg_price DESC;

-- Umfortunately this dataset does not have a significant use of joins, hence let us stop here !!




