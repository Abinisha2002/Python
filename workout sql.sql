create database student;
use student;
show tables;
create table d2(roll_number int primary key,student_name varchar(5),mark1 int,result varchar(5));
insert into d2 values(1,"abis",50,"pass");
insert into d2 values(2,"sumi",90,"pass");
insert into d2 values(3,"kavi",80,"pass");
insert into d2 values(4,"indhu",20,"fail");
select * from d2;
