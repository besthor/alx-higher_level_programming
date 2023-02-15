-- List all genres by their ratings
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
	FROM tv_genres
	JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	JOIN tv_show_ratings
	ON tv_shows.id = tv_show_ratings.show_id
	GROUP BY tv_genres.name
	ORDER BY rating DESC;
