# Database applications in use in business 

## What is a Database Application and why would we use one❓

A database application is software that enables users to store, retrieve, and manage data efficiently by holding information in a structured, relational system that facilitates queries. To understand why this matters, it helps to consider the alternative. When information is siloed across multiple locations and held in multiple formats (paper records in filing cabinets, spreadsheets on individual machines, emails in personal inboxes) it becomes extremely difficult and time-consuming to query that data in any meaningful way. Finding a single customer's complete history might require searching three different systems manually. Identifying a trend across departments might require someone to copy data into yet another spreadsheet and reconcile conflicting formats by hand. The data exists, but deriving insight from it is burdensome and slow.

By centralising this information in a relational database, organisations can use Structured Query Language (SQL) to ask meaningful questions of the data and return precise, consistent results. A query that would take a member of staff an afternoon or longer to compile manually can be returned in seconds. More importantly, because all users are drawing from the same centralised source, the results are consistent, there is a single source for the data rather than multiple conflicting spreadsheets produced by different teams at different times.

Database applications are highly flexible and can be adapted to a wide range of business use cases, from managing customer relationships and processing financial transactions to tracking inventory and analysing operational performance. 

 Due to their flexibility database applications are used across many sectors. In banking, they may be used to store customer accounts, process transactions, record balances, and support fraud monitoring. In healthcare, they help manage patient records, appointments, prescriptions, and test results while restricting access to sensitive medical information. In schools and colleges, databases are used to store student records, attendance, grades, timetables, and course enrolments. In e-commerce, they support product catalogues, customer accounts, orders, payments, stock levels, and delivery tracking. They are used wherever large amounts of structured data need to be stored, updated, protected, and queried.
 
Despite the variety of applications that a RDBMS can have they typically share a core set of features and functionality. 

## Architectural commonalities

Database applications commonly include features that help protect the accuracy and reliability of the data. Tables are designed with primary keys, which uniquely identify each record, and foreign keys, which link related records between tables. These relationships enforce referential integrity, meaning that records cannot easily become disconnected or inconsistent. For example, an order should not be linked to a customer who does not exist in the customer table. Constraints such as `NOT NULL`, `UNIQUE`, `CHECK`, primary keys, and foreign keys help prevent invalid or duplicate data from being entered.

Another common architectural feature is controlled access through user accounts, roles, and permissions. In SQL databases, administrators can decide which users are allowed to view, insert, update, or delete particular data. This means that different users can have different levels of access depending on their job role. For example, a receptionist in a healthcare setting may need access to appointment details, while only clinical staff should be able to view sensitive medical notes. Many database systems also support additional security features such as password authentication, encryption, backups, and audit trails. These help protect confidential information, recover data if something goes wrong, and record who accessed or changed data and when.

Many database applications also use forms, reports, and queries as part of their design. Forms provide a user-friendly way to enter or update data without requiring users to write SQL directly. Queries allow users to search, filter, join, and analyse data from one or more tables. Reports present selected data in a clear format for business decision-making, such as sales summaries, attendance reports, stock-level reports, or financial statements.

## Operational Commonalities

They typically support four essential operations, commonly referred to by the acronym CRUD: the ability to **Create** new records, to **Read** and retrieve information from those records, to **Update** existing information as circumstances change, and to **Delete** records when they are no longer required. These four operations underpin almost every interaction a user or application has with a database, and directly inform how a database application is designed.

In a relational database management system or **RDBMS**, these operations are usually carried out using Structured Query Language, or SQL. For example, `INSERT` is used to create new records, `SELECT` is used to read or retrieve records, `UPDATE` is used to amend existing records, and `DELETE` is used to remove records. All SQL databases MUST at least support the Keyword operations provided by SELECT,UPDATE, DELETE, INSERT, and WHERE. This gives users and applications a consistent way to interact with the data, regardless of whether the database is being used for customer orders, medical records, school attendance, or financial transactions.


```SQL

"CRUD operations and their SQL key word equivalents:"

-- Create
INSERT

-- Read
SELECT

-- Update
UPDATE

-- Delete
DELETE

```


Overall, while the purpose of a database application may vary between organisations, most are built around the same common principles: structured storage, CRUD operations, relationships between tables, data integrity, controlled access, and the ability to query and report on information efficiently.


## Structures used in database implementation

To explore and illustrate some of the core functionality of a relational database management system I will be considering the use case for a live music box office, this business will sell tickets for live music events across multiple venues, these events will be produced and promoted by different agencies and they will have different headlining artists. 

I will use this example to explain some key concepts in RDBMS design such as:

- fields/columns  
- records/rows  
- primary keys  
- foreign keys  
- relationships  
- data types  
- constraints  
- queries

## Tables, Columns & Datatypes

A database is organised into a structured hierarchy with the top-level object being the database itself, in turn this database will be composed of multiple distinct tables which will share some relationship to each other. Before considering how the database will be implemented it is first necessary to consider the data we would like to capture and reason about how to separate it into logical categories and what relationships these categories have to each other.

