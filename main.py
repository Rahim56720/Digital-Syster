import asyncio


# BOOK CLASS

class Book:
    def __init__(self, book_id: int, title: str):
        self.book_id = book_id
        self.title = title
        self.available = True



# LIBRARY CLASS

class Library:
    def __init__(self):
        self.books = {
            1: Book(1, "Python Basics"),
            2: Book(2, "Data Structures")
        }

    async def borrow_book(self, user_id: int, book_id: int):
        print(f"User {user_id} is trying to borrow Book {book_id}...")

        await asyncio.sleep(1)  # simulate delay

        book = self.books.get(book_id)

        if not book:
            return f"User {user_id} failed: Book not found"

        if not book.available:
            return f"User {user_id} failed: Book {book_id} is not available"

        book.available = False
        return f"User {user_id} successfully borrowed Book {book_id}"

    async def return_book(self, user_id: int, book_id: int):
        print(f"User {user_id} is returning Book {book_id}...")

        await asyncio.sleep(1)

        book = self.books.get(book_id)

        if not book:
            return f"User {user_id} failed: Book not found"

        book.available = True
        return f"User {user_id} returned Book {book_id}"



# MAIN FUNCTION (ASYNC)

async def main():
    library = Library()

    tasks = [
        library.borrow_book(101, 1),
        library.borrow_book(102, 1),
        library.borrow_book(103, 2),
        library.return_book(101, 1),
        library.borrow_book(104, 1),
    ]

    results = await asyncio.gather(*tasks)

    print("\n--- Results ---")
    for result in results:
        print(result)



# RUN PROGRAM

if __name__ == "__main__":
    asyncio.run(main())