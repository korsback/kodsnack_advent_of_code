create table T (c1 integer, c2 integer) strict;
.mode csv
.import 01_data.csv T
-- solution
select sum(abs(T1.c1-T2.c2))
from (
	select row_number() over (order by c1) as row, c1 from T
) T1
join (
    select row_number() over (order by c2) as row, c2 from T 
) T2
on T1.row = T2.row;
