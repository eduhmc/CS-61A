----------
-- Dogs -- DEMO1
----------

-- Parents
CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

-- Fur
CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur UNION
  SELECT "barack"         , "short"       UNION
  SELECT "clinton"        , "long"        UNION
  SELECT "delano"         , "long"        UNION
  SELECT "eisenhower"     , "short"       UNION
  SELECT "fillmore"       , "curly"       UNION
  SELECT "grover"         , "short"       UNION
  SELECT "herbert"        , "curly";

-- All pairs of rows of dogs with rows of parents
SELECT * FROM parents, dogs;

-- All rows that have matched child and name
SELECT * FROM parents, dogs WHERE child = name;

-- All rows that have matched child and name and the child's fur is curly
SELECT * FROM parents, dogs WHERE child = name AND fur = "curly";

-- Parents of curly dogs
SELECT parent FROM parents, dogs WHERE child = name AND fur = "curly";

-- DEMO2

-- Siblings
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Grandparents
CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS granpup
    FROM parents AS a, parents AS b
    WHERE a.child = b.parent;

-- Grandogs with the same fur AS their granpups
SELECT grandog, granpup, c.fur FROM grandparents, dogs AS c, dogs AS d
  WHERE grandog = c.name AND
        granpup = d.name AND
        c.fur = d.fur;

------------
-- Cities -- DEMO3
------------

CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42,              71,              "Cambridge"        UNION
  SELECT 45,              93,              "Minneapolis"      UNION
  SELECT 33,             117,              "San Diego"        UNION
  SELECT 26,              80,              "Miami"            UNION
  SELECT 90,               0,              "North Pole";

SELECT name FROM cities WHERE latitude > 43

CREATE TABLE cold AS
  SELECT name FROM cities WHERE latitude > 43 UNION
  SELECT "Chicago";

SELECT name, "is cold!" FROM cold;

CREATE TABLE distances AS
  SELECT a.name AS first, b.name AS second,
         69*(a.latitude-b.latitude) AS distance
         FROM cities AS a, cities AS b
         WHERE a.name != b.name
         ORDER BY a.longitude;

SELECT second FROM distances WHERE first="Minneapolis" ORDER BY -distance;

---------------
-- Sentences -- DEMO4
---------------

CREATE TABLE nouns AS
  SELECT "the dog" AS phrase UNION
  SELECT "the cat"           UNION
  SELECT "the bird";

SELECT subject.phrase || " chased " || object.phrase AS "chasing all around"
       FROM nouns AS subject, nouns AS object
       WHERE subject.phrase != object.phrase;

CREATE TABLE ands AS
  SELECT phrase FROM nouns UNION
  SELECT first.phrase || " AND " || second.phrase
         FROM nouns AS first, nouns AS second
         WHERE first.phrase != second.phrase;

SELECT subject.phrase || " chased " || object.phrase
       FROM ands AS subject, ands AS object
       WHERE subject.phrase != object.phrase;

SELECT a.name AS "Dog 1", b.name AS "Dog 2", c.name AS "Dog 3" 
       FROM dogs AS a, dogs as b, dogs as c 
       WHERE a.fur == b.fur and b.fur == c.fur and a.name > b.name and b.name > c.name

SELECT 1 as N union select 2 union select 3;
       