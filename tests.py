from main import BooksCollector


class TestBooksCollector:

    def test_init_default_books_rating_value_is_empty_dict(self):
        collector = BooksCollector()
        assert collector.get_books_rating() == {}

    def test_add_new_book_add_book_default_rating_eq_1(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        assert collector.get_books_rating()['Алхимик'] == 1

    def test_add_new_book_add_the_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Алхимик')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_valid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_rating('Алхимик', 5)
        assert collector.get_books_rating()['Алхимик'] == 5

    def test_set_book_rating_set_rating_more_than_10(self):
        collector = BooksCollector()
        collector.books_rating = {'Алхимик': 1}
        collector.set_book_rating('Алхимик', 11)
        assert collector.books_rating['Алхимик'] == 1

    def test_get_book_rating_get_rating_for_book_that_not_in_list(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Алхимик') is None

    def test_get_books_with_specific_rating_get_books_with_rating_8(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_rating('Алхимик', 7)
        collector.add_new_book('Фауст')
        collector.set_book_rating('Фауст', 8)
        assert 'Фауст' in collector.get_books_with_specific_rating(8)

    def test_get_books_rating_get_books_contained_in_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Фауст')
        assert collector.get_books_rating() == {'Алхимик': 1, 'Фауст': 1}

    def test_add_book_in_favorites_unable_to_add_book_that_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Алхимик')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_delete_book_contained_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_book_in_favorites('Алхимик')
        collector.delete_book_from_favorites('Алхимик')
        assert 'Алхимик' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_get_book_contained_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Фауст')
        collector.add_book_in_favorites('Алхимик')
        collector.add_book_in_favorites('Фауст')
        assert 'Алхимик' and 'Фауст' in collector.get_list_of_favorites_books()