Each table will store data about one type of thing, known as an entity. An entity is something the organisation needs to record information about, such as a person, place, object, event, or transaction. When designing a database, one of the first steps is to identify the main entities by looking at the business process and asking what information needs to be stored. For example, in the case of my hypothetical box office, the business needs to store information about:

- Its **Customers**
- The **Venues** where events will be held 
- The **Promoters** who produce the show and book artists
- Information about the **Event** itself, the date and the price etc
- Information about the **Ticket**, it's serial number, date issued, status, etc

Each of these is a separate entity because each one has its own set of details or *attributes*. 

For instance, a customer has a name, DOB, email address, and phone number; a venue has a name, location, and capacity; an event has a date, ticket price, promoter, and venue; and ticket records which customer bought tickets for which event. Because these are distinct types of information, they are best stored in separate but related tables. Our supposed `box_office` database will have the following separate tables:

- `box_office`
	- `customer`
	- `venue`
	- `promoter`
	- `event`
	- `ticket`

Each of these tables are composed of **fields** or columns. These define the type of information that can be stored in the table. For example, the `customer` table might include the following columns:

- `customer_id`
- `first_name`
- `last_name`
- `email`
- `address_line_one`
-  `city`
- `postcode`
- `phone_number`
- `date_of_birth`
- `referrer`

These columns impose a structure on the data being collected and can be defined in order to accept only certain kinds of data or **datatypes.** For instance the `date_of_birth` column can be implemented to accept only dates, this means that the data must be supplied to the database in a manner that is recognisable to it as a date, the standard for entries to an SQL database is defined by ISO 8601 meaning that the database expects the date to be formatted in the following manner `yyyy/mm/dd`. The virtue of implementing this as a recognisable date is that it now allows us to perform logical operations on it which would not be possible if it were instead stored as a string of text for instance. Now that the `date_of_birth` is captured as a `DATE` datatype we can write the logic for a calculated field to deduce the customers age, something that would not be possible if instead it were stored as text or VARCHAR.

There are many different kinds of datatypes that can be defined in an SQL database with each allowing for different kinds of operation on them, such as numerical datatypes which allow for mathematical operations or Boolean datatypes which allow for logical operations. Here are some of the different kinds of datatypes that could be used when specifying columns within a table:

- Numeric 
	- INT, DECIMAL, FLOAT
- Binary (for raw data)
	- BINARY, BLOB
- String (for text)
	- VARCHAR, CHAR, TEXT
- Boolean
	- BOOLEAN, BIT
- Date/Time
	- DATE, TIME, DATETIME
- Special
	- UUID, JSON, XML

## Other Constraints

Furthermore, additional constraints can be specified and applied to the columns of a table that further restrict the kind of data that will be accepted by the database. A `NOT NULL` constraint means that a field must contain a value and cannot be left blank. For example, a customer record may require a `first_name` and `email_address` because these are essential pieces of information. A `UNIQUE` constraint ensures that no two records in a table can contain the same value for that column. This could be used for an email address, where each customer should have a different email. A `CHECK` constraint is used to limit the values that can be entered into a column based on a condition. For example, a ticket price could be checked to ensure that it is greater than zero, or a venue capacity could be checked to ensure it is not a negative number. 

These constraints help maintain data accuracy and prevent invalid records from being stored. 

## Types of Keys

Two other kinds of constraint are especially important in relational databases are **primary keys** and **foreign keys**, which are used to uniquely identify records and create relationships between tables.

A **primary key** is a column used to uniquely identify each row in a table. Each table can only have one primary key, and the values in that key must be unique and not null. For example, in a `customer` table, `customer_id` can be used as the primary key because each customer should have a unique identifier.

A **foreign key** is a column in one table that refers to the primary key of another table. Foreign keys are used to create relationships between tables and enforce referential integrity. This means that a record cannot refer to another record that does not exist. For example, in the ticket box office database, the `event` table contains `promoter_id` and `venue_id` as foreign keys. These link each event to a valid promoter and venue. Similarly, the `ticket` table contains `customer_id` and `event_id`, linking each ticket to the customer who bought it and the event it is for.

Foreign keys help reduce duplication because related information can be stored once in its own table and then referenced where needed. For example, the venue name and capacity do not need to be repeated in every event record. Instead, the event stores the `venue_id`, and the full venue details can be retrieved by joining the `event` and `venue` tables. This makes the database easier to update and helps keep related data consistent.


## Rows & Records

Each individual entry in a table is called a **record**, or row. For example, one row in the `customer` table represents one customer. A row is made up of values entered into the columns defined by the table structure. When a new record is added, the database checks the values against the rules set for each column before accepting it. These rules include the column’s data type, any constraints, and any key relationships.

For example, if the `customer_id` column is defined as an integer primary key, the database will only accept a valid whole number and will not allow two customers to have the same `customer_id`. If the `email` column is marked as `NOT NULL`, then a customer record cannot be saved without an email address. If the email column also has a `UNIQUE` constraint, the database will reject a new record if another customer already has the same email address.

This means the structure of the table controls the quality of the data entered into it. The database does not just store any information the user provides; it validates each record against the design of the table. This helps prevent missing, duplicated, or invalid data from being added and helps keep the database accurate and consistent.


## Relationships between tables

