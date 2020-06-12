select constraint_type,constraint_name from user_constraints
where table_name='STUDENT_INFO';
SELECT * FROM STUDENT_INFO;
SELECT * FROM TAB;
create table course(
       C_id number(3) primary key,
       C_NAME varchar2(20) not null,
       FEE Number(6) Not null,
       check (C_NAME in('Developer','Tester','Dba'))
);
insert into course(c_id,c_name,fee) values(101,"pratik",2000);
select * from course;
select constraint_type,constraint_name from user_constraints
where table_name='COURSE';

ALTER TABLE STUDENT_INFO(
       ADD (C_ID NUMBER(3) REFERENCE COURSE(C_ID)));
