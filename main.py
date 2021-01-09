from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut


app = FastAPI()


@app.get('/')
def home():
    return {'key': 'hello'}


@app.get('/{pk}')
def get_item(pk: int, q: str=None):
    return {'key': pk, "q": q}


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}


@app.post('/book', response_model=Book, response_model_exclude={'pages', 'date'})
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {'item': item, "author": author, 'quant': quantity}


@app.post('/book',  response_model=BookOut)
def get_boot(item: Book, q: str = Query(..., min_length=3, max_length=5, deprecated=True)):
    return BookOut(**item.dict(), id=3)


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1), pages: int = Query(None, gt=10, le=500)):
    return {'pk': pk}