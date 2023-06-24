input()
books = [*input()]
sorted_books = sorted(books)

read = 0
for i, b in enumerate(books):
    s_book = sorted_books.index(b)

    if s_book > i:
        if s_book - i > 5:
            print("A Database Systems student read a book.")
            break

        read += s_book - i
        sorted_books = sorted_books[:i] + [b] + sorted_books[i:s_book] + sorted_books[s_book+1:]
else:
    print(read)
