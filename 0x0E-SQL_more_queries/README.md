# MORE QUERIES.

# 0x0E. SQL - More queries

## At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* **How to create a new MySQL user
* **How to manage privileges for a user to a database or table
* **What’s a PRIMARY KEY
* **What’s a FOREIGN KEY
* **How to use NOT NULL and UNIQUE constraints
* **How to retrieve datas from multiple tables in one request
* **What are subqueries
* **What are JOIN and UNION

## Tasks :page_with_curl:

* **0. My privileges!**
  * [0-privileges.sql](./0-privileges.sql): MySQL script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

* **1. Root user**
  * [1-create_user.sql](./1-create_user.sql): MySQL script that creates the MySQL server user user_0d_1
  
* **2. Read user**
  * [2-create_read_user.sql](./2-create_read_user.sql): MySQL script that creates the database hbtn_0d_2 and the user user_0d_2.

* **3. Always a name**
  * [3-force_name.sql](./3-force_name.sql): MySQL script that creates the table force_name on your MySQL server.
  
* **4. ID can't be null**
  * [4-never_empty.sql](./4-never_empty.sql): MySQL script that creates the table `id_not_null` on your `MySQL server`.
  * id_not_null Description:
    * `id`: INT with the default value 1
    * `name`: VARCHAR(256).

* **5. Unique ID**
  * [5-unique_id.sql](./5-unique_id.sql): MySQL script that creates the table `unique_id` on your `MySQL server`.
  * unique_id description:
    * `id`: INT with the default value 1 and must be unique
    * `name`: VARCHAR(256).
  
* **6. States table**
  * [6-states.sql](./6-states.sql): MySQL script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
  * `states`: description:
    * `id`:  INT unique, auto generated, can’t be null and is a primary key.
    * `name`: VARCHAR(256) can’t be null.

* **7. Cities table**
  * [7-cities.sql](./7-cities.sql): MySQL script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your `MySQL server`.
  * `cities`: Description:
    * `id` = `INT unique, auto generated, can’t be null and is a primary key`
    * `state_id` = `INT, can’t be null and must be a FOREIGN KEY that references to id of the states table`
    * `name` = `VARCHAR(256) can’t be null`

* **8. Cities of California**
  * [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql): MySQL script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
  * `The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)`
  * `Results must be sorted in ascending order by `cities.id``
  * `You are not allowed to use the `JOIN` keyword``
  * `The database name will be passed as an argument of the `mysql` command``

* **9. Cities by States**
  * [9-cities_by_state_join.sql](./9-cities_by_state_join.sql): MySQL script that lists all cities contained in the database `hbtn_0d_usa``.
  * Description:
    * `Each record should display: `cities.id` - `cities.name` - `states.name``
    * `Results must be sorted in ascending order by `cities.id``
    * `You can use only one `SELECT` statement``
    * `The database name will be passed as an argument of the `mysql` command`

* **10. Genre ID by show**
  * [10-genre_id_by_show.sql](./10-genre_id_by_show.sql): Import the database dump from `hbtn_0d_tvshows` to your MySQL server: `download``.

  * MySQL script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked`.
  * Description: 
    * `Each record should display: `tv_shows.title` - `tv_show_genres.genre_id``
    * `Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id``
    * `You can use only one `SELECT` statement`
    * `The database name will be passed as an argument of the `mysql` command`

* **11. Genre ID for all shows**
  * [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql): `Import the database dump of `hbtn_0d_tvshows` to your MySQL server: `download` (same as `10-genre_id_by_show.sql`)`.
  * MySQL script that lists all shows contained in the database `hbtn_0d_tvshows`.
  * Description:
    * `Each record should display: `tv_shows.title` - `tv_show_genres.genre_id``.
    * `Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id``
    * `If a show doesn’t have a genre, display `NULL``
    * `You can use only one `SELECT` statement``
    * `The database name will be passed as an argument of the `mysql` command`

* **12. No genre**
  * [12-no_genre.sql](./12-no_genre.sql): `Import the database dump from `hbtn_0d_tvshows` to your MySQL server: `download` (same as `11-genre_id_all_shows.sql`).
  * MySQL script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
  * Description:
    * `Each record should display: `tv_shows.title` - `tv_show_genres.genre_id``
    * `Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id``
    * `You can use only one `SELECT` statement```
    * `The database name will be passed as an argument of the `mysql` command``.

* **13. 