The tables in the `box_office` database are linked together using relationships. These relationships are created by correlating primary keys and foreign keys, allowing data to be stored in separate tables while still being connected when needed. For example, the `event` table does not need to store the full details of each venue or promoter. Instead, it stores `venue_id` and `promoter_id`, which link to the relevant records in the `venue` and `promoter` tables.

There are several common types of relationship used in relational database design. 

A **one-to-one relationship** occurs when one record in a table is linked to only one record in another table. For example, a database might store a customer’s login details in one table and their customer profile in another, with each login record belonging to one customer profile. This can be useful when sensitive or optional information needs to be separated. 

A **one-to-many relationship** occurs when one record in a table can be linked to many records in another table. This is one of the most common relationship types. In the `box_office` database, one `promoter` can be linked to many `event` records because a promoter may organise more than one event. However, each individual event is linked to only one promoter. Similarly, one `venue` can host many `event` records, but each event takes place at one venue.

A **many-to-many relationship** occurs when many records in one table can be linked to many records in another table. This is usually implemented using a linking table or associative table. In the `box_office` database, one `customer` can buy tickets for many events, and one `event` can have tickets bought by many customers. This relationship is represented through the `ticket` table, which links `customer` and `event` together by storing both `customer_id` and `event_id`.

Another type of relationship is a **recursive relationship**. This occurs when a table contains a foreign key that refers back to its own primary key. In the `box_office` database, the `customer` table uses the `referrer` field to refer to another customer in the same table. This allows the database to record which customer referred another customer and enables a self join to be performed.

These relationships reduce duplication and improve data consistency. Relationships also allow related data to be queried together. The database can retrieve the promoter and venue for an event, list the customers attending a gig, calculate how many valid tickets have been sold, or use aggregate functions to calculate revenue by event, venue, or promoter.

#  Creating the Database

To begin to understand the data and how the tables and columns relate to each other it is usually necessary to create an Entity Relationship Diagram (ERD). Here is an ERD for the proposed `box_office` database which illustrates the relationships between the tables, the datatypes expected in each column and also the primary and foreign keys.

The ERD forms part of the data modelling process. Data modelling involves identifying the main entities that the database needs to store information about, such as `customer`, `venue`, `promoter`, `event`, and `ticket`, and then deciding what attributes belong to each entity. It also involves defining the relationships between those entities so that the database accurately reflects the real-world process it is intended to represent.

During this process, the data should also be normalised. The normalisation process involves organising the data in a logical manner in order to reduce unnecessary duplication and to improve consistency. This makes the database easier to maintain, because if the details of field change, such as the `venue_email`, it will only need to be updated in one place.

![[sql_schema_png.png]]

While there are a few different variants of SQL databases such as Oracle, MySQL, Postgres, MongoDB, etc, I will be implementing this database with Microsoft SQL Server. It was chosen for this project because it is a widely used relational database management system suitable for business and educational database development. It supports structured data storage, SQL querying, primary and foreign keys, data integrity constraints, joins, and controlled access to data. Although the `box office` database is illustrative, SQL Server provides a realistic professional environment for demonstrating relational database design and implementation.

## Implementing the Database

I will use the ERD as a guide to setup the `box_office` database. To begin, the database itself must be created.

```SQL
"Database initialised with the CREATE keyword"
CREATE DATABASE box_office;
```

Next the tables need to be created, I will start with the tables that do not rely on references to other tables, IE do not have Foreign Keys otherwise I would need to reference those tables when they do not currently exist. As the Foreign keys are logically dependent on the Primary Keys the database will not allow me to create these tables to ensure referential integrity.

### Promoter Table

```SQL
"I will declare which database I would like to use"
USE box_office;

"The CREATE TABLE command is used to create individual tables within the database. While SQL is in fact case invariant, the convention is for SQL Keywords to be declared in uppercase and for identifiers to use lowercase. Furthermore I will be using a linter to make the syntax even more clear"

"I have made a design decision to limit the email field to 100 characters. While I acknowledge that it is technically possible to have a valid email of 255 characters an analysis of >10 million emails concluded that the longest valid one was in fact only 89 characters in length."

CREATE TABLE promoter (
    promoter_id INT IDENTITY(1,1) PRIMARY KEY,
    promoter_name VARCHAR(100) NOT NULL,
    promoter_email VARCHAR(100),
    promoter_phone VARCHAR(20)
);
```

### Venue Table

```SQL
USE box_office;

"I have introduced a check on venue_capacity to make sure that it is greater than 0 as well as the constraint that it be NOT NULL"

CREATE TABLE venue (  
	venue_id INT IDENTITY(1,1) PRIMARY KEY,  
	venue_name VARCHAR(100) NOT NULL,  
	venue_address_line_one VARCHAR(100) NOT NULL,
	venue_city VARCHAR(100) NOT NULL,
	venue_postcode VARCHAR(100) NOT NULL,
	venue_email VARCHAR(100) NOT NULL,
	venue_website VARCHAR(100) NOT NULL,
	venue_capacity INT NOT NULL CHECK (venue_capacity > 0),
	disabled_access BIT NOT NULL DEFAULT 0
);
```

