-- List all comedy shows
SELECT t.`title`
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS s
ON t.`id` = s.`show_id`
INNER JOIN `tv_genres` AS a
ON a.`id` = s.`genre_id`
WHERE a.`name` = "Comedy"
ORDER BY t.`title`;
