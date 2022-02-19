--drop table users;
--drop table accountdetail;
--drop table orderdetail;
--drop table billing;
--drop table dealdetails;
--drop table itemdetails;
--drop table orders;
--drop table paymenttype;
--drop table dealdescription;
--drop table deals;
--drop table employees;
--drop table price;
--drop table items;
--drop table branches;
--drop table cat_detail;
--drop table sizes;
--drop table category;

/*------------------------------CALIFORNIA PIZZA POINT OF SALE SCHEMA-----------------------------------------------------------------------*/
/*------------------------------------------CATEGORY----------------------------------------------------------------------------*/
create table category(
cat_ID number(4) not null constraint cat_catid_pk primary key,
cat_name varchar2(20) not null
);
/*--------------------------------------------SIZE--------------------------------------------*/
Create table sizes(
size_ID Number(4) constraint size_sizeid_pk Primary key,
size_name varchar2(10)
);
/*----------------------------Cat_details------------------------------------------------*/
create table cat_detail(
cat_ID number(4) not null,
size_ID number(4),
constraint cat_id_fk foreign key (cat_ID) references category(cat_ID),
constraint size_id_fk foreign key (size_ID) references sizes(size_ID)
);
/*---------------------------------------------BRANCHES----------------------------------------*/
create table branches(
branch_ID number(4) constraint branches_id_pk primary key,
loc varchar2(20) not null
);
/*----------------------------------------------ITEMs----------------------------------------------*/
create table items(
item_ID number(4) constraint item_itid_pk primary key,
item_name varchar2(40),
cat_ID number(4),
constraint catid_FK foreign key(cat_ID) references category(cat_ID) 
);

/*---------------------------------------Price----------------------*/
create table price(
item_id number(4) not null,
price number(4) not null,
size_id number(4),
constraint itemp_Fk foreign key (item_id) references items(item_id),
constraint sizes_price_FK foreign key (size_id) references sizes(size_id)
);
/*----------------------------------------------EMPLOYESS--------------------------------------------------*/
create table employees(
emp_ID number(4) constraint emp_empid_pk primary key,
ename varchar2(40) not null,
email varchar2(40) not null,
address varchar2(40) not null,
phone number(11) not null,
salary number(6) not null,
hiredate date default sysdate not null,
comm number(4),
branch_ID number(4) not null,
constraint employees_FK foreign key(branch_ID) references branches(branch_ID)
);

/*---------------------------------------------DEALS---------------------------------*/
create table deals(
deal_ID number(4) constraint deals_dealid_pk primary key,
dname varchar2(30) not null,
dprice number(4) not null
);
/*--------------------  -------------------------DEALDESCRIPTION---------------------------------*/
create table dealdescription(
deal_ID number(4)not null,
size_id number(4),
item_id number(4)not null,
constraint dealidx_Fk foreign key (deal_ID) references deals(deal_ID),
constraint sizeidx_Fk foreign key (size_ID) references sizes(size_ID),
constraint itemidx_Fk foreign key (item_ID) references items(item_ID)
);

/*---------------------------------------PAYMENT TYPE------------------------------*/
create table paymenttype(
paymenttype_ID number(4) constraint paymenttype_pk primary key,
paymenttype_name varchar2(20) not null
);
/*--------------------------------------------ORDER-----------------------------------------------------------------------*/
create table Orders(
order_ID number(4) constraint order_orderid_pk primary key,
orderdate Date Default SYSDATE,
emp_ID number(4) not null,
constraint empid_FK foreign key(emp_ID) references employees(emp_ID)
);
/*----------------------------------------------itemdetails--------------------------------------------------*/
create table itemdetails(
item_Qty number(3) not null,
item_ID number(4) not null,
Size_ID number(4),
Order_ID number(4) not null,
constraint itemsiid_FK foreign key(item_ID) references items(item_ID),
constraint order_ordid_FK foreign key(order_ID) references orders(order_ID), 
constraint sizes_id_FK foreign key(size_ID) references sizes(size_ID) 
);
/*---------------------------------------------DEALDETAILS---------------------------------*/

create table dealdetails(
deal_Qty number(4) not null,
deal_ID number(4)not null,
Order_ID number(4) not null,
constraint ordersid_FK foreign key(order_ID) references orders(order_ID), 
constraint dealsid_Fk foreign key (deal_ID) references deals(deal_ID)

);
/*----------------------------------------------BILLING------------------------------*/
create table billing(
reciept_id number(4) constraint bill_receipt_pk primary key,
order_ID number(4),
amount number(5),
paymenttype_ID number(4),
constraint billing_orders_FK foreign key(order_ID )references orders(order_ID),
constraint billing_pay_FK foreign key(paymenttype_ID) references paymenttype(paymenttype_ID)
);

/*------------------------------------------orderdetail----------------------------------------*/
create table orderdetail(
order_ID number(4),
branch_id number(4),
reciept_id number(4),
constraint order_ids_fk foreign key (order_id) references Orders(order_id),
constraint branchesid_fk foreign key (branch_id) references branches(branch_id),
constraint reciept_ids_fk foreign key (reciept_id) references billing(reciept_id)
);
/*-------------------------------------ACCOUNT DETAIL------------------------------*/
create table accountdetail(
accountno number(16) constraint cd_accno_pk primary key,
accountname varchar2(40),
reciept_id number(4),
constraint recieptid_fk foreign key (reciept_id) references billing(reciept_id)
);

create table USERS (
U_ID Number(4) primary key,
Username Varchar2(40),
Passwords varchar2(40),
Emp_id number(4),
constraint em_fk foreign key (emp_id) references employees(emp_id)
);


commit;