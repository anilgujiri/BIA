# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 09:34:12 2022

@author: AN20259618
"""

products  = {1:["Pepsi",10,38],
             2:["COkaCola",10,40],
             3:["Maaza",10,30],
             4:["Sprite",10,35],
             5:["Redbull",10,100]}

price =0;

while True:
    print("Below are the remaining Products")
    print("ID : Name,Remaining,Quantity,Price")
    
    for k,v in products.items():
        print(f"{k} : {v[0]},{v[1]},{v[2]}")
        
    drink = int(input("Enter the product ID : "))
    quantity = int(input("Enter the quantity : "))
    
    
    price = price + (products[drink][2] * quantity)
    
    print("Your Bill : ",price )
    
    option = input("DO you wish to continue ? ")
    if option == "yes":
        continue;
    elif option == "no":
        break;
    else:
        print("Please type either 'yes' or 'no'")
    