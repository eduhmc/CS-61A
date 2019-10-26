-- DEMO1

create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;

select max(legs) from animals;

select sum(weight) from animals;

select max(legs - weight) + 5 from animals;

select min(legs), max(weight) from animals;

select min(legs), max(weight) from animals where kind <> "t-rex";

select min(legs) + max(weight) from animals where kind <> "t-rex";

select avg(legs) from animals;

-- how many rows are there?
select count(legs) from animals;

select count(*) from animals;

select count(distinct legs) from animals;

select sum(distinct legs) from animals;


select kind, max(weight) from animals;

select kind, max(legs) from animals;

select kind, avg(weight) from animals;

select kind, min(kind), legs, weight from animals;


-- Discussion solutions

-- select kind from animals where legs=max(legs);

create table m as select max(legs) as maxlegs from animals;

select kind from animals, m where legs=maxlegs;

select kind from animals, (select max(legs) as maxlegs from animals) where legs=maxlegs;

select kind from animals where legs = (select max(legs) from animals);


select legs from animals group by legs;

select legs, count(*) from animals group by legs;

select legs, max(weight) from animals group by legs;

select legs, weight, count(*) from animals group by legs, weight;

select weight/legs, count(*) from animals group by weight/legs;

select weight/legs, max(kind) from animals group by weight/legs;

select weight/legs, count(*) from animals group by weight/legs having count(*)>1;



-- Discussion solutions

select max(a.legs-b.legs) from animals as a, animals as b where a.weight=b.weight;

select max(legs)-min(legs) as diff from animals group by weight order by -diff limit 1;

