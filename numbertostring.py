ones=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
elevens=[]
tens=["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

numberInt=int(input("Enter number less than 100"))
numberString=str(numberInt)
if numberInt < 20:
    print(numberInt,":",ones[numberInt-1])
else:
    first_digit = int(numberString[0] ) # This will be '4'
    second_digit = int(numberString[1])
    if second_digit==0:
        print(tens[first_digit-2])
    else:
        print(tens[first_digit - 2], ones[second_digit - 1])

