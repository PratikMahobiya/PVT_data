create table customer(c_id number(3) constraint pk_c_id primary key,
                     c_name varchar2(20) constraint NN_c_NAME not null,
                     mobile number(10) constraint ue_MOBILE unique);
                     
select constraint_type,constraint_name from user_constraints
where table_name='CUSTOMER';

insert into customer(c_id,c_name,mobile)
values(101,'pratik',700068073);
insert into customer(c_id,c_name,mobile)
values(102,'sudeep',8518937674);
insert into customer(c_id,c_name,mobile)
values(103,'sumeet',9827198271);
insert into customer(c_id,c_name,mobile)
values(104,'tilesh',9307117548);
insert into customer(c_id,c_name,mobile)
values(105,'ashu',7999399856);

select * from customer;
truncate table customer;

delete from customer where c_id=105;
update customer set c_name='raju' where C_id=102;
update emp set mgr=1234 where deptno=20;
rollback;

select * from Tab;
select * from emp;
