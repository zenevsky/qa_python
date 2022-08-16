# qa_python

# 1. test_init_default_books_rating_value_is_empty_dict()
# “ест провер€ет, что дефолтное значение books_rating == {}

# 2. test_add_new_book_add_book_default_rating_eq_1()
# “ест провер€ет, что дефолтное значение рейтинга добавленной книги == 1

# 3. test_add_new_book_add_the_same_book()
# “ест провер€ет невозможность добавлени€ книги, котора€ уже содержитс€ в books_rating

# 4. test_set_book_rating_set_valid_rating()
# “ест провер€ет выставление валидного рейтинга книге

# 5. test_set_book_rating_set_rating_more_than_10()
# “ест провер€ет невозможность выставлени€ рейтинга больше 10

# 6. test_get_book_rating_get_rating_for_book_that_not_in_list()
# “ест провер€ет, что метод get_book_rating() не возвращает рейтинг, если книга не содержитс€ в books_rating

# 7. test_get_books_with_specific_rating_get_books_with_rating_8()
# “ест провер€ет, что метод get_books_with_specific_rating() возвращает книгу соответствующую рейтингу переданному в аргументе

# 8. test_get_books_rating_get_books_contained_in_books_rating()
# “ест провер€ет, что get_books_rating() возвращает полный список книг, содержащихс€ в books_rating

# 9 .test_add_book_in_favorites_unable_to_add_book_that_not_in_books_rating()
# “ест провер€ет, невозможность добавлени€ книги в favorites, если она не содержитс€ в books_rating

# 10. test_delete_book_from_favorites_delete_book_contained_in_favorites()
# “ест провер€ет, что delete_book_from_favorites удал€ет книгу из favorites, если книга содержитс€ в favorites

# 11. test_get_list_of_favorites_books_get_book_contained_in_favorites()
# “ест провер€ет, что метод get_list_of_favorites возвращает полный список книг, содержащихс€ в favorites