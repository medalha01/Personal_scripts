class bookInfo:
    def __init__(self, book_name, author_name, avg_rating):
        self.book_name = book_name
        self.author_name = author_name
        self.avg_rating = avg_rating

    def __str__(self):
        return f"{self.book_name} by {self.author_name}"

    def __repr__(self):
        return f"{self.book_name} by {self.author_name}"

def extract_book_info(line):
    # Extract book name and author name from the line
    parts = line.split('(')
    book_name = parts[0].strip()
    author_name = parts[0].split('by')[0].split('(')[0].strip()
    return book_name, author_name

def main():
    # Open data.txt for reading
    with open('data.txt', 'r', encoding='utf-8') as file:
        list_of_books = list()
        # Open best_books.txt for writing
        with open('best_books.txt', 'w', encoding='utf-8') as output_file:
            previous_lines = list()
            for line in file:
                if line.startswith('avg rating'):
                    # Extract average rating from the line
                    avg_rating = float(line.split('avg rating')[1].split(' —')[0].strip())
                    if avg_rating > 4.25:
                        # If average rating is higher than 4.30, extract book info and write to best_books.txt
                        book_name, author_name = extract_book_info(line)
                        print(previous_lines[-4])
                        print(previous_lines[-2].split('by')[-1])
                        book = bookInfo(previous_lines[-4], previous_lines[-2].split('by')[-1], avg_rating)
                        list_of_books.append(book)
                previous_lines.append(line)
                if len(previous_lines) > 4:
                    previous_lines.pop(0)
            list_of_books.sort(key=lambda x: x.avg_rating, reverse=True)
            for book in list_of_books:
                output_file.write(f"{book}\n")


if __name__ == "__main__":
    main()
