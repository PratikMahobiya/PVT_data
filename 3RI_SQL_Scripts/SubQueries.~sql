select * from tab;
select * from emp;
select * from dept;

// Subqueries..
type of subqueries:-
     1. single row subq-> = for only one value;
     2. multi-row subq-> in is used
     
//Single-row:-
select dname from dept where deptno=(select deptno from emp where empno=7369);
select * from emp where deptno=(select deptno from dept where dname='RESEARCH');

//multi-row:-
select * from emp where deptno in (select deptno from dept where dname='SALES' or dname='RESEARCH');
select * from emp where deptno in (select deptno from dept where dname in ('SALES','RESEARCH'));

//Question
select ename,job,sal from emp where sal=(select min(sal) from emp);

//Question
select deptno,job,min(sal) from emp group by deptno,job having min(sal)<(select min(sal) from emp where deptno=30);

//Co-Related Subqueries:-
select *  from emp where exists (select deptno from dept where deptno=30);

//Question
select * from dept where not exists (select deptno from emp where emp.deptno=dept.deptno);
//ulta Question
select * from dept where exists (select deptno from emp where emp.deptno=dept.deptno);

select * from emp where not exists (select deptno from dept where emp.deptno=dept.deptno);
