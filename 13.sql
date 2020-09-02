SELECT NAME FROM PEOPLE 
JOIN STARS ON STARS.PERSON_ID = PEOPLE.ID 
WHERE MOVIE_ID IN 
(SELECT MOVIE_ID FROM STARS
JOIN PEOPLE ON PEOPLE.ID = STARS.PERSON_ID
WHERE NAME = "Kevin Bacon" AND BIRTH = 1958)
AND NAME <> 'Kevin Bacon'
group by name,people.id;