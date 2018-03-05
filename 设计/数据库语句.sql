use crm;
create table employee(
	employee_Id int primary key auto_increment,
	employee_name varchar(10) not null,
	employee_phone varchar(20) unique not null,
	employee_auth tinyint not null default 1,
	employee_department varchar(10),
	employee_position varchar(10),
	employee_status varchar(10),
	remarks varchar(200),
	user_id varchar(20) unique,
	user_pw varchar(20),
	user_status varchar(10),
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
create table customer(
	customer_Id int primary key auto_increment,
	customer_name varchar(10) not null,
	customer_phone varchar(20) unique not null,
	customer_company varchar(10),
	customer_address varchar(10),
	customer_qq varchar(20) unique,
	customer_wechar varchar(10),
	customer_thestatus varchar(10),
	remarks varchar(200),
	__employee_Id int not null,
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
create table product(
	product_Id int primary key auto_increment,
	product_name varchar(10) not null,
	product_model varchar(10) not null,
	product_num int not null,
	product_price int not null,
	remarks varchar(200),
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
create table orderlist(
	id int primary key auto_increment,
	order_Id int not null,
	order_key varchar(10) not null,
	order_value varchar(10) not null,
	order_key_num int not null,
	remarks varchar(200),
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
CREATE TABLE colnamesmap(
  id int primary key auto_increment,
  colname varchar(20) not null UNIQUE ,
  chinese varchar(20)

)