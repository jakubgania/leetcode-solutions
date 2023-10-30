-- https://leetcode.com/problems/not-boring-movies/

SELECT
    id,
    movie,
    description,
    rating
FROM
    Cinema
WHERE
    description != 'boring'
AND
    mod (id, 2) != 0
ORDER BY
    rating
DESC