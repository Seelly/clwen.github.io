mysql8修改密码

```sql
update user set authentication_string='pwd' where user ='username';
FLUSH PRIVILEGES;
```



### 表（Table）

> 任何一张表有行和列：
>
> * 行（row）：被称为数据/记录
>
> * 列（column）：被称为字段
>
> * 字段有：
>   * 字段名，数据类型，约束等属性
>   * 约束：其中一个约束为唯一性约束，该字段的数据==不能重复==

### SQL语句

> ##### DQL:数据查询语言（带有==selec==t关键字的语句）
>
> * select
>
>##### DML:数据操作语言（对表中数据增删改，操作的是==表中数据==）
>
>* insert
>
>* delete
>
>* update    	
>
> ##### DDL:数据定义语言，带有create drop alter的都是DDL，操作的是==表结构==
>
> * create 新建
>
> * drop删除
>
> * alter 修改
>
> ##### TCL:事务控制语言，包括：
>
> * 事务提交：commit
>
> * 事务回滚：rollback
>
> ##### DCL:数据控制语言
>
> * 授权grant
>
> * 撤销权限revoke

#### 常用命令

> select database();//查询当前使用数据库
>
> \c//终止一条命令输入
>
> desc 表名字 	查询表结构

### 导入数据

```sql
source 文件路径//路径中不能有中文
```

### 查询

> * 查询一个字段
>
>   * select 字段名 from 表名
>
> * 查询多个字段
>
>   * select column1，column2....from table
>
> * 查询所有字段
>
>   * select * from table
>
> 
>
> 
>
>     其他
>
> * 用as可以取别名，select abc as s
> * 数字型字段可以参与数学表达式运算，select number*12 from table
>
>   #### 条件查询
>
>   * select   字段名  from  where 条件
>
>   * 特殊符号：
>
> 不等于：!=，<>,
>
> 在两个值之间：between...and..
>
> 并且：and
>
> 或者：or
>
> 像：like，模糊查询，支持%和下划线匹配字符
>
> 包含：in
>
> 取非：not，主要用于in 和is中
>
> 匹配任意字符：%
>
> 匹配一个字符：__
>
> and 优先级比or高
>
> #### 模糊查询
>
> * like 称为模糊查询
>
> 匹配任意字符：%
>
> select name from user where name like ‘%o%’		//查询name包含o的
>
> 匹配一个字符：__
>
> select name from user where name like ‘__o%’		//查询name第二个字母为o的
>
> select name from user where name like ‘%\__o%’		//查询包含__的，需要用转义字符\
>



#### 排序

> ``` sql
> select name,age from user order by age //默认升序排序
> select name,age from user order by age desc //降序排序
> select name,age from user order by age asc//升序排序
> select name,age from user order by age asc，name asc//age相同时候，按照name升序
> 
> ```
>

#### 单行处理函数

​	单行函数特点：一行输入对应一行输出

​	多行函数特点：多行函数对应一个输出

```
 lower 转换小写
 upper 转换大写
 substr（x，y）从下标x到y取子串，下标从1开始没有0
 length 去长度
 trim 去掉空格
 format 设置千分位
 round 四舍五入
 rand（） 生成随机数
 infull 将null转换为具体值
 concat 拼接字符串
 str_to_data 字符串转换为日期
 data_format 格式化日期
```

#### 分组函数

> 多行处理函数：输入多个，最终输出一行。
>
> ``` 
> count 计数
> sum 求和
> avg 平均值
> max 最大值
> minn 最小值
> ```
>
> 分组函数使用时必须先分组才能使用，如果没有进行分组，整张表默认为一个组。
>
> ​	count（*）：统计行数
>
> ​	count（字段名）：统计不为null的行数
>
>  
>
> 使用顺序：==不能颠倒==
>
> ``` 
> select
> 	...
> from
> 	...
> group by
> 	...
> order by
> 	...
> ```
>
> 以上关键字执行顺序
>
> * from
> * where
> * group by
> * select
> * order by
>
> ==分组函数不能用在where后面==，因为where的优先级比group by高，where执行的时候还未分组 。
>
>  可以用having对group by后的结果筛选



#### 连接查询

> 多张表连接查询，如果==不加条件限制==，会出现==笛卡尔积==现象。
>
> ##### 内连接
>
> ``` 
> select
> 	xx，xx 
> from 
> 	table1
> inner join//innerr 内连接，可省略
> 	table2
> on
> 	连接条件
> where
> 	
> ```
>
> ##### 外连接
>
> ``` 
> select
> 	xx，xx 
> from 
> 	table1
> right join//右外连接，把右边表的所有信息查询出来，可改为left
> 	table2
> on
> 	连接条件
> where
> ```
>
> 
>
> #### 三表连接
>
> ``` 
> select
> 	xx，xx 
> from 
> 	table1
> join
> 	table2
> on
> 	1和2的连接条件
> left join 
> 	table3
> on 
> 	1和3的条件
> right join 
> 	table4
> on 
> 	1和4的条件
> //内外连接可以混用
> ```

#### 子查询

