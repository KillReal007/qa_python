from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2


    def test_absent_book_has_no_rating(self):
        absent_book = BooksCollector()
        absent_book.add_new_book('Война и мир')
        rating = absent_book.get_book_rating('Гарри Поттер')
        assert rating is None


    def test_adding_books_to_favorites(self):
        adding = BooksCollector()
        adding.add_new_book('Гордость и предубеждение и зомби')
        adding.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert adding.favorites == ['Гордость и предубеждение и зомби']
        assert adding.books_rating == {'Гордость и предубеждение и зомби': 1}

    def test_deleting_a_book_from_favorites(self):
        del_book = BooksCollector()
        del_book.add_new_book('Преступление и наказание')
        del_book.add_book_in_favorites('Преступление и наказание')
        del_book.delete_book_from_favorites('Преступление и наказание')
        assert del_book.favorites == []

    def test_cant_set_rating_less_than_one(self):
        rating_book = BooksCollector()
        rating_book.add_new_book('Мертвые души')
        rating_book.set_book_rating('Мертвые души', 0)
        assert rating_book.books_rating == {'Мертвые души': 1}

    def test_cant_set_rating_greater_than_ten(self):
        rating_book = BooksCollector()
        rating_book.add_new_book('Властелин колец')
        rating_book.set_book_rating('Властелин колец', 11)
        assert rating_book.books_rating == {'Властелин колец': 1}

    def test_get_books_with_specific_rating_fails_if_no_books(self):
        list_of_books = BooksCollector()
        list_of_books.add_new_book('Тихий Дон')
        list_of_books.set_book_rating('Тихий Дон', 2)
        assert list_of_books.get_books_with_specific_rating(3) == []

    def test_get_list_of_favorites_books(self):
        favorites_book = BooksCollector()
        favorites_book.add_new_book('Война и мир')
        favorites_book.add_book_in_favorites('Война и мир')
        assert favorites_book.get_list_of_favorites_books() == ['Война и мир']

    def test_add_book_twice(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Пикник на обочине')
        books_collector.add_new_book('Пикник на обочине')
        assert books_collector.favorites == []
        assert books_collector.books_rating == {'Пикник на обочине': 1}


