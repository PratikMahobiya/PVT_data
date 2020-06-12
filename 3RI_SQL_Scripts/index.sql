select * from tab;
select * from emp where sal>1200 and deptno=30;
select * from emp where sal>1200;
select * from emp;

create index s_index on emp(sal);
create index s_d_index on emp(sal,deptno);
create bitmap index bt_indx on emp(xyz);
create index fun_index on emp(lower(ename));
create index indx_rev_sal on emp(sal) reverse;


drop index s_index;
drop index s_d_index;
drop index bt_indx;
drop index fun_index;
drop index indx_rev_empno;

