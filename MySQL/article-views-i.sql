-- https://leetcode.com/problems/article-views-i/

SELECT
    DISTINCT author_id as id
FROM
    views
WHERE
    author_id = viewer_id
ORDER BY
    author_id