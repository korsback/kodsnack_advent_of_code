create table T (c1 text) strict;
.import 02_data.csv T

with

-- see 02_01.sql for explanations

-- discarded columns
D(discard) as (select 1 union all select discard + 1 from D where discard < 8),

L(row, discard, col, curr, prev) as (
	select
		T.rowid,
		D.discard,
		id,
		value,
		-- lag value by 1
		lag(value) over (partition by T.rowid, D.discard order by id) as prev
	from T, json_each("[" || T.c1 || "]")
	-- handle discards
	cross join D
	where D.discard != id
),

-- output
O(id) as (
	select row
	from L as L1
	where
	not exists (select 1 from L as L2 where (L1.row = L2.row and L1.discard = L2.discard) and (prev is not null and abs(prev - curr) > 3))
	and (
		not exists (select 1 from L as L2 where (L1.row = L2.row and L1.discard = L2.discard) and (prev is not null and prev <= curr))
		or
		not exists (select 1 from L as L2 where (L1.row = L2.row and L1.discard = L2.discard) and (prev is not null and prev >= curr))
    )
)

select count(distinct id) from O;
