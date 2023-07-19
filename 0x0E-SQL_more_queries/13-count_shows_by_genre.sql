-- List all genres and how many of times they are referenced

SELECT a.`name` AS `genre`,
COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS a
INNER JOIN `tv_show_genres` AS s
ON a.`id` = s.`genre_id`
GROUP BY a.`name`
ORDER BY `number_of_shows` DESC;
