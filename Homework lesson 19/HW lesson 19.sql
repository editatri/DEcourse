--Напишите скрипт, который с помощью цикла и переменной выводит таблицу умножения для заданного числа.

declare @number int = 3, @count int = 0

while @count <=10
BEGIN

select @number*@count
select @count+=1
END


--Таблицы: HumanResources.Employee
--Описание задачи: С помощью переменной найдите всех сотрудников, которые работают в компании дольше заданного количества лет.

declare @numOfYears int
set @numOfYears = 10

select * -- BusinessEntityID, LoginID, JobTitle
from [AdventureWorks2017].[HumanResources].[Employee]
where datediff(YEAR,  HireDate, getdate())  > @numOfYears
order by hiredate desc

--Таблицы: Sales.Customer, Sales.SalesOrderHeader
--Описание задачи: Напишите запрос с переменной и подзапросом, чтобы найти всех клиентов, которые потратили в сумме больше заданной суммы на все свои заказы.

declare @amount float
set @amount = 10000.10

select t.CustomerID
from (
select c.CustomerID, sum(so.TotalDue) as totalAmount
from [AdventureWorks2017].[Sales].[Customer] c
join [AdventureWorks2017].[Sales].[SalesOrderHeader] so on so.CustomerID = c.CustomerID 
group by c.CustomerID) t
where t.totalAmount > @amount


/*Таблицы:
Sales.SalesOrderDetail
Sales.SalesOrderHeader
Production.Product
Описание задачи: Напишите запрос, который с использованием переменной и подзапроса определяет самый продаваемый товар (по количеству проданных единиц) для каждого года.*/

declare @year int
set @year = 2014

select top 1 max(t.numberOfItems) as mostPopularProduct, t.Year, t.Name
from (
select year(so.ShipDate) as Year, p.Name, count(p.Name) as numberOfItems
from [AdventureWorks2017].[Sales].[SalesOrderDetail] s
join [AdventureWorks2017].[Sales].[SalesOrderHeader] so on so.salesorderid = s.salesorderid
join [AdventureWorks2017].[Production].[Product] p on p.ProductID = s.ProductID
group by year(so.ShipDate), p.Name
) t
where t.Year = @year
group by t.Year, t.name
order by max(t.numberOfItems) desc