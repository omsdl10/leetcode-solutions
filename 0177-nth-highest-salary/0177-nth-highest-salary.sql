CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        with ranked as(
            select 
            id ,salary,
            DENSE_RANK() over(
                order by salary desc
            ) as rnk
            from Employee
        )
        select salary
        from ranked
        where rnk=N
        Limit 1
  );
END