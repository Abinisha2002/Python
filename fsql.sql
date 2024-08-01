show databases;
create database bank;
use bank;
create table v1(Name varchar(50),AadharNo int,PanNo int,Contact varchar(25),EmailId int,Address varchar(50));
insert into v1 values("abi",786,677,6777,4674,"ktm");
insert into v1 values("sumi",099,889,098,4433,"ts");
select * from v1;