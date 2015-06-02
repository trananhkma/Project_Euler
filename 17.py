dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 
        8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
        14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
        19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
        60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 1000:'onethousand'}

sum = 0    
def check_99(x):
    sum = 0
    if x in dict:
        sum += len(dict[x])
    elif str(x)[0] == '2':
        sum += len(dict[20]) + len(dict[int(str(x)[1])])
    elif str(x)[0] == '3':
        sum += len(dict[30]) + len(dict[int(str(x)[1])])
    elif str(x)[0] == '4':
        sum += len(dict[40]) + len(dict[int(str(x)[1])])
    elif str(x)[0] == '5':
        sum += len(dict[50]) + len(dict[int(str(x)[1])])    
    elif str(x)[0] == '6':
        sum += len(dict[60]) + len(dict[int(str(x)[1])])    
    elif str(x)[0] == '7':
        sum += len(dict[70]) + len(dict[int(str(x)[1])])    
    elif str(x)[0] == '8':
        sum += len(dict[80]) + len(dict[int(str(x)[1])])    
    elif str(x)[0] == '9':
        sum += len(dict[90]) + len(dict[int(str(x)[1])])   
    return sum


for i in xrange(1, 1001):
    if len(str(i)) == 2:
        sum += check_99(i)
    elif len(str(i)) == 3:
        if str(i)[1:] == '00':
            sum += len(dict[int(str(i)[0])]) + len('hundred')
        else:    
            sum += len(dict[int(str(i)[0])]) + len('hundredand') + check_99(int(str(i)[1:]))
    else:
        sum += check_99(i)

print sum     

# 21124       
