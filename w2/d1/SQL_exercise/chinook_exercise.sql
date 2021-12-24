/* SQL Exercise
====================================================================
We will be working with database chinook.db
You can download it here: https://drive.google.com/file/d/0Bz9_0VdXvv9bWUtqM0NBYzhKZ3c/view?usp=sharing

 The Chinook Database is about an imaginary video and music store. Each track is stored using one of the digital formats and has a genre. The store has also some playlists, where a single track can be part of several playlists. Orders are recorded for customers, but are called invoices. Every customer is assigned a support employee, and Employees report to other employees.
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
Which artists did not make any albums at all?
 Include their names in your answer.
*/

SELECT Name FROM artists
WHERE ArtistId NOT IN 
    (SELECT ArtistId FROM albums GROUP BY ArtistId)

/* TASK II
Which artists recorded any tracks of the Latin genre?
*/

SELECT name FROM artists WHERE ArtistId IN
    (SELECT ArtistId FROM albums WHERE AlbumId IN
        (SELECT AlbumId FROM tracks WHERE GenreId IN
            (SELECT GenreId FROM genres WHERE Name = "Latin")
        )
    )

/* TASK III
Which video track has the longest length?
*/

SELECT tracks.Name, MAX(tracks.Milliseconds) FROM tracks 
JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId 
WHERE media_types.MediaTypeId = 3

/* TASK IV
Find the names of customers who live in the same city 
as the top employee (The one not managed by anyone).
*/

SELECT FirstName, LastName FROM customers WHERE City IN 
    (SELECT City FROM employees WHERE ReportsTo IS NULL)

/* TASK V
Find the managers of employees supporting 
Brazilian customers.
*/

SELECT EmployeeId FROM employees WHERE EmployeeId IN
    (SELECT ReportsTo FROM employees WHERE EmployeeId IN
        (SELECT SupportRepId FROM customers WHERE Country = "Brazil")
    )

/* TASK VI
Which playlists have no Latin tracks?
*/

SELECT Name FROM playlists WHERE PlaylistId NOT IN             /* Find playlists that are NOT IN the below list of playlists */
    (SELECT PlaylistId FROM playlist_track WHERE TrackId IN    /* Find playlists where these track ids show up */
        (SELECT TrackId FROM tracks WHERE GenreId IN           /* Find Track ids of latin songs */
            (SELECT GenreId FROM genres WHERE Name = "Latin"   /* Find 'latin' genreid*/
            )
        )
    ) 