###  Customer Table

```SQL
USE box_office;

"I have included a referrer as a foreign key in this table, however, it refers back to the customer_id. This is so that I can perform a self join later on and show which customers have referred other customers. I have also allowed this value to be NULL by default to cover the situation whereby the customer has not been referred by anyone.

Phone numbers are storred as text to account for leading zeroes as in 02920456789.

The 'age' column is a computed column and calculates the age by retreiving todays date via GETDATE(), as this returns a DATETIME datatype it is converted into a DATE datatype with the CAST function. We then apply a conditional logic to see if subtract the dates from one another and apply a conditional logic to subtract a further year if they have not had their birthday this year"

CREATE TABLE customer (  
customer_id INT IDENTITY(1,1) PRIMARY KEY,  
first_name VARCHAR(50) NOT NULL,  
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,   
date_of_birth DATE NOT NULL,
address_line_one VARCHAR(100) NOT NULL,
city VARCHAR(100) NOT NULL, 
phone VARCHAR(20),  
referrer INT NULL,
age AS (  
	DATEDIFF(YEAR, date_of_birth, CAST(GETDATE() AS DATE))  
	- CASE  
		WHEN DATEADD(  
		YEAR,  
		DATEDIFF(YEAR, date_of_birth, CAST(GETDATE() AS DATE)),  
		date_of_birth  
		) > CAST(GETDATE() AS DATE)  
		THEN 1  
		ELSE 0  
	END  
),

CONSTRAINT fk_customer_referred_by  
	FOREIGN KEY (referrer)  
	REFERENCES customer(customer_id)  
);
```

### Event Table

```SQL
USE box_office;

"The event table can now be created without error as it references both the venue and promoter table which have both been created. Furthermore a check has been added to make sure that ticket price is above zero and an additional check has been added to confirm if an age restriction is in place, typically is either all ages, over 14 or over 18."

CREATE TABLE event (  
	event_id INT IDENTITY(1,1) PRIMARY KEY,  
	event_name VARCHAR(100) NOT NULL,  
	event_date DATE NOT NULL,  
	ticket_price DECIMAL(8,2) NOT NULL CHECK (ticket_price > 0),
	age_restriction INT NOT NULL 
		CONSTRAINT chk_age_restriction CHECK (age_restriction IN (0, 14, 18)),   
	promoter_id INT NOT NULL,  
	venue_id INT NOT NULL,  
	  
	CONSTRAINT fk_event_promoter  
		FOREIGN KEY (promoter_id)  
		REFERENCES promoter(promoter_id),  
	  
	CONSTRAINT fk_event_venue  
		FOREIGN KEY (venue_id)  
		REFERENCES venue(venue_id)  
);
```

### Ticket Table

```SQL
USE box_office;

"The ticket table relates a customer to an event that they have a ticket for. 

ticket_guid uses the NEWID() function provided by SQL Server to generate a GUID which will be a public facing Unique Identifier. I felt that this was necessary as the auto incrementing ticket_id is unsuitable to be provided publically (printed on a ticket for instance) as it is a business intelligence leak. It could theoretically be used to infer the amount of ticket sales between two points in time and is directly related to the number of entries within the database.

There is a boolean field is_redeemed which could be updated when the ticket is scanned and used at point of entry preventing duplicate tickets being inadvertently accepted.

There is a simple check in order to allow multiple types of ticket status to account for situations where it may be necessary to cancel or refund the ticket, void it if created in error and expired if the ticket was never redeemed.

Finally the Foreign keys relate and assign the ticket to an event and to a customer"


CREATE TABLE ticket (  
	ticket_id INT IDENTITY(1,1) PRIMARY KEY,
	ticket_guid UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
	date_issued DATETIME NOT NULL DEFAULT GETDATE(),    
	event_id INT NOT NULL,  
	customer_id INT NOT NULL,   
	is_redeemed BIT NOT NULL DEFAULT 0,  
	redeemed_at DATETIME NULL,  
	ticket_status VARCHAR(20) NOT NULL DEFAULT 'valid'  
	CHECK (ticket_status IN ('valid', 'cancelled', 'refunded', 'void', 'expired')),  

CONSTRAINT fk_ticket_customer  
	FOREIGN KEY (customer_id)  
	REFERENCES customer(customer_id),  
  
CONSTRAINT fk_ticket_event  
	FOREIGN KEY (event_id)  
	REFERENCES event(event_id)
);
```


## Full Schema

Here is a copy of the schema in it's entirety.

