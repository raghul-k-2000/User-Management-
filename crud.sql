use crud;
create table users(
ID int not null auto_increment primary key,
NAME varchar(50),
AGE int,
CITY varchar(50)
);

select * from users;
insert into users(NAME,AGE,CITY) values('Ram',26,'Chennai');
