--select * from [dbo].[Order_items]
--select * from [dbo].[Orders]
--select * from [dbo].[Products]
--select * from [dbo].[Categories]
--drop table [dbo].[Order_items]

/*Исходная задача:
Напишите SQL-запрос, который для каждой категории товаров показывает:

Название категории.
Общую сумму продаж (количество × цена).
Количество проданных товаров.
Среднюю цену проданных товаров.
Отсортируйте результат по убыванию общей суммы продаж.

Задание:
Напишите исходный запрос для решения задачи.
Проверьте его производительность, используя данные объемом не менее 100 000 записей в таблицах order_items и products.
Оптимизируйте запрос:
Используйте индексы.
Проверьте план выполнения (EXPLAIN).
Перепишите запрос так, чтобы он выполнялся быстрее.*/

use AdventureWorksDW2017;

select * 
from (
select  c.[name] as 'categoryName', sum(p.price * oi.quantity) as 'totalSalesAmount', sum(oi.quantity) as 'numberOfSoldGoods', avg(p.price) as 'avgPrice'
from [dbo].[Categories] c
join [dbo].[Products] p on p.category_id = c.id
join [dbo].[Order_items] oi on oi.product_id = p.id
join [dbo].[Orders] o on o.id = oi.order_id
group by c.[name]) t
order by t.totalSalesAmount desc

create index ind_productid on [dbo].[Order_items](product_id)
create clustered index ind_product_id on [dbo].[Products](id)
create clustered index ind_order_id on [dbo].[Orders](id)

