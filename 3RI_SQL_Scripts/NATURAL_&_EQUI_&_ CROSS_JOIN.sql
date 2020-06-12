select * from tab;
select * from emp;
select * from dept;

//Natural Join:-
select empno,ename,dname,loc from emp natural join dept;
select ename,job,deptno,dname from emp natural join dept;
  
//Equii Join:-
select * from emp,dept where emp.deptno=dept.deptno and dept.dname='RESEARCH';

//Cross join:-
select ename,dname from emp cross join dept;
