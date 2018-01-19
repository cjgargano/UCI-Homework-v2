USE sakila;

-- Question 1 --

-- * 1a. Display the first and last names of all actors from the table `actor`. 
SELECT first_name, last_name FROM actor;

-- * 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 
SELECT CONCAT(first_name, " ", last_name) AS `Actor Name` FROM actor;
/* -----------------------------------------------------------------*/

-- Question 2 --

-- * 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe."
--       What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name FROM actor
WHERE first_name = 'Joe';

-- * 2b. Find all actors whose last name contain the letters `GEN`:
SELECT * FROM actor
WHERE last_name LIKE '%GEN%';

-- * 2c. Find all actors whose last names contain the letters `LI`.
--       This time, order the rows by last name and first name, in that order:
SELECT * FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- * 2d. Using `IN`, display the `country_id` and `country` columns of the following countries:
--       Afghanistan, Bangladesh, and China:
SELECT country_id, country FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');
/* -----------------------------------------------------------------*/

-- Question 3 --

-- * 3a. Add a `middle_name` column to the table `actor`.
--       Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.
ALTER TABLE actor
ADD middle_name VARCHAR(30) AFTER first_name;

-- * 3b. You realize that some of these actors have tremendously long last names.
--       Change the data type of the `middle_name` column to `blobs`.
ALTER TABLE actor
MODIFY COLUMN middle_name BLOB;

-- * 3c. Now delete the `middle_name` column.
ALTER TABLE actor
DROP COLUMN middle_name;
/* -----------------------------------------------------------------*/

-- Question 4 --

-- * 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, count(last_name) AS last_name_num FROM actor
GROUP BY last_name
ORDER BY last_name_num DESC;

-- * 4b. List last names of actors and the number of actors who have that last name, 
--       but only for names that are shared by at least two actors
SELECT last_name, count(last_name) AS last_name_num FROM actor
GROUP BY last_name
HAVING last_name_num > 1
ORDER BY last_name_num DESC;

-- * 4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, 
--       the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name = 'Williams';

-- * 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct 
--       name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.
--       Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error.
--       BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER!
--       (Hint: update the record using a unique identifier.)
SELECT first_name, CASE
	WHEN first_name = 'GROUCHO' THEN first_name = 'MUCHO GROUCHO'
    WHEN first_name = 'HARPO' THEN first_name = 'GROUCHO'
    END
FROM actor;

SELECT first_name, last_name FROM actor
WHERE first_name LIKE 'GROUCHO' OR first_name = 'HARPO';

/* -----------------------------------------------------------------*/

-- Question 5 --

-- * 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
DESCRIBE address;
/* -----------------------------------------------------------------*/

-- Question 6 --

-- * 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member.
--       Use the tables `staff` and `address`:
SELECT staff.first_name, staff.last_name, address.address FROM staff
LEFT JOIN address ON staff.address_id = address.address_id;

-- * 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`. 
SELECT staff.staff_id, SUM(payment.amount) AS payment_total FROM staff
LEFT JOIN payment ON staff.staff_id = payment.staff_id
WHERE payment.payment_date BETWEEN '2005-08-01 00:00:00' AND '2005-08-31 11:59:59'
GROUP BY staff.staff_id
ORDER BY staff.staff_id;

-- * 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`.  Use inner join.
SELECT film.title, COUNT(film_actor.film_id) AS actors_per_film FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id;

/* NEED TO COMPLETE THIS QUESTION!!!!!! */

-- * 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT count(film_id) FROM inventory
WHERE film_id IN (
	SELECT film_id FROM film
    WHERE title = 'Hunchback Impossible'
);

-- * 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer.
--       List the customers alphabetically by last name:
SELECT customer.customer_id, customer.first_name, customer.last_name, SUM(payment.amount) AS amount FROM customer
LEFT JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY customer.customer_id;
/* -----------------------------------------------------------------*/

-- Question 7 --

