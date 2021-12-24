/* SQL Exercise
====================================================================
We will be working with database imdb.db
You can download it here: https://drive.google.com/file/d/1E3KQDdGJs4a0i1RoYb8DEq0PFxCgI6cN/view?usp=sharing
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE

SELECT * FROM movie_distributors



--==================================================================
/* TASK I
 Find the id's of movies that have been distributed by “Universal Pictures”.
*/

SELECT movie_id FROM movie_distributors
WHERE distributor_id = (SELECT distributor_id 
                        FROM distributors
                        WHERE name = "Universal Pictures");

/* TASK II
 Find the name of the companies that distributed movies released in 2006.
*/

SELECT name FROM distributors WHERE distributor_id =
    (SELECT distributor_id FROM movie_distributors WHERE movie_id =
        (SELECT movie_id FROM movies WHERE year = 2006)
    );
/* TASK III
Find all pairs of movie titles released in the same year, after 2010.
hint: use self join on table movies.
*/

SELECT movies.title, pair.title, movies.year
FROM movies
JOIN movies pair ON movies.year = pair.year
WHERE movies.year > 2010;

/* TASK IV
 Find the names and movie titles of directors that 
 also acted in their movies.
*/

SELECT movies.title, people.name AS DirectorActor, roles.role FROM movies
JOIN directors USING (movie_id)
JOIN roles USING (person_id)
JOIN people USING (person_id);

/* TASK V
Find ALL movies realeased in 2011 and their aka titles.
hint: left join
*/

SELECT movies.title, aka_titles.title AS aka_title, note FROM movies
LEFT OUTER JOIN aka_titles USING (movie_id)
WHERE year = 2011;


/* TASK VI
Find ALL movies realeased in 1976 OR 1977 
and their composer's name.
*/

SELECT title, people.name AS composer  FROM movies
JOIN composers USING (movie_id)
JOIN people USING (person_id)
WHERE movies.year = 1976 OR movies.year = 1977;


/* TASK VII
Find the most popular movie genres.
*/

SELECT genres.label AS genre, COUNT(*) FROM movies
JOIN movie_genres USING (movie_id)
JOIN genres USING (genre_id)
GROUP BY genres.label
ORDER BY COUNT(*) DESC;

/* TASK VIII
Find the people that achieved the 10 highest average 
ratings for the movies they cinematographed.
*/

SELECT people.name AS cinematographer, movies.title, movies.rating 
FROM movies
JOIN cinematographers USING (movie_id)
JOIN people USING (person_id)
ORDER BY movies.rating DESC
LIMIT 10;

/* TASK IX
Find all countries which have produced at least one 
movie with a rating higher than 8.5.
hint: subquery
*/

SELECT countries.name FROM movie_countries
JOIN countries USING (country_id)
WHERE movie_id IN
    (SELECT movie_id FROM movies WHERE rating > 8.5)
GROUP BY countries.name;


/* TASK X
Find the highest-rated movie, and report its 
title, year, rating, and country. There
can be ties; if so, you should report for each of them.
*/

SELECT title, year, rating, name AS country 
FROM movies
JOIN movie_countries USING (movie_id)
JOIN countries USING (country_id)
ORDER BY rating DESC
LIMIT 1


/* STRETCH BONUS
Find the pairs of people that have directed at least 5 movies and whose 
carees do not overlap (i.e. The release year of a director's last movie is 
lower than the release year of another director's first movie).
*/