> select中嵌套select语句
>
> eg.在a中查询大于最小值的num
>
> ``` 
> select num from a where num > (select min(num) from a);
> ```
>

#### union

> 合并查询结果集，减少匹配次数。
>
> 在使用时要保证两个表的列数相同。
>
> 在MySQL中可以连接数据类型不同的列，Oracle中不可以。

### limit

> 将查询结果集部分取出，常用于分页查询。
>
> select * from table limit index，length；
>
> index：起始下标，第一条为0
>
> length：长度。
>
> ==limit==在order by之后执行

### 删除

> delete 删除：
>
> ​				删除慢，rollback可恢复。
>
> truncate：
>
> ​				truncate tble，删除快，不可恢复。

#### 约束

> #### 主键
>
> 不建议使用业务主键，使用==自然主键==，否则业务发生变化时会改变主键。
>
> 主键建议类型int，bigint等 ，定长数值。
>
> #### 外键
>
> 

#### 事务transaction

> 一个事务就是一个完整的业务逻辑，与事务有关的语句都是==DML==语句，事务要么同时成功，要么同时失败。
>
> ##### 提交事务commit
>
> 清空事务活动日志文件，将数据彻底持久化到数据库中；标志着事务成功结束。
>
> ##### 回滚事务rollback
>
> 将之前的DML操作全部撤销，并清空事务性活动日志文件；标志事务失败结束。
>
> *MySQL中==默认开启自动提交==事务
>
> 关闭自动提交机制语句：start transaction
>
> ##### 事务特性
>
> * 原子性
>
>   最小的工作但愿不可再分
>
> * 一致性
>
>   一个事务中，要么同时成功，要么同时失败
>
> * 隔离性
>
>   A,B事务之间有一定隔离
>
> * 持久性
>
>   事务提交，数据就持久地保存。
>
> ###### 事务隔离级别
>
> * 读未提交（Read uncommitted）：最低隔离级别。指事务A可以读取到B的未提交的数据，存在脏读（dirty read ）现象
> * 读已提交（Read committed）:A只能读取到B提交以后的数据，解决了脏读现象。但是不可重复读取数据，例如第一次读取到3条，第二次读取到4条，3！=4，称为不可重复读取去数据，读取到==真实数据==。==Oracle默认级别==
> * 可重复读（Repeatable read）：事务A开启后，即使B将数据改变，不管多久A读取到的数据没有发生改变，都是事务开启时的数据。解决不可重复读取数据。读取到的==非真实数据==。==MySQL默认级别==
> * 序列化/串行化（Serializable ）：最高隔离级别。解决所有问题，效率最低。事务排队进行，不能并发。
>
> 设置隔离级别方法：set global transaction isolation level ***

#### 索引

> 在表的字段添加的，未来提高查询效率的一种机制。一个字段可以添加一个索引，也可以多个字段联合添加索引。
>
> 任何数据库中，==主键自动添加==索引，==MySQL会给unique约束的字段添加索引==。
>
> ![数据表](https://pic2.zhimg.com/80/v2-5ede58ec7ac5609f96dffd420a035595_720w.png)
>
> 二叉树存储原则：左小右大
>
> ![二叉树存储原则：左小右大](https://pic1.zhimg.com/80/v2-51305c25a99c8384a6c939d8c5f9b04d_720w.png)
>
> ###### 索引创建
>
> create index table_id_index on table(id)；
>
> 给table表的id添加索引，取名为 table_id_index
>
> ###### 删除索引
>
> drop  index emp enane index on emp;
>
> 将emp表上的emp enane index索引对象删除
>
> ###### 查看索引
>
> 在mysql当中，怎么查看一个SQL语句是否使用了索引进行检索?
>
> explain select * fron enp where ename - 'KING' ;
>
> ###### 索引失效
>
> * 模糊查询以%开始导致索引失效，尽量避免以%开始匹配。
> * 使用or时，or两边的值必须都要有索引，否则索引失效。
> * 复合索引时候，没有使用左侧的列查询，使索引失效。
> * where当中索引列参加运算，索引失效。
> * where当中，索引列使用函数，索引失效，

#### 数据库设计范式

> ###### 第一范式
>
> 要求任何一张表必须有主键，每一个字段原子性不可再分.
>
> ###### 第二范式
>
> 建立在第一范式之上，要求所有非主键字段完全依赖主键，不产生部分依赖
>
> 复合主键才会产生传递依赖
>
> ![](https://pic1.zhimg.com/80/v2-fe44c799d7b4176eac971f1c51badda0_720w.jpg)
>
> ![](https://pic3.zhimg.com/80/v2-8cfe607738f5091ebede28c91e550022_720w.jpg)
>
> ###### 第三范式
>
> 建立在第二范式之上，要求所有非主键字段直接依赖主键，不产生传递依赖 
>
> ![](https://pic3.zhimg.com/80/v2-2d3791afde09415867fe7d4240c8baba_720w.jpg)
>
> ![](https://pic3.zhimg.com/80/v2-d10ea416b6e305778dbae737bc62193e_720w.jpg)
>
> 总结：
>
> 一对多：两张表，多的表加外键
>
> 多对多：三张表，关系表加外键

