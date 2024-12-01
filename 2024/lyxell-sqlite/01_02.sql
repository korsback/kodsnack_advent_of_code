create table T (c1 integer, c2 integer) strict;
.mode csv
.import 01_data.csv T
-- solution
select sum(T.c1*C.occ) from (
	select c2, count(*) as occ
    from T
    group by c2
) C
join T on C.c2 = T.c1;
