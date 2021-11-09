### Q1

class Book():
    pass

catch22 = Book()
catch22.__dict__['title'] = 'Catch 22'
catch22.__dict__['author'] = 'Joseph Heller'
catch22.__dict__['genre'] = 'Novel'
catch22.__dict__['year_of_publication'] = '1961'
catch22.__dict__['no_of_pages'] = '453'

catch22 = Book()
catch22.title = 'Catch 22'
catch22.author = 'Joseph Heller'
catch22.genre  = 'Novel'
catch22.year_of_publication = '1961'
catch22.no_of_pages = '453'



def mybook (title,author,genre,year_of_publication,no_of_pages):
    newbook = Book()
    newbook.title = title
    newbook.author = author
    newbook.genre = genre
    newbook.year_of_publication = year_of_publication
    newbook.no_of_pages = no_of_pages
    return newbook

catch22 = mybook ('Catch 22','Joseph Heller','Novel','1961','453')

###Q4

class Car():
    pass

mustang = Car()
mustang.maker = 'Ford'
mustang.model = 'Mustang'
mustang.year = '1964'
mustang.price = '50000'
mustang.hp = '300'
mustang.engine = '3800'
mustang.submodel = 'GT'


