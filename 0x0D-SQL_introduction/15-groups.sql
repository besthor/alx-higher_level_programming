-- List by occurences of scores
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