-- * 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence.
--       As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity.
-- 		 Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English. 
SELECT title, language_id FROM film
WHERE title LIKE 'K%' OR title LIKE 'Q%' AND language_id IN (
	SELECT language_id FROM language
    WHERE language.name = 'English'
);

-- * 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
SELECT first_name, last_name FROM actor
WHERE actor_id IN (
	SELECT actor_id FROM film_actor
    WHERE film_id IN (
		SELECT film_id FROM film
        WHERE title = "Alone Trip"
	)
);

-- * 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses
-- 		 of all Canadian customers. Use joins to retrieve this information.
SELECT customer.first_name, customer.last_name, customer.email, country.country FROM customer
INNER JOIN address
	ON customer.address_id = address.address_id
INNER JOIN city
	ON address.city_id = city.city_id
INNER JOIN country
	ON city.country_id = country.country_id
    WHERE country.country = 'Canada';

-- * 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion.
--       Identify all movies categorized as famiy films.
SELECT title FROM film
INNER JOIN film_category
	ON film.film_id = film_category.film_id
INNER JOIN category
	ON film_category.category_id = category.category_id
    WHERE category.name = 'Family';

SELECT title FROM film
WHERE film_id IN (
	SELECT film_id FROM film_category
    WHERE category_id IN (
		SELECT category_id FROM category
        WHERE name = "Family"
	)
);

-- * 7e. Display the most frequently rented movies in descending order.
CREATE TEMPORARY TABLE temp1 AS 
SELECT inventory.inventory_id, rental.rental_id AS NumRentals FROM inventory
LEFT JOIN rental ON inventory.inventory_id = rental.inventory_id
ORDER BY NumRentals DESC;

SELECT film.title, temp1.inventory_id, NumRentals FROM film
LEFT JOIN temp1 ON film.film_id = temp1.inventory_id;


-- * 7f. Write a query to display how much business, in dollars, each store brought in.
-- combine 'store' table w/ the payment table???
SELECT store.store_id, SUM(payment.amount) AS total_amt FROM store
JOIN inventory
	ON store.store_id = inventory.store_id
JOIN rental
	ON inventory.inventory_id = rental.inventory_id
JOIN payment
	ON rental.rental_id = payment.rental_id
GROUP BY store.store_id
ORDER BY store.store_id;	

-- * 7g. Write a query to display for each store its store ID, city, and country.
-- combine (address table w/ city table ON address_id) w/ country table on city_id
SELECT store.store_id, city.city, country.country FROM store
LEFT JOIN address 
	ON store.address_id = address.address_id
LEFT JOIN city 
	ON address.city_id = city.city_id
LEFT JOIN country 
	ON city.country_id = country.country_id;

-- * 7h. List the top five genres in gross revenue in descending order.
-- (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT category.name, SUM(payment.amount) AS total_amt FROM category 
JOIN film_category
	ON category.category_id = film_category.category_id
JOIN inventory
	ON film_category.film_id = inventory.film_id
JOIN rental
	ON inventory.inventory_id = rental.inventory_id
LEFT JOIN payment
	ON rental.rental_id = payment.rental_id
GROUP BY category.name
ORDER BY total_amt DESC
LIMIT 5;

/* -----------------------------------------------------------------*/

-- * 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue.
-- Use the solution from the problem above to create a view.
-- If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_genres AS
	SELECT category.name, payment.amount FROM category
	JOIN film_category
		ON category.category_id = film_category.category_id
	JOIN inventory
		ON film_category.film_id = inventory.film_id
	JOIN rental
		ON inventory.inventory_id = rental.inventory_id
	LEFT JOIN payment
		ON rental.rental_id = payment.rental_id
	GROUP BY category.name
	ORDER BY amount DESC;

-- * 8b. How would you display the view that you created in 8a?
SELECT * FROM top_genres;

-- * 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
DROP VIEW top_genres;
