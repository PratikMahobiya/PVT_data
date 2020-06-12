select * from tab;
select * from customer;
create sequence sequence_no start with 101 increment by 1;

select sequence_no.nextval from dual;
select sequence_no.currval from dual;
select * from dual;

insert into customer values(sequence_no.nextval,'rohit',7519536482);

drop sequence sequence_no;
rollback;
