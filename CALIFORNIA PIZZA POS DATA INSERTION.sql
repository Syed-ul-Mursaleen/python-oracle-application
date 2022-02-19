/*---------------------branches branches---------------------*/
insert into branches(branch_ID,loc) values(11,'Gulshan e Iqbal');
insert into branches(branch_ID,loc) values(12,'Clifton');
insert into branches(branch_ID,loc) values(13,'Nazimabad');
insert into branches(branch_ID,loc) values(14,'Garden West');

/*----------------------------------------employee insertion--------------------------------------------------------------*/
insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1112,'okasha','okashasameer0@gmail.com','House-123 Gulberg 17',03404799559,30000,to_date('10-mar-2015','dd-mon-yy'),400,11);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1113,'zain','zain@gmail.com','House 12 Johar ',03404799559,34000,to_date('19-apr-15','dd-mon-yy'),400,14);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1114,'mursaleen','mursaleen@gmail.com','flat 105,Garden West',03304799559,32000,to_date('21-jun-2016','dd-mon-yy'),null,11);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1115,'savera','syedasavera@gmail.com','Gulshan 13D1',03404119559,40000,to_date('21-jun-2016','dd-mon-yy'),100,11);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1116,'usama','usama34@gmail.com','Flat 222, Korangi',03404794459,30000,to_date('21-aug-2016','dd-mon-yy'),null,12);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1117,'ahmed','asad12@gmail.com','R-302/17',03244743912,27000,to_date('21-jul-2017','dd-mon-yy'),1900,12);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1118,'ubaid','ubaid34@gmail.com','flat 444, Nazimabad',03244743966,30000,to_date('28-jan-2017','dd-mon-yy'),800,12);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1119,'asad','asad234@gmail.com','Flat-190, Kharadar',03244743990,27000,to_date('21-jul-2017','dd-mon-yy'),null,13);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1120,'huzaifa','huzaifa@gmail.com','House 144,Shah Faisal Town',03244743521,30000,to_date('01-feb-2018','dd-mon-yy'),500,13);

insert into employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) 
values(1121,'rizwan','riz12@gmail.com','R-7892/2 Gizri',03244346912,30000,to_date('21-dec-2019','dd-mon-yy'),230,14);

/*------------------sizes insertion--------------------*/
insert into sizes(size_id,size_name) values(1,'small');
insert into sizes(size_id,size_name) values(2,'medium');
insert into sizes(size_id,size_name) values(3,'large');
insert into sizes(size_id,size_name) values(4,'245g');
insert into sizes(size_id,size_name) values(5,'475g');

/*------------------category---------------------*/
insert into category(cat_id,cat_name) values(10,'Pizza');
insert into category(cat_id,cat_name) values(20,'Special');
insert into category(cat_id,cat_name) values(30,'Beverages');
insert into category(cat_id,cat_name) values(40,'Desserts');
insert into category(cat_id,cat_name) values(50,'Appetizer');
insert into category(cat_id,cat_name) values(60,'Icecream');
/*---------------------cat_details---------------------*/
insert into cat_detail(cat_id,size_id) values(10,1);
insert into cat_detail(cat_id,size_id) values(10,2);
insert into cat_detail(cat_id,size_id) values(10,3);
insert into cat_detail(cat_id,size_id) values(20,1);
insert into cat_detail(cat_id,size_id) values(20,2);
insert into cat_detail(cat_id,size_id) values(20,3);
insert into cat_detail(cat_id,size_id) values(30,1);
insert into cat_detail(cat_id,size_id) values(30,2);
insert into cat_detail(cat_id,size_id) values(30,3);
insert into cat_detail(cat_id,size_id) values(60,4);
insert into cat_detail(cat_id,size_id) values(60,5);
/*--------------------paymenttype-----------------------------*/
insert into paymenttype(paymenttype_id,paymenttype_name)values(111,'cash');
insert into paymenttype(paymenttype_id,paymenttype_name)values(112,'card');

