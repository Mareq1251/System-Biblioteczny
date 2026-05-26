class Library:
    def __init__(self):
        # Struktura: 'tytuł': {'copies': int, 'available': int}
        self.books = {}
        # Struktura: 'id': {'name': str, 'borrowed': [lista_tytułów]}
        self.users = {}

    # Funkcja 1: Dodawanie książki
    def add_book(self, title: str, copies: int):
        if not title:
            raise ValueError("Tytuł nie może być pusty.")
        if copies <= 0:
            raise ValueError("Liczba kopii musi być większa od zera.")
        
        if title in self.books:
            self.books[title]['copies'] += copies
            self.books[title]['available'] += copies
        else:
            self.books[title] = {'copies': copies, 'available': copies}
        return True

    # Funkcja 2: Rejestracja czytelnika
    def register_user(self, user_id: str, name: str):
        if not user_id:
            raise ValueError("ID użytkownika nie może być puste.")
        if not name:
            raise ValueError("Nazwa użytkownika nie może być pusta.")
        if user_id in self.users:
            raise ValueError("Użytkownik o tym ID już istnieje.")
        
        self.users[user_id] = {'name': name, 'borrowed': []}
        return True

    # Funkcja 3: Wypożyczanie
    def borrow_book(self, user_id: str, title: str):
        if user_id not in self.users:
            raise ValueError("Nie znaleziono użytkownika.")
        if title not in self.books:
            raise ValueError("Książki nie ma w systemie.")
        if self.books[title]['available'] <= 0:
            raise ValueError("Brak dostępnych egzemplarzy.")
        if title in self.users[user_id]['borrowed']:
            raise ValueError("Użytkownik już wypożyczył tę książkę.")

        self.books[title]['available'] -= 1
        self.users[user_id]['borrowed'].append(title)
        return True

    # Funkcja 4: Zwrot książki
    def return_book(self, user_id: str, title: str):
        if user_id not in self.users:
            raise ValueError("Nie znaleziono użytkownika.")
        if title not in self.books:
            raise ValueError("Książki nie ma w bibliotece.")
        if title not in self.users[user_id]['borrowed']:
            raise ValueError("Ten użytkownik nie wypożyczył tej książki.")

        self.books[title]['available'] += 1
        self.users[user_id]['borrowed'].remove(title)
        return True

    # Funkcja 5: Wyszukiwanie
    def search_book(self, query: str):
        if not query:
            return []
        query_lower = query.lower()
        return [title for title in self.books if query_lower in title.lower()]