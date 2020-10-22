import matplotlib.pyplot as plt
#database of elements available in shop
directory=   {'milk':[3,16],'rice':[25,53],'banana':[20,5],'salt':[20,10],
        'bread':[12,20],'butter':[19,50],'onion':[10,30],'tomato':[21,15],
        'potato':[15,22],'lays':[20,10],'eggs':[50,5],'wheat':[20,30]}
def itemsList(name,list):
    print('+-+-+-+-+-+-+-+-+-+-+-+')
    print('\t',name)
    print('+-+-+-+-+-+-+-+-+-+-+-+')
    print('\t================================')
    if name=='Stocks' or name=='Available list':
        print('\t|Name|      |Quantity| |Price|')  
    else:
        print('\t|Name|      |Quantity| |Amount|')  
    print('\t================================')
    for k, v in list.items():
            q, price = v
            print ("\t{:<13} {:<9} {:<10}".format(k, q, price))
    print('\t================================')
checkout={}
sales={}
total={}
l=[]
x=0
s=0
sum=0
#banner
print('\t _  __   ____       _     __   __     _ ')   
print('\t| |/ /  |  _ \     / \    \ \ / /    / \ ')  
print('\t| K /   | |R) |   / A \    \ Y /    / A \ ')  
print('\t|   \   |  _ <   / ___ \    | |    / ___ \ ') 
print('\t|_|\_\  |_| \_\ /_/   \_\   |_|   /_/   \_\ ')
print('    The one stop destination to all your grocery needs')
while True:
    #homepage
    c=int(input('\n\t\t\tWelcome❤\n\t  Are you a 1.Customer or 2.Shopkeeper?\n\t\t\t'))
    x=0
    if c==1:
        while x!=1:
                ch=int(input('Enter your choice\n1:Shop\t2:Available list\t3:exit\n'))
                if ch==1:
                    print('*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-\nWelcome to the shopping portal!\n*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-\nEnter help if you need to see Available items\nEnter x when you are finished')
                    while True:
                        entered = input("Enter the item name\t:\t")
                        if(entered)=='x':
                            #to check if the cart is empty                          
                            if not checkout:
                                print('Your cart is empty')
                            else:
                                #bill generation
                                itemsList('bill',checkout)
                                sum=0
                                for k, v in checkout.items():
                                    q, price = v
                                    sum=sum+price
                                print('\tyou need to pay     :     ₹'+str(sum)+'/-')
                                print('\t================================')
                                print('Thanks for shopping with us!\n\n')
                                total={**total,**checkout}
                                checkout.clear()
                                s=0
                                m=input('press 0 for new customer ')
                                #if user enters anything else than 0 he will go to the home page
                                if m!='0':
                                    x=1
                                    break
                        elif entered =='help':
                            #this will forward to display the items present in list
                            ch=2
                            break
                        elif(entered) not in directory:
                            print('Item not found, check your spelling!')
                        else:
                            #this is where we take the quantity of item and proceed the order                
                            quant = int(input("Quantity\t\t:   \t"))
                            if quant>directory[entered][0]:
                                print("Sorry, this item can't be processed only",directory[entered][0],"in stock!")
                            else:
                                #for updating the directoryionary i.e., the database of shop
                                directory[entered][0]= int(directory[entered][0]-quant)
                                if checkout.get(entered)==None: 
                                    checkout[entered]=(quant,int(directory[entered][1]*quant))
                                else:
                                    x,y=checkout[entered]
                                    checkout[entered]=(x+quant,int(directory[entered][1]*(quant+x)))
                                #for keeping sales in track
                                sales[entered]=int(directory[entered][0])
                                #will display remaining stock in shop
                                print("Stock left in",entered,'is',directory[entered][0])
                if ch==2:
                    #will display all items and their quantities available in shop
                    itemsList('Available List',directory)
                else:
                    x=1
                    #this option is to exit the loop
    elif c==2:
        s=0
        while s!=1:
            ch=int(input('\t\t\tEnter your choice\n1:Add items to Stock\t2:View Stocks\t3:View sales\t4:exit\n\t\t\t\t'))
            if ch==1:
                #this piece is for adding a new item to the inventory
                name=input('Enter Name : ')
                quantity=int(input('Enter Quantity : '))
                price=int(input('Enter Price : '))
                directory[name]=[quantity,price]
            elif ch==2:
                itemsList('Stocks',directory)
            elif ch==3:
                #this piece will show the stats of sales happening in the shop
                itemsList('Sales',total)
                sum=0
                for k, v in total.items():
                        q, price = v
                        sum=sum+price
                print('\tTotal sales            ',sum)
                print('\t================================\n')
                m=max(total,key=total.get)
                #this will show the item which was bought the most
                print('\t*********************************')
                print('\t  Most sold item    ',m)
                print('\t*********************************')
                #this will show the items which are out of stock
                for k, v in directory.items():
                    lab,price=v
                    if lab==0:
                        print('\t  ',k,'is out of stock')
                #this piece is to provide a graphical representation about the products sold
                keys=sales.keys() 
                for k, v in total.items():
                        q, price = v
                        l.append(q)
                plt.bar(keys,l)
                plt.title('sales')
                plt.show()
            elif ch==4:
                s=1
