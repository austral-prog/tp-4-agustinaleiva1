def leap_year():
    print("TO DO")
    year = input("ingrese un año:")
    if year % 100 == 0:
        if year % 400 == 0:
            print (f"El año {year} es bisiesto")
    elif year % 4 == 0:
        print (f"El año {year} es bisiesto")
    else:
        print (f"El año {year} no es bisiesto")
        
 