```SQL
CREATE DATABASE box_office;  
GO  
  
USE box_office;  
GO

CREATE TABLE promoter (
    promoter_id INT IDENTITY(1,1) PRIMARY KEY,
    promoter_name VARCHAR(100) NOT NULL,
    promoter_email VARCHAR(100),
    promoter_phone VARCHAR(20)
);

CREATE TABLE venue (  
	venue_id INT IDENTITY(1,1) PRIMARY KEY,  
	venue_name VARCHAR(100) NOT NULL,  
	venue_address_line_one VARCHAR(100) NOT NULL,
	venue_city VARCHAR(100) NOT NULL,
	venue_postcode VARCHAR(100) NOT NULL,
	venue_email VARCHAR(100) NOT NULL,
	venue_website VARCHAR(100) NOT NULL,
	venue_capacity INT NOT NULL CHECK (venue_capacity > 0),
	disabled_access BIT NOT NULL DEFAULT 0
);

CREATE TABLE customer (  
	customer_id INT IDENTITY(1,1) PRIMARY KEY,
	customer_public_guid UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),  
	first_name VARCHAR(50) NOT NULL,  
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,   
	date_of_birth DATE NOT NULL,
	address_line_one VARCHAR(100) NOT NULL,
	city VARCHAR(100) NOT NULL, 
	phone VARCHAR(20),  
	referrer INT NULL,
	age AS (  
	DATEDIFF(YEAR, date_of_birth, CAST(GETDATE() AS DATE))  
		- CASE  
			WHEN DATEADD(  
			YEAR,  
			DATEDIFF(YEAR, date_of_birth, CAST(GETDATE() AS DATE)),  
			date_of_birth  
			) > CAST(GETDATE() AS DATE)  
			THEN 1  
			ELSE 0  
		END  
	),
	  
	CONSTRAINT fk_customer_referred_by  
		FOREIGN KEY (referrer)  
		REFERENCES customer(customer_id)  
);

CREATE TABLE event (  
	event_id INT IDENTITY(1,1) PRIMARY KEY,  
	event_name VARCHAR(100) NOT NULL,  
	event_date DATE NOT NULL,  
	ticket_price DECIMAL(8,2) NOT NULL CHECK (ticket_price > 0),
	age_restriction INT NOT NULL 
		CONSTRAINT chk_age_restriction CHECK (age_restriction IN (0, 14, 18)),   
	promoter_id INT NOT NULL,  
	venue_id INT NOT NULL,  
	  
	CONSTRAINT fk_event_promoter  
		FOREIGN KEY (promoter_id)  
		REFERENCES promoter(promoter_id),  
	  
	CONSTRAINT fk_event_venue  
		FOREIGN KEY (venue_id)  
		REFERENCES venue(venue_id)  
);

CREATE TABLE ticket (  
	ticket_id INT IDENTITY(1,1) PRIMARY KEY,
	ticket_guid UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
	date_issued DATETIME NOT NULL DEFAULT GETDATE(),    
	event_id INT NOT NULL,  
	customer_id INT NOT NULL,   
	is_redeemed BIT NOT NULL DEFAULT 0,  
	redeemed_at DATETIME NULL,  
	ticket_status VARCHAR(20) NOT NULL DEFAULT 'valid'  
	CHECK (ticket_status IN ('valid', 'cancelled', 'refunded', 'void', 'expired')),  

CONSTRAINT fk_ticket_customer  
	FOREIGN KEY (customer_id)  
	REFERENCES customer(customer_id),  
  
CONSTRAINT fk_ticket_event  
	FOREIGN KEY (event_id)  
	REFERENCES event(event_id)
);

```


# Basic SQL Statements

Here are some of the basic statements that allow the user to Create, Read, Update and Delete (CRUD) records from within a table.

## Creating Records

Now that the database structure is implemented we can begin to populate it with information. For the sake of this assignment the data is fictional and will be entered directly with SQL commands. I will provide the syntax for inserting into the `promoter` table here but I will be using the exact same method to insert data into all other tables with the exception of the `ticket` table, the data for which will be procedurally generated by a script. The full INSERT statements and Schema will be provided separately.

```SQL
USE box_office;

"As the promoter_id field is set to auto-increment/identity it can be omitted from the insertion as it will be added by the database when a record is inserted."

INSERT INTO promoter
--Specify the columns to insert values into  
(promoter_name, promoter_email, promoter_phone)
VALUES
('SJM Concerts', 'info@sjmconcerts.com', '0161 907 3600'),
('333 Promotions', 'info@333promotions.co.uk', '02920 344333'),
('No Poetry', 'hello@nopoetry.co.uk', '02920 198765'),
...
...


```

The Tables have been populated with 40 records for `promoter`, 20 records for `venue`, 500 records for `customer`, 80 records for `event`,  and finally 20, 000 entries for `ticket` which will be used to demonstrate common SQL queries and functions.

## Simple SELECT statement

One of the most simplest statements that we can use to **read** information from the database is the `SELECT *` statement which will display all entries in the table. We can extend the functionality of this statement by applying conditional statements with the keyword `WHERE` as will be demonstrated later.

![[select_from_venue.png]]

## Updating Records

As well as creating and reading records it is sometimes necessary to update the information within a record, this can be done by using the `UPDATE` keyword and specifying the table and row and/or rows to be updated. Consider the following example, in the `venue` table there is a location that needs to be updated from 'Pentyrch' to 'Cardiff' this would be achieved as follows:

![[select_acapella_from_venue.png]]

```SQL
"Update the entry for Acapella Studios to change venue_city from 'Pentyrch' to 'Cardiff' using the UPDATE function and the venue_id"

UPDATE venue
SET venue_city = 'Cardiff'
WHERE venue_id = 7;
```

