input()
books = input()
ord_books = sorted(books)

read = 0
for i in range(len(books)-1):
    if ord(books[i]) > ord(books[i+1]):
        x = 0
        for j in range(i+1, len(books)):
            if ord(books[i]) > ord(books[j]):
                x += 1
            else:
                break
        if x > 5:
            print("A Database Systems student read a book.")
            exit(0)
        read += x
print(read)
