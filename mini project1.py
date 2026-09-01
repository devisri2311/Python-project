product_list=['Apple','Guava','Pineapple','Promogranate']
cost_list=[65,20,50,60]
seling_price=[70,30,60,55]
quantity=[10,20,15,10]
user_list=[]
user_ph=[]
cart_list=[]
cart_price=[]
while True:
    
    print('1.Admin')
    print('2.User')
    print('3.Exit')
    role=int(input('select the role :'))
    if role==3:
        print('Exiting the application')
        break
    elif role not in [1, 2]:
        print("choose correct option")
        continue
    Admin_login='Owner'
    Admin_password='Owner@23'     
    while True:
              
        if role==1:
            mylogin=input('Enter login id:')
            mypassword=input('Enter the password:')
            if Admin_login==mylogin and Admin_password==mypassword:
                print('You are sucessfully login')
                break
            else:
                print('In correct password or user name')
        elif role==2:
             name=input('Enter your name:')
             ph=input('Enter your phone number:')
             break
        else:
            print('Please try again')
    if role==1:
            while True:
                print('1.Add Products')
                print('2.Update Products')
                print('3.Remove Products')
                print('4.View Products')
                print('5.View Users')
                print('6.Revenue')
                print('7.Profit')
                print('8.Exit')
                ch=int(input('Choose one option:'))
                if ch==1:
                    product=input('Enter the product name:')
                    if product in product_list:
                        print('Product is alredy in list')
                        
                    else:
                        qut=float(input('Enter the quantity:'))
                        cost=int(input('Enter the original cost:'))
                        price=int(input('Enter the offer/seling price:'))
                        product_list.append(product)
                        quantity.append(qut)
                        cost_list.append(cost)
                        seling_price.append(price)
                        print('Product details are sucessfully Added')
                    
                    print('product_list',''*10,'quantity',''*10,'cost_list',''*10,'selling_price',''*10)

                    for i in zip(product_list,quantity,cost_list,seling_price):
                        print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}{i[3]: <15}')
                    print("*" * 30)    
                elif ch==2:
                    item=input('Enter the product name:')
                    if item in product_list:
                        idx=product_list.index(item)
                        print('1.Update product')
                        print('2.Update quantity')
                        print('3.Update cost')
                        print('4.Update price')
                        ch=int(input('Choose one option:'))
                        if ch==1:
                            product=input('Enter the product name:')
                            product_list[idx]=product
                            print('Product is succesfully updated')
                        elif ch==2:
                            qut=input('Enter the quantity:')
                            quantity[idx]=qut
                            print('Quantity is succesfully updated')
                        elif ch==3:
                            cost=int(input('Enter the original cost:'))
                            cost_list[idx]=cost
                            print('Cost is sucessfully updated')
                        elif ch==4:
                            price=int(input('Enter the offer/seling price:'))
                            seling_price[idx]=price
                            print('Cost is sucessfully updated')
                        else:
                            print('Choose correct option')
                    else:
                        print('Item is not found')
                    print('product_list',''*10,'quantity',''*10,'cost_list',''*10,'selling_price',''*10)
 
                    for i in zip(product_list,quantity,cost_list,seling_price):
                        print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}{i[3]: <15}')
                    print("*" * 30)
                elif ch==3:
                    item=input('Enter the product name:')
                    if item in product_list:
                        idx=product_list.index(item)
                        product_list.pop(idx)
                        quantity.pop(idx)
                        cost_list.pop(idx)
                        seling_price.pop(idx)
                        print('Product is Remove Successfully')
                    else:
                        print('item is not found')
                    
                        print('Product_list',''*10,'quantity',''*10,'cost_list',''*10,'selling_price',''*1)

                    for i in zip(product_list,quantity,cost_list,seling_price):
                        print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}{i[3]: <15}')
                    print("*" * 30)
                elif ch==4:
                    if len(product_list)==0:
                        print('No product is available')
                    else:
                        
                        print('product_list',''*10,'quantity',''*10,'cost_list',''*10,'selling_price',''*10)

                    for i in zip(product_list,quantity,cost_list,seling_price):
                        print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}{i[3]: <15}')
                    print("*" * 30)
                elif ch==5:
                    print('Users List','phno')
                    for i in zip(user_list,user_ph):
                        print(f'{i[0]: <15}{i[1]: <15}')
                    print("*" * 30) 
                elif ch==6:
                    revenue=0
                    if len(cart_price)==0:
                        print('No purchase made.Revenue:0.00')
                        print("*" * 30)
                    else:
                        for price in cart_price:
                            revenue=revenue+price
                        print("*" * 30)
                        print("Total Revenue=",revenue)
                        print("*" * 30)
                elif ch==7:
                   if not cart_list:
                        print("*" * 30)
                        print('No sales yet. Total Profit = 0')
                        print("*" * 30)
                   else:
                        profit=0
                        for item, qty in zip(cart_list, cart_qut):
                          idx = product_list.index(item)
                          profit=profit+(seling_price[idx]-cost_list[idx])*qty
                        print("*" * 30 )
                        print("Total Profit=",profit)
                        if profit>0:
                            print("Business is in Profit")
                        elif profit<0:
                            print("Business is in Loss")
                        else:
                            print("No Profit No Loss")
                        print("*" * 30)
            
                elif ch==8:
                    print('Exit')
                    print("*" * 30)
                    break
                else:
                    print('Choose correct option:')
                    print("*" * 30)
    elif role==2:
        cart_qut=[]
      
        if name in user_list:
            print('name is alredy in list')
        elif ph in user_ph:
            print('phone number is alredy exists')
        elif len(ph) == 10 and ph.isdigit() and ph[0] in ['9', '8', '7', '6']:
            user_list.append(name)
            user_ph.append(ph)
            print("Valid phone number")
        else:
            print("Invalid phone number")
                
        while True:
            print('1.View Products')
            print('2.Add To Cart')
            print('3.Remove from Cart')
            print('4.view Cart')
            print('5.Checkout')
            print('6.Exit')
            ch=int(input('Choose one option:'))
            if ch==1:
                if len(product_list)==0:
                        print('no prosucts available')
                else:
                    print('product_list',''*10,'selling_price',''*10)
                    for i in zip(product_list,seling_price):
                        print(f'{i[0]: <15}{i[1]: <15}')
                    print("*" * 30)
            elif ch==2:
                product=input('enter the product name:')
                if product in product_list:
                    qut=float(input('enter the quantity :'))
                    idx=product_list.index(product)
                    if qut<=quantity[idx]:
                        price=qut*seling_price[idx]
                        quantity[idx]=quantity[idx]-qut
                        cart_list.append(product)
                        cart_qut.append(qut)
                        cart_price.append(price)
                        print('product is added to cart')
                    else:
                        print('out of stoct')
                else:
                    print('product is not found cart')
                print('cart_list',''*10,'cart_qut',''*10,'cart_price',''*10)
                for i in zip(cart_list,cart_qut,cart_price):
                    print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}')
                print("*" * 30)
            elif ch==3:
                item=input('enter the product name:')
                if item in cart_list:
                    idx=cart_list.index(item)
                    cart_list.pop(idx)
                    cart_qut.pop(idx)
                    cart_price.pop()
                    print('product is Remove Successfully')
                else:
                    print('cart_list',''*10,'cart_qut',''*10,'cart_price',''*10)
                    for i in zip(cart_list,cart_qut,cart_price):
                        print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}')
            elif ch==4:
                if len(cart_list)==0:
                    print('cart is empty')
                else:
                    print('cart_list',''*10,'cart_qut',''*10,'cart_price',''*10)
                    for i in zip(cart_list,cart_qut,cart_price):
                        print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}')
                    print("*" * 30)
            elif ch==5:
                print('*'*10,'Bill','*'*10)
                print('cart_list',''*10,'cart_qut',''*10,'cart_price',''*10)
                for i in zip(cart_list,cart_qut,cart_price):
                    print(f'{i[0]: <15}{i[1]: <15}{i[2]: <15}')
                print('_'*30)
                print(' '*15,'Total=',sum(cart_price))
                print("*" * 30)
                break
            
            elif ch==6:
                 print('Exit')
                 print("*" * 30)
                 break
            else:
                print('choose correct option')
                print("*" * 30)