As can be seen after running another `SELECT *` statement the Acapela Studio record with `venue_id` = 17 in the `venue` table has indeed been updated.

![[updated_acapella.png]]

Deleting Records

It is also possible to delete records within a table using the `DELETE` keyword. The basic syntax of such a statement is as follows:

```SQL
DELETE FROM _table_name_ WHERE _condition_;

/*
**Note:** Be careful when deleting records in a table.
Notice the `WHERE` clause in the `DELETE` statement. The `WHERE` clause specifies which record(s) should be deleted. If you omit the `WHERE` clause, ALL records in the table will be deleted.
/*

```

Here I will be deleting a record from the `ticket` table. I have chosen this table to demonstrate the `DELETE` function as the records in this table are not referenced in other tables so I can safely delete records within this table without violating the referential integrity of the database.

As can be seen there are many tickets in the ticket table that correlate a `ticket_id` with an `event_id` and a `customer_id` 

![[select_tickets.png]]

I would like to remove the information for  the ticket with the`ticket_id = 20,000`. This is achieved with the following SQL statement.

```SQL
DELETE FROM ticket  
WHERE ticket_id = 20000;
```

![[delete_ticket.png]]


# SQL Aggregate Functions

SQL has a number of aggregate functions  such as `SUM, AVG, MIN, MAX, COUNT` that reduce rows to a single result. Example usage:

## Sum

Sum will total all of the values within a column. Here I will `SUM` the values of all the tickets sold to calculate the `total_ticket_revenue`. This query requires an `INNER JOIN` which will be explained in more detail later. The total amount of tickets sold amounts to £340,153.50

```SQL
USE box_office
-- calculate the total revenue generated from ticket sales for all events
SELECT SUM(event.ticket_price) AS total_ticket_revenue
FROM ticket
INNER JOIN event
    ON ticket.event_id = event.event_id;
```

![[sum_revenue.png]]

## Count

Here I will use the `COUNT` function to count the number of records in the `event` table. Because `event_id` is the primary key, each event record has a unique identifier, so counting `event_id` shows how many event records are currently stored. 

I have also used the keyword `AS` to create an alias for the column header so that it is clear what this statement is counting.

![[count_events 1.png]]

## Average

The average function will total the entries in a column and divide by the number of entries in the column. It will however ignore all `NULL` values meaning that they will neither contribute to either the total or the count (where AVG = total/count). Here the average ticket price for a gig is determined to be £14.56

![[avg_ticket_price.png]]

## Min & Max

The `MIN` and `MAX` functions can be used to return the lowest and highest values found within a column. In this case the prices of gig tickets range from a minimum of £7.50 to a maximum of £30.00.

![[min_ticket_price.png]]

![[max_price_ticket.png]]


# WHERE Statement

The `WHERE` clause is used to filter down the records returned by a query. Instead of displaying every row in a table, it allows the user to specify one or more conditions that each row must meet in order to be included in the search results. Conditions can be combined using logical operators such as `AND` and `OR`.  This makes the `WHERE` clause useful for creating more precise queries, for example:

```SQL
USE box_office

/* find all events with an age restriction of 18 and a ticket price
greater than 20.00 */

SELECT * FROM event  
WHERE age_restriction = 18  
AND ticket_price > 20.00;
```

![[select_age_restriction_events.png]]


# Joins

I have used the `JOIN` clause in a previous query in order to combine information from multiple tables together based on a column that relates the data in those tables together such as the foreign key.

There are different kinds of joins that can be performed depending on how we would like to combine the tables and data together.

- `LEFT (OUTER) JOIN`: Returns **all rows from the left table**: matched rows from the right table
- `RIGHT (OUTER) JOIN`: Returns **all rows from the right table**: matched rows from the left table.
- `FULL (OUTER) JOIN`: Returns **all rows** when there is a match in either the left or right table
- `(INNER) JOIN`: Returns only rows that have **matching values** in both tables

## Full Outer Join

A `FULL OUTER JOIN` returns all matching and non-matching records from both tables. In this example, it can be used to compare venues and events. Venues with matching events will appear together, while venues with no events *will still appear* with `NULL` values in the event columns. In this case it reveals that 3 venues, Utilita Arena, St David's Hall and Jacobs basement have no events booked.

```SQL
USE box_office
/* 
OUTER JOIN: Return all venues and all events, including those that do
not have a match in the other table. 
*/
SELECT
    venue.venue_id,
    venue.venue_name,
    event.event_id,
    event.event_name
FROM venue
FULL OUTER JOIN event
ON venue.venue_id = event.venue_id;
```

![[venues_with_no_events.png]]


## Left Outer Join

A `LEFT JOIN` returns all records from the table specified *before* the `JOIN` statement (the left hand table), along with any matching records from the table specified *after* the `join` statement (the right hand table). If there is no matching record in the right-hand table, the left-hand record is still included and the missing values from the right-hand table are returned as `NULL`. This makes a `LEFT JOIN` useful when the query needs to include all records from one table, even where related data may not exist.

