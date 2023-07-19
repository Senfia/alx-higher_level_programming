-- display all genres not linked to the tv show Dexter
SELECT DISTINCT tv_genres.`name`
FROM tv_genres
WHERE tv_genres.id not in
      (SELECT DISTINCT s.genre_id
      FROM tv_show_genres s
      INNER JOIN tv_shows u ON u.id = s.show_id
      INNER JOIN tv_genres v ON s.genre_id = v.id
      WHERE u.`title` = 'Dexter')
ORDER BY tv_genres.`name` ASC;
