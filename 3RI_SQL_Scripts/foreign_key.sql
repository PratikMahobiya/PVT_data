insert into customer(c_id,c_name,mobile)
values(106,'sham',7999456987);
select * from customer;
commit;
rollback;

create table product(p_id number(3) primary key,
                    p_name varchar2(10) not null,
                    p_cost number(6),
                    c_id number(3) references customer(c_id));
        
select * from product;

insert into product
values(201,'car',1500,103);
insert into product
values(204,'paper',1200,103);
insert into product
values(208,'chair',2000,103);
insert into product
values(206,'pen',1800,104);
insert into product
values(202,'watch',2600,101);
insert into product
values(203,'chair',2000,104);
insert into product
values(205,'cards',500,103);

select * from product;
select * from tab;
select * from student;

select constraint_type,constraint_name from user_constraints
where table_name='STUDENT';

create table student(s_id number(3),s_name varchar2(20));

alter table student
add constraint PK_s_id primary key(s_id);

alter table student
add constraint chk_s_id
check (s_id in (101,102,103));

insert into student
values(103,'fridge');

insert into student
values(103,'mobile');

select * from student;

alter table student
drop constraint chk_s_id;