This query uses a `LEFT JOIN` because the `event` table appears on the left side of the `JOIN` statement. This means all events are returned, even where there are no matching records in the `ticket` table. Where ticket records do exist, they are matched using the shared `event_id` field. Where no tickets have been sold for an event, the ticket fields return `NULL`, and `COUNT(ticket.ticket_id)` returns `0`. This allows the query to show ticket sales for every event, including events with no ticket sales.

```SQL
USE box_office
/* 
Return the total number of tickets sold for each event using COUNT for tickets_sold and GROUP BY on event_id,
ordered by the number of tickets sold in descending order. 
Includes events that have not sold any tickets.
*/
SELECT event.event_name,
COUNT(ticket.ticket_id) AS tickets_sold
FROM event
LEFT JOIN ticket
ON event.event_id = ticket.event_id
GROUP BY event.event_name
ORDER BY tickets_sold DESC;
```

![[tickets_per_gig.png]]

## Right Outer Join

A `RIGHT JOIN` works in the opposite direction to the `LEFT JOIN`. It returns all records from the table written *after* the `JOIN` statement (the right hand table), along with any matching records from the written *before* the `JOIN` statement (the left hand table). A `RIGHT JOIN` can be rewritten as an equivalent `LEFT JOIN` by reversing the order of the tables. For this reason, `RIGHT JOIN` does not usually provide different functionality from `LEFT JOIN` as it fundamentally expresses the same relationship. 

For example this `RIGHT JOIN` is identical to the query used for the  previous `LEFT JOIN` but with the table order reversed which will provide the same results.

```SQL
USE box_office
/* 
RIGHT JOIN: Identical result to LEFT JOIN but table order reversed
Return the total number of tickets sold for each event 
*/
SELECT event.event_name,
COUNT(ticket.ticket_id) AS tickets_sold
FROM ticket
RIGHT JOIN event
ON ticket.event_id = event.event_id
GROUP BY event.event_name
ORDER BY tickets_sold DESC;

```

![[right_join_ticket_sales.png]]

## Inner Join

An `INNER JOIN` returns only records where there is a matching value in both tables being joined. It is used when the query is interested only in related data that definitely exists on both sides of the relationship. This contrasts with an outer join, which can return all records from one table even when no matching record exists in the other.

The following query returns a list of events and uses `INNER JOIN` to bring in related information from the `promoter` and `venue` tables. The `event` table stores the foreign keys `promoter_id` and `venue_id`, but the actual promoter and venue names are stored separately in their own tables. By joining these tables together, the query can display the event name, event date, promoter name, and venue name in one result.

```SQL
USE box_office
/* 
Return a list of all events, including the promoter and venue names 
from their respective tables. 
The list should be ordered by event date in ascending order.
*/
SELECT
    event.event_name,
    event.event_date,
    event.ticket_price,
    promoter.promoter_name,
    venue.venue_name,
    venue.venue_address_line_one
FROM event
INNER JOIN promoter
ON event.promoter_id = promoter.promoter_id
INNER JOIN venue
ON event.venue_id = venue.venue_id;
```

![[inner_join_event_on_venue_promoter.png]]

Self Join

A **self join** is used when a table needs to be joined to itself. In this database, the `customer` table includes a `referrer` column, which stores the `customer_id` of another customer who referred them. This means the table has a relationship with itself, IE a recursive relationship, one customer can be the **referrer**, while another customer is the **referee**. 

To make this readable, the same table is given two different aliases so that SQL Server can treat one copy as the referee and the other as the referrer. As the table uses an `INNER JOIN` it only returns customers who actually have a referrer. Customers where the `referrer` is `NULL` will not appear in the results.

```SQL
USE box_office;
/*
Return customers who were referred by another customer.
Show the referrer and referee names rather than their customer_id values.
*/
SELECT
    referrer.first_name + ' ' + referrer.last_name AS referrer_name,
    referee.first_name + ' ' + referee.last_name AS referee_name
FROM customer AS referee
INNER JOIN customer AS referrer
ON referee.referrer = referrer.customer_id
ORDER BY referrer_name, referee_name;
```


# Management Information Reports

Now that the different types of queries have been demonstrated we can consider the different kinds of results that the database is capable of providing and construct the corresponding queries. The way that this database has been structured allows us to ask meaningful questions about the data it contains that can be compiled into insightful management reports.

## Total Revenue and Ticket Sales by Venue

The total amount of revenue generated by each individual venue can be listed and ordered revealing that £72,105.50 worth of tickets have been sold for the 5 events being hosted at the Tramshed and that these events will pull 2990 people through their doors. 

```SQL
/*
Calculate the total ticket revenue generated by each venue.
Each row in the ticket table represents one individual ticket.
Also show how many gigs/events are being held at each venue.
*/
SELECT
    venue.venue_name,
    venue.venue_city,
    COUNT(DISTINCT event.event_id) AS number_of_gigs,
    COUNT(ticket.ticket_id) AS tickets_sold,
    SUM(event.ticket_price) AS total_revenue
FROM venue
LEFT JOIN event
ON venue.venue_id = event.venue_id
LEFT JOIN ticket
ON event.event_id = ticket.event_id
GROUP BY
    venue.venue_name,
    venue.venue_city
ORDER BY total_revenue DESC;
```

![[ticket_revenue_and_sales_per_venue.png]]

