kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
Crorepati=0
Lakhpati=0
Dilwale=0
counter=0
while counter<len(kitna_paisa_hai):
    if kitna_paisa_hai[counter]>=10000000:
        Crorepati+=1
    elif kitna_paisa_hai[counter]>=100000:
        Lakhpati+=1
    else:
        Dilwale+=1
    counter+=1
print Crorepati,"crorepati hai"
print Lakhpati,"lakhpati hai"
print Dilwale,"dilwale hai"