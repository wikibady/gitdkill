#-*- coding:utf-8 -*-
from django.shortcuts import render
from library.models import Author
from library.models import Book
from django.http import HttpResponse
from django.shortcuts import render_to_response
 
from django.views.decorators.csrf import csrf_exempt
def index(request):
	return render_to_response('index.html')
def list(request):
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	return render_to_response('index.html',{'AuthorList':lis,'BookList':lis2})
@csrf_exempt
def Add(request):
	return render_to_response('Add.html')
@csrf_exempt
def BookList(request):
	BookList = Book.objects.all()

	return render_to_response('BookList.html',{'BookList':BookList})
@csrf_exempt
def AddBook(request):
	name = request.POST['book_name']
	#ISBN = request.POST['book_ISBN']
	authorID = request.POST['book_authorID']
	publisher = request.POST['book_publisher']
	date = request.POST['book_date']
	price = request.POST['book_price']
	try:
		author = Author.objects.get(AulthorID=authorID)
	except Author.DoesNotExist:
		return render_to_response('AddBook2.html',{'AulthorID':authorID,'book_name':name,'book_publisher':publisher,'book_date':date,'book_price':price})
	else:

		BOOK = Book()
		#BOOK.ISBN = ISBN
		BOOK.Title = name
		BOOK.AulthorID_id = authorID
		BOOK.Publisher =  publisher
		BOOK.PublishDate = date
		BOOK.Price = float(price)
		BOOK.save()
		lis = Author.objects.all()
		lis2 = Book.objects.all()
		return render_to_response('index.html',{'AuthorList':lis,'BookList':lis2})
@csrf_exempt
def AddBook2(request):
	AUTHOR = Author()
	AUTHOR.AulthorID = request.POST['author_ID']
	AUTHOR.Age = request.POST['author_age']
	AUTHOR.Country = request.POST['author_country']
	AUTHOR.Name = request.POST['author_name']
	AUTHOR.save()
	BOOK = Book()
	BOOK.Title = request.POST['book_name']
	BOOK.AulthorID_id = request.POST['author_ID']
	BOOK.Publisher =  request.POST['book_publisher']
	BOOK.PublishDate = request.POST['book_date']
	BOOK.Price = float(request.POST['book_price'])
	BOOK.save()
	BookList = Book.objects.all()
	return render_to_response('BookList.html',{'BookList':BookList})
@csrf_exempt
def DelBook(request):
	Aim = Book.objects.get(ISBN=request.POST['DelBook_ISBN']).delete()
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	return render_to_response('index.html',{'AuthorList':lis,'BookList':lis2})
@csrf_exempt
def UpdateBook(request):
	Aim = Book.objects.get(ISBN=request.POST['DelBook_ISBN'])

	return render_to_response('UpdateBook.html',{'book':Aim})
@csrf_exempt
def UpdateBook2(request):
	publisher = request.POST['book_publisher']
	date = request.POST['book_date']
	price = request.POST['book_price']
	Aim = Book.objects.get(ISBN=request.POST['book_ISBN'])
	Aim.Publisher =  publisher
	Aim.PublishDate = date
	Aim.Price = float(price)
	Aim.save()
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	return render_to_response('index.html',{'AuthorList':lis,'BookList':lis2})
@csrf_exempt
def Find(request):
	word = request.POST['serchinput']
	choice = request.POST['choice']
	if choice == "book":
		try:
			BookAim = Book.objects.filter(Title=word)
		except Book.DoesNotExist:
			return render_to_response('index.html')#这里要加页面
		else:
			if len(BookAim)>0:
				BookAuthor=[]
				for Aim in BookAim:
					BookAuthor.append(Aim.AulthorID)				
				return render_to_response('Find.html',{'Books':BookAim,'KEY':1,'BookAuthor':BookAuthor})#   1-----book  2-----author
			else:
				return render_to_response('index.html')#这里要加页面
	else:
		try:
			AuthorAim = Author.objects.filter(Name=word)
		except Author.DoesNotExist:
			return render_to_response('index.html')#这里要加页面
		else:
			if len(AuthorAim)>0:
				AuthorBooks=[]
				for Aim in AuthorAim:
					AuthorBooks.append(Book.objects.filter(AulthorID_id=Aim.AulthorID))
				return render_to_response('Find.html',{'Authors':AuthorAim,'AuthorBooks':AuthorBooks,'KEY':2,'test':AuthorBooks})
			else:
				return render_to_response('index.html')#这里要加页面
@csrf_exempt
def FindByAuthor(request):
	Aim = Author.objects.filter(Name=request.POST['author_name'])
	BOOKS = []
	for author in Aim:
		BOOKS.append(author.ID.all())
	return render_to_response('FindByAuthor.html',{'Aim':Aim,'BOOKS':BOOKS})