## Total Revenue Generated by each promoter at each Venue

```SQL
/*
Calculate the number of tickets sold and total revenue generated
by each promoter at each venue.
*/
SELECT
    promoter.promoter_name,
    venue.venue_name,
    venue.venue_city,
    COUNT(ticket.ticket_id) AS tickets_sold,
    SUM(event.ticket_price) AS total_revenue
FROM promoter
INNER JOIN event
ON promoter.promoter_id = event.promoter_id
INNER JOIN venue
ON event.venue_id = venue.venue_id
LEFT JOIN ticket
ON event.event_id = ticket.event_id
GROUP BY
    promoter.promoter_name,
    venue.venue_name,
    venue.venue_city
ORDER BY
    venue.venue_name,
    total_revenue DESC;
```

![[promoter_revenue_by_venue.png]]

From this query we can see that of the 5 events and £72,105.50 in ticket sales for the Tramshed only one of those events is being produced internally and generating £9383.50 in revenue, while 4 of the other events are external promoters. This query reveals how the £72,105.50 is distributed across the 5 promoters producing events at the Tramshed.

## Amount of Tickets Sold and Revenue For Each Event 

This will find the total amount of revenue generated by each event, the amount of tickets sold and the capacity of each venue. Furthermore by creating a join on the venue table we can retrieve the venue capacity and calculate how many tickets are left until it is at capacity.

```SQL
/*
Calculate tickets sold and total revenue for each event,
including the venue name and venue capacity.
Each row in the ticket table represents one individual ticket.
*/
SELECT
    event.event_name,
    event.event_date,
    venue.venue_name,
    venue.venue_capacity,
    COUNT(ticket.ticket_id) AS tickets_sold,
    venue.venue_capacity - COUNT(ticket.ticket_id) AS remaining_capacity,
    SUM(event.ticket_price) AS total_revenue
FROM event
INNER JOIN venue
ON event.venue_id = venue.venue_id
LEFT JOIN ticket
ON event.event_id = ticket.event_id
GROUP BY
    event.event_name,
    event.event_date,
    venue.venue_name,
    venue.venue_capacity
ORDER BY total_revenue DESC;
```

![[remaining_capacity.png]]
```
```

Here we can see that the top grossing event is Cate Le Bon at The Wales Millennium Centre which has sold 1214 tickets and grossed £33,992.00. As the WMC has a capacity of 1900 there is remaining capacity for a further 686 people / tickets.

## MIN, MAX and AVG ticket prices per venue for over 18 Events

Here I have done an inner join to exclude the venues that have 0 ticket sales of which there are 3. This query will provide the user with the spread of ticket prices for events per venue by calculating and returning the minimum, the average and the maximum.

```SQL
/*
Calculate the aMIN, MAX and AVG ticket price for 18+ events at each venue.
*/
SELECT
    venue.venue_name,
    venue.venue_city,
    MIN(event.ticket_price) AS minimum_ticket_price,
    AVG(event.ticket_price) AS average_ticket_price,
    MAX(event.ticket_price) AS maximum_ticket_price
FROM venue
INNER JOIN event
ON venue.venue_id = event.venue_id
WHERE event.age_restriction = 18
GROUP BY
    venue.venue_name,
    venue.venue_city
ORDER BY average_ticket_price DESC;
```

![[min_max_average.png]]

## Dashboard View

It is also possible to create a virtual table in SQL which can be constructed of multiple joins and provide a summary of the salient event information. Here I will combine the `promoter`, `venue`, and `ticket tables` to provide a convenient summary of event information.

```SQL
CREATE VIEW vw_event_sales_summary AS  
SELECT  
	event.event_id,  
	event.event_name,  
	event.event_date,  
	event.ticket_price,  
	event.age_restriction,  
	promoter.promoter_name,  
	venue.venue_name,  
	venue.venue_city,  
	venue.venue_capacity,  
	COUNT(ticket.ticket_id) AS tickets_sold,  
	venue.venue_capacity - COUNT(ticket.ticket_id) AS remaining_capacity,  
	SUM(event.ticket_price) AS total_revenue  
FROM event  
INNER JOIN promoter  
ON event.promoter_id = promoter.promoter_id  
INNER JOIN venue  
ON event.venue_id = venue.venue_id  
LEFT JOIN ticket  
ON event.event_id = ticket.event_id  
AND ticket.ticket_status = 'valid'  
GROUP BY  
	event.event_id,  
	event.event_name,  
	event.event_date,  
	event.ticket_price,  
	event.age_restriction,  
	promoter.promoter_name,  
	venue.venue_name,  
	venue.venue_city,  
	venue.venue_capacity;
```

It can be queried as if it were an actual table:

```SQL
SELECT *
FROM vw_event_sales_summary
ORDER BY total_revenue DESC;
```

![[summary_view.png]]

# Notes  
  
# Supporting Documents

---
# Sources

GUID in SQL SERVER https://www.geeksforgeeks.org/sql-server/what-is-a-guid-in-sql-server/
CAST DATETIME to DATE https://www.geeksforgeeks.org/sql/sql-query-to-convert-datetime-to-date/



