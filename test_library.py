import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()

    #Testy dla Funkcji 1: add_book
    def test_add_new_book(self):
        self.assertTrue(self.lib.add_book("Hobbit", 3))
        self.assertEqual(self.lib.books["Hobbit"]["available"], 3)

    def test_add_existing_book_increases_copies(self):
        self.lib.add_book("Hobbit", 2)
        self.lib.add_book("Hobbit", 3)
        self.assertEqual(self.lib.books["Hobbit"]["available"], 5)

    def test_add_book_empty_title(self):
        with self.assertRaises(ValueError):
            self.lib.add_book("", 2)

    def test_add_book_negative_copies(self):
        with self.assertRaises(ValueError):
            self.lib.add_book("Hobbit", -1)

    #Testy dla Funkcji 2: register_user
    def test_register_user_success(self):
        self.assertTrue(self.lib.register_user("U1", "Jan Kowalski"))
        self.assertIn("U1", self.lib.users)

    def test_register_duplicate_user(self):
        self.lib.register_user("U1", "Jan Kowalski")
        with self.assertRaises(ValueError):
            self.lib.register_user("U1", "Anna Nowak")

    def test_register_empty_id(self):
        with self.assertRaises(ValueError):
            self.lib.register_user("", "Jan Kowalski")

    def test_register_empty_name(self):
        with self.assertRaises(ValueError):
            self.lib.register_user("U2", "")

    #Testy dla Funkcji 3: borrow_book
    def test_borrow_success(self):
        self.lib.add_book("Dune", 1)
        self.lib.register_user("U1", "Jan")
        self.assertTrue(self.lib.borrow_book("U1", "Dune"))
        self.assertEqual(self.lib.books["Dune"]["available"], 0)

    def test_borrow_user_not_found(self):
        self.lib.add_book("Dune", 1)
        with self.assertRaises(ValueError):
            self.lib.borrow_book("U99", "Dune")

    def test_borrow_book_not_found(self):
        self.lib.register_user("U1", "Jan")
        with self.assertRaises(ValueError):
            self.lib.borrow_book("U1", "Nieistniejąca")

    def test_borrow_no_copies_available(self):
        self.lib.add_book("Dune", 1)
        self.lib.register_user("U1", "Jan")
        self.lib.register_user("U2", "Anna")
        self.lib.borrow_book("U1", "Dune")
        with self.assertRaises(ValueError): # Brak kopii dla drugiego
            self.lib.borrow_book("U2", "Dune")

    #Testy dla Funkcji 4: return_book
    def test_return_success(self):
        self.lib.add_book("Dune", 1)
        self.lib.register_user("U1", "Jan")
        self.lib.borrow_book("U1", "Dune")
        self.assertTrue(self.lib.return_book("U1", "Dune"))
        self.assertEqual(self.lib.books["Dune"]["available"], 1)

    def test_return_user_not_found(self):
        with self.assertRaises(ValueError):
            self.lib.return_book("U99", "Dune")

    def test_return_book_not_in_system(self):
        self.lib.register_user("U1", "Jan")
        with self.assertRaises(ValueError):
            self.lib.return_book("U1", "Nieznana Książka")

    def test_return_not_borrowed_by_user(self):
        self.lib.add_book("Dune", 5)
        self.lib.register_user("U1", "Jan")
        with self.assertRaises(ValueError):
            self.lib.return_book("U1", "Dune")

    #Testy dla Funkcji 5: search_book
    def test_search_exact_match(self):
        self.lib.add_book("Wiedźmin", 1)
        self.assertEqual(self.lib.search_book("Wiedźmin"), ["Wiedźmin"])

    def test_search_partial_match(self):
        self.lib.add_book("Harry Potter i Kamień", 1)
        self.assertEqual(self.lib.search_book("Potter"), ["Harry Potter i Kamień"])

    def test_search_case_insensitive(self):
        self.lib.add_book("MATRIX", 1)
        self.assertEqual(self.lib.search_book("matrix"), ["MATRIX"])

    def test_search_no_results(self):
        self.lib.add_book("Wiedźmin", 1)
        self.assertEqual(self.lib.search_book("Gwiezdne Wojny"), [])

if __name__ == '__main__':
    unittest.main()