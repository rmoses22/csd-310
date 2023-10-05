
# Displaying wishlist user

SELECT user.user_id,user.first_name,user.last_name, book.book_id,book.title,book.author
FROM wishlist
	INNER JOIN user ON wishlist.user_id	= user.user_id
    INNER JOIN book ON wishlist.user_id = book.book_id
WHERE user.user_id = 1;

# Displaying Store location

SELECT store_id, locale from store;


# Displaying All Whatabook books

SELECT book_id, title, author, publication_date from book;

# Displaying All books not present in a user's wishlist

SELECT book_id, title, author, publication_date FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 3);

# Inserting new book into wishlist

INSERT INTO wishlist(user_id, book_id)
    VALUES(4, 5)


# Deleting books from wishlist

DELETE FROM wishlist WHERE user_id = 4 AND book_id = 5;

