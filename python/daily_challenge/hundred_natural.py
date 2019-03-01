sum_square_number=0
square_sum_number=0
counter=1
while counter<=100:
    sum_square_number+=counter**2#here we adding the square of every counter value
    square_sum_number+=counter#here we adding the every  counter value
    counter+=1#increment the counter
square_sum_natural_number=square_sum_number**2# here we are doing squaring the sum counter value
print sum_square_number
print square_sum_natural_number
print square_sum_natural_number-sum_square_number