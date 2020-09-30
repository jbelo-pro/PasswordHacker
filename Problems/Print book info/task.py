def print_book_info(title, author=None, year=None):
    title = f'"{title}"'
    if author or year:
        title = title + ' was written'

    if author:
        title = title + f' by {author}'

    if year:
        title = title + f' in {year}'

    print(title)

# print_book_info('War and Peace', 'Leon Tolstoy', 1869)
# print_book_info('Crime and Punishment', None, 1866)
# print_book_info('The Chronicles of Narnia', 'C. S. Lewis', None)
# print_book_info('Harry Potter', None, None)