book={}
book['tom']={
    'name':'tom',
    'address':'1 red street, NY',
    'phone':989898989
}
book['bob']={
    'name':'bob',
    'address':'1 green street, NY',
    'phone':20009101
}
import json
s=json.dumps(book)
file=open("book.txt","w")
file.write(s)
file.close()
book=json.loads(s)#String to json
print (book)