/*------------------orders----------------------*/
insert into orders(order_id,orderdate,emp_id) values(111,'21-jan-22',1112);
insert into orders(order_id,orderdate,emp_id) values(112,'1-feb-22',1112);
insert into orders(order_id,orderdate,emp_id) values(113,'2-feb-22',1112);
insert into orders(order_id,orderdate,emp_id) values(114,'12-mar-22',1113);
insert into orders(order_id,orderdate,emp_id) values(115,'12-mar-22',1113);
insert into orders(order_id,orderdate,emp_id) values(116,'23-mar-22',1114);
insert into orders(order_id,orderdate,emp_id) values(117,'3-apr-22',1115);
insert into orders(order_id,orderdate,emp_id) values(118,'3-apr-22',1116);
insert into orders(order_id,orderdate,emp_id) values(119,'3-apr-22',1116);
insert into orders(order_id,orderdate,emp_id) values(120,'14-may-22',1117);
insert into orders(order_id,orderdate,emp_id) values(121,'14-may-22',1118);
insert into orders(order_id,orderdate,emp_id) values(122,'14-may-22',1120);


/*-------------------items-----------------*/
insert into items(item_id,item_name,cat_id) values(1,'super supreme',10);
Insert into items(item_id,item_name,cat_id) values(2,'chicken supreme',10);
Insert into items(item_id,item_name,cat_id) values(3,'chicken fajita',10);
Insert into items(item_id,item_name,cat_id) values(4,'Ranch pizza',10);
Insert into items(item_id,item_name,cat_id) values(5,'mexican treat',10);
Insert into items(item_id,item_name,cat_id) values(6,'chicken tikka',10);
Insert into items(item_id,item_name,cat_id) values(7,'chipotle pizza',10);
Insert into items(item_id,item_name,cat_id) values(8,'pizza fries',20);
Insert into items(item_id,item_name,cat_id) values(9,'chicken lasagnia',20);
Insert into items(item_id,item_name,cat_id) values(10,'Cheesy Fries',20);
Insert into items(item_id,item_name,cat_id) values(11,'chicken Pasta',20);
Insert into items(item_id,item_name,cat_id) values(12,'Pepsi',30);
Insert into items(item_id,item_name,cat_id) values(13,'7up',30);

Insert into items(item_id,item_name,cat_id) values(14,'Mountain Dew',30);
Insert into items(item_id,item_name,cat_id) values(15,'Brownie',40);
Insert into items(item_id,item_name,cat_id) values(16,'Lava Cake',40);
Insert into items(item_id,item_name,cat_id) values(17,'Crispy Wings',50);
Insert into items(item_id,item_name,cat_id) values(18,'Chicken Wrap',50);
Insert into items(item_id,item_name,cat_id) values(19,'Salad',50);
Insert into items(item_id,item_name,cat_id) values(20,'Crispy Mayo Fries',50);
Insert into items(item_id,item_name,cat_id) values(21,'Garlic Bread',50);
Insert into items(item_id,item_name,cat_id) values(22,'Vanilla',60);
Insert into items(item_id,item_name,cat_id) values(23,'Chocolate',60);
Insert into items(item_id,item_name,cat_id) values(24,'Strawberry',60);
Insert into items(item_id,item_name,cat_id) values(25,'Mango',60);



/*-----------deals--------------------*/
insert into  deals(deal_id,dname,dprice) values(121,'Meat Feista',2099);
insert into  deals(deal_id,dname,dprice) values(122,'Cheese Feista',1999);
insert into  deals(deal_id,dname,dprice) values(123,'Three-O-Treat',2399);
insert into  deals(deal_id,dname,dprice) values(124,'Mid-Night Blast',1599);
insert into  deals(deal_id,dname,dprice) values(125,'Kid Special',999);
insert into  deals(deal_id,dname,dprice) values(126,'Snow Cheese storm',1799);

