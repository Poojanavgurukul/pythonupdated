magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
counter=0
diagnol_sum1=0
diagnol_sum2=0
while counter<len(magic_square):
        row_sum=0
        column_sum=0
        counter2=0
        diagnol_sum1+=magic_square[counter][counter]
        diagnol_sum2+=magic_square[counter][-counter-1]
        while counter2<len(magic_square[counter]):
            row_sum=row_sum+magic_square[counter][counter2]
            column_sum+=magic_square[counter2][counter2]
            counter2+=1
        counter+=1
        print "row"+str(counter),(row_sum)
        print "column"+str(counter),column_sum
print "Diagnol1",diagnol_sum1
print "Diagnol2",diagnol_sum2
