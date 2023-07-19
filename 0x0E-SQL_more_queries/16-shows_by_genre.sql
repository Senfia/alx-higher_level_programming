-- List all shows and the genre names associated to that show
SELECT t.`title`, a.`name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s
ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS a
ON s.`genre_id` = a.`id`
ORDER BY t.`title`, a.`name`;
