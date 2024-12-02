create table T (c1 text) strict;
.import 02_data.csv T

with

-- we index the data using row and column
-- i.e. for 3 and 5 in the following data
--
--  _,_,_,_
--  3,5,_,_
--  _,_,_,_
--
-- we produce a table such as
--
--  row col curr prev
--  2   1   3    NULL
--  2   2   5    3
--
L(row, col, curr, prev) as (
	select
		T.rowid,
		id,
		value,
		-- lag value by 1
		lag(value) over (partition by T.rowid order by id)
	from T, json_each("[" || T.c1 || "]")
),

O(row) as (
	select row
	from L as L1
	where
	-- there's no way to express ∀ in sql, so we express the conditions using ¬∃, i.e.
	-- ¬∃x : abs(prev(x)-x) > 3 ∧ ((¬∃x : prev(x) <= x) ∨ (¬∃x : prev(x) >= x))
	not exists (select 1 from L as L2 where (L1.row = L2.row) and (prev is not null and abs(prev - curr) > 3))
	and (
		not exists (select 1 from L as L2 where (L1.row = L2.row) and (prev is not null and prev <= curr))
		or
		not exists (select 1 from L as L2 where (L1.row = L2.row) and (prev is not null and prev >= curr))
	)
)

select count(distinct row) from O;
