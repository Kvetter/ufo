# UFO Linq Exercise


## Technical Diary

0:00 Starting (installing linq)

0:30 Just finished seeting up linqpad and made a simple query to get all customers, next i look at differences between mysql and linq

1:00 Looking at client-side joins (what it is and how its "prevented" by linq)


## List of Google queries and websites visited

https://www.linqpad.net

"connect linq to mysql server"

https://www.devart.com/dotconnect/mysql/articles/tutorial_linq.html

"connect linqpad to mysql server"

https://stackoverflow.com/questions/6629786/how-can-i-connect-to-mysql-via-linqpad

"Linq query"

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/linq-query-examples

https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/basic-linq-query-operations

"mysql vs linq"

https://www.quora.com/Is-LINQ-like-MySQL-or-Oracle-If-no-whats-the-difference

https://arstechnica.com/civis/viewtopic.php?t=37804

"sql vs linq"

https://www.linqpad.net/WhyLINQBeatsSQL.aspx


"client side joins"

https://stackoverflow.com/questions/16531527/which-is-better-in-performance-client-side-joins-or-server-side-joins


"prevent client side joins"

https://stackoverflow.com/questions/38969123/how-to-avoid-multiple-joins-for-better-performance

https://softwareengineering.stackexchange.com/questions/180012/is-there-any-reason-not-to-go-directly-from-client-side-javascript-to-a-database

"prevent client side joins linq"

https://stackoverflow.com/questions/9115708/how-to-write-linq-query-to-prevent-duplicates-joins

http://weblogs.thinktecture.com/pawel/2016/04/entity-framework-prevent-redundant-joins.html

https://coding.abel.nu/2012/06/dont-use-linqs-join-navigate/

https://docs.telerik.com/data-access/developers-guide/profiling-and-tuning/profiler-and-tuning-advisor/data-access-profiler-client-side-linq-queries

##Problems encountered

First problem is how linqpad "works", meaning how to set it up so a simple query to the remote database can be made.
I got confused because my query tab didn't automaticly point at the database when i added a new connection, i had to manually tell the tab i was using
to use the connection i just added. I used some time trying to figure out why my C# statements didn't work like in the tutorials i had looked up

Second problem, trying to figure out what "client side joins" means and if it is a bad thing and then how linq would "prevent" this.


