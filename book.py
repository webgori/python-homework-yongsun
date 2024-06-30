class Book():
  def set_info(self, title, author):
    self.title = title
    self.author = author
    
  def print_info(self):
    print(f'책 제목: {self.title}')
    print(f'책 저자: {self.author}')
    
book1 = Book()
book1.set_info('파이썬', '민경태')
book1.print_info()

book2 = Book()
book2.set_info('어린왕자', '생텍쥐페리')
book2.print_info()

book_list = [book1, book2]