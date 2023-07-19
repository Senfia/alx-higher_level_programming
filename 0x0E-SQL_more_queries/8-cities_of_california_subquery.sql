-- List all cities of California in ascending order
SELECT cities.id, name FROM cities WHERE state_id IN
(SELECT states.id 
FROM states 
WHERE name = 'California')
ORDER BY cities.id ASC;
