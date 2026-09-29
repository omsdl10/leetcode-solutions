# Write your MySQL query statement below
select today.id
from weather yes
cross join weather today
where DATEDIFF(today.recordDate,yes.recordDate)=1
and today.temperature>yes.temperature