/*-------------------deal description-----------------*/
insert into dealdescription(deal_id,size_id,item_id) values(121,2,7);
insert into dealdescription(deal_id,size_id,item_id) values(121,2,12);
insert into dealdescription(deal_id,size_id,item_id) values(122,1,5);
insert into dealdescription(deal_id,size_id,item_id) values(122,1,10);
insert into dealdescription(deal_id,size_id,item_id) values(122,1,13);
insert into dealdescription(deal_id,size_id,item_id) values(123,2,2);
insert into dealdescription(deal_id,size_id,item_id) values(123,2,4);
insert into dealdescription(deal_id,size_id,item_id) values(123,2,6);
insert into dealdescription(deal_id,size_id,item_id) values(123,3,12);
insert into dealdescription(deal_id,size_id,item_id) values(124,3,6);
insert into dealdescription(deal_id,size_id,item_id) values(124,1,5);
insert into dealdescription(deal_id,size_id,item_id) values(124,1,3);
insert into dealdescription(deal_id,size_id,item_id) values(125,1,1);
insert into dealdescription(deal_id,size_id,item_id) values(125,1,2);
insert into dealdescription(deal_id,size_id,item_id) values(125,1,3);
insert into dealdescription(deal_id,size_id,item_id) values(126,3,9);
insert into dealdescription(deal_id,size_id,item_id) values(126,2,8);
insert into dealdescription(deal_id,size_id,item_id) values(126,1,13);

/*-------------------deal detail-----------------*/
insert into dealdetails(deal_qty,deal_id,order_id) values(1,122,114);
insert into dealdetails(deal_qty,deal_id,order_id) values(2,122,116);
insert into dealdetails(deal_qty,deal_id,order_id) values(1,124,113);
insert into dealdetails(deal_qty,deal_id,order_id) values(2,125,113);
insert into dealdetails(deal_qty,deal_id,order_id) values(1,126,115);

/*-------------------items detail-----------------*/

insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,1,2,111);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,1,2,112);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(2,8,2,112);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,4,3,113);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,7,2,113);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(2,3,2,114);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,5,2,115);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,5,2,116);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(2,1,2,116);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,2,2,117);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(2,6,1,118);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(2,8,2,119);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(3,8,3,120);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(4,8,2,121);
insert into itemdetails(item_qty,item_id,size_id,order_id) values(1,8,1,122);

/*-------------------Price-----------------*/
insert into price(item_id,price,size_id) values(1,899,1);
insert into price(item_id,price,size_id) values(1,1200,2);
insert into price(item_id,price,size_id) values(1,2000,3);
insert into price(item_id,price,size_id) values(2,950,1);
insert into price(item_id,price,size_id) values(2,1300,2);
insert into price(item_id,price,size_id) values(2,2100,3);
insert into price(item_id,price,size_id) values(3,899,1);
insert into price(item_id,price,size_id) values(3,1400,2);
insert into price(item_id,price,size_id) values(3,2100,3);
insert into price(item_id,price,size_id) values(4,899,1);
insert into price(item_id,price,size_id) values(4,1300,2);
insert into price(item_id,price,size_id) values(4,1900,3);
insert into price(item_id,price,size_id) values(5,999,1);
insert into price(item_id,price,size_id) values(5,1450,2);
insert into price(item_id,price,size_id) values(5,2150,3);
insert into price(item_id,price,size_id) values(6,999,1);
insert into price(item_id,price,size_id) values(6,1350,2);
insert into price(item_id,price,size_id) values(6,1850,3);
insert into price(item_id,price,size_id) values(7,1099,1);
insert into price(item_id,price,size_id) values(7,1600,2);
insert into price(item_id,price,size_id) values(7,2150,3);
insert into price(item_id,price,size_id) values(8,350,1);
insert into price(item_id,price,size_id) values(8,670,2);
insert into price(item_id,price,size_id) values(8,1250,3);
insert into price(item_id,price,size_id) values(9,650,1);
insert into price(item_id,price,size_id) values(9,1350,2);
insert into price(item_id,price,size_id) values(9,2000,3);
insert into price(item_id,price,size_id) values(10,320,1);
insert into price(item_id,price,size_id) values(10,570,2);
insert into price(item_id,price,size_id) values(10,850,3);
insert into price(item_id,price,size_id) values(11,1199,1);
insert into price(item_id,price,size_id) values(11,1750,2);
insert into price(item_id,price,size_id) values(11,2300,3);
insert into price(item_id,price,size_id) values(12,70,1);
insert into price(item_id,price,size_id) values(12,120,2);
insert into price(item_id,price,size_id) values(12,175,3);
insert into price(item_id,price,size_id) values(13,70,1);
insert into price(item_id,price,size_id) values(13,120,2);
insert into price(item_id,price,size_id) values(13,175,3);
insert into price(item_id,price,size_id) values(14,70,1);
insert into price(item_id,price,size_id) values(14,120,2);
insert into price(item_id,price,size_id) values(14,175,3);

insert into price(item_id,price,size_id) values(15,120,Null);
insert into price(item_id,price,size_id) values(16,120,Null);
insert into price(item_id,price,size_id) values(17,300,Null);
insert into price(item_id,price,size_id) values(18,200,Null);
insert into price(item_id,price,size_id) values(19,120,Null);
insert into price(item_id,price,size_id) values(20,200,Null);
insert into price(item_id,price,size_id) values(21,300,Null);

insert into price(item_id,price,size_id) values(22,420,4);
insert into price(item_id,price,size_id) values(22,660,5);
insert into price(item_id,price,size_id) values(23,420,4);
insert into price(item_id,price,size_id) values(23,660,5);
insert into price(item_id,price,size_id) values(24,420,4);
insert into price(item_id,price,size_id) values(24,660,5);
insert into price(item_id,price,size_id) values(25,420,4);
insert into price(item_id,price,size_id) values(25,660,5);
commit;


/*-------------------BILLING-----------------*/
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2000,111,1200,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2001,112,2540,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2002,113,7097,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2003,114,4899,112);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2004,115,3249,112);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2005,116,5448,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2006,117,1300,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2007,118,1998,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2008,119,1340,112);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2009,120,3750,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2010,121,2680,111);
insert into billing(reciept_id,order_id,amount,paymenttype_id) values(2011,122,350,111);

/*-------------orderdetails-------------------*/
insert into orderdetail(order_id,branch_id,reciept_id) values(111,11,2000);
insert into orderdetail(order_id,branch_id,reciept_id) values(112,11,2001);
insert into orderdetail(order_id,branch_id,reciept_id) values(113,11,2002);
insert into orderdetail(order_id,branch_id,reciept_id) values(114,14,2003);
insert into orderdetail(order_id,branch_id,reciept_id) values(115,14,2004);
insert into orderdetail(order_id,branch_id,reciept_id) values(116,11,2005);
insert into orderdetail(order_id,branch_id,reciept_id) values(117,11,2006);
insert into orderdetail(order_id,branch_id,reciept_id) values(118,12,2007);
insert into orderdetail(order_id,branch_id,reciept_id) values(119,12,2008);
insert into orderdetail(order_id,branch_id,reciept_id) values(120,12,2009);
insert into orderdetail(order_id,branch_id,reciept_id) values(121,12,2010);
insert into orderdetail(order_id,branch_id,reciept_id) values(122,13,2011);
/*-------------accountdetails-------------------*/
insert into accountdetail(accountno,accountname,reciept_id) values(10234511425,'Ahmed Ali',2003);
insert into accountdetail(accountno,accountname,reciept_id) values(10179607401,'Nadia Sheikh',2004);
insert into accountdetail(accountno,accountname,reciept_id) values(10556328896,'Amjad iqbal',2008);

----user----s
insert into users values(1,'admin','admin',null);
insert into users values(2,'mursaleen','12345',1114);
insert into users values(3,'okasha','12345',1112);
--select * from employees;
--select * from branches;
--select * from sizes;
--select * from cat_detail;
--select * from paymenttype;
--select * from orders;
--select * from items;
--select * from pricing;
--select * from itemdetails;
--select * from category;
--select * from deals;
--select * from dealdetails;
--select * from dealdescription;
--select * from billing;
--select * from orderdetail;
--select * from accountdetail;
commit;