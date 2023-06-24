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


# primeira solução
# verifica se a diferença entre algum dos indices dos livros ordenados
# e desordenados é maior que cinco, caso seja imprime e encerra o programa.
# Conta quantas ordenações do método Bubble Sort são necessárias para
# ordenar os livros.

# input()
# books = [*input()]

# sorted_books = sorted(books)
# for i, b in enumerate(books):
#     if sorted_books.index(b) - i > 5:
#         print("A Database Systems student read a book.")
#         exit(0)

# read = 0
# f = True
# while f:
#     f = False

#     for i in range(len(books)-1):
#         if ord(books[i]) > ord(books[i+1]):
#             books[i], books[i+1] = books[i+1], books[i]
#             read += 1
#             f = True

# print(read)
