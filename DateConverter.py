def main():
    months=("JanFebMarAprMayJunJulAugSepOctNovDec")
    date=input("Enter the date in mm/dd/yy format:")
    month=int(date[0:2])
    

    
    pos=(month-1)*3
    monthsAbbrev=months[pos:pos+3]
    day=int(date[3:5])
    year=(date[6:])
            
    print(monthsAbbrev+".",day,"20"+year)
    

main()
