-- selects all genres for Dexter
SELECT a.`name` 
FROM `tv_genres` AS a
INNER JOIN `tv_show_genres` AS s
ON a.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t
ON t.`id` = s.`show_id`
WHERE t.`title` = "Dexter"
ORDER BY a.`name`;
