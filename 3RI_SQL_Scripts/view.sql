create view emp_deptno_vw as select * from employees where department_id=100;
create view emp_deptno as select * from departments where department_id=100;
select * from tab;
select * from employees;
select * from departments;
select * from emp_deptno_vw;
select * from emp_deptno;

insert into emp_deptno_vw(employee_id,LAST_NAME,email,hire_date,job_id,DEPARTMENT_ID)
values(200,mahobiya,p@gmail.com,'12-02-2020',Halwai,100);

insert into emp_deptno
values(303,'halwai',200,1700);

select constraint_type,constraint_name from user_constraints
where table_name='DEPARTMENTS';

create or replace view emp_deptno_vw as select employee_id e_id, email "EmAiL_ID" from employees where department_id=100;

