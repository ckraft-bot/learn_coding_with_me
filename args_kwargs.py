order_num = [4372 ,9012, 1379, 2468, 6732]

print("listed numbers:")
print(order_num) # listed numbers
print("unpacked numbers:")
print(*order_num) # unpacked numbers

############################## *args ##############################
# first arguement is size of latte
# the *args is the conventinoal name but can be reanmed to *flavors and its a tupple
def order_coffee(size, *flavors): 
    print(f"Ordered a {size} latte with these favlors:")
    # print(flavors)
    for flavor in flavors:
        print(f" - {flavor}")

# first input is size, the rest of the inputs part of the *flavors 
order_coffee('grande', 'vanilla', 'lavender') 


############################## **kwargs ##############################
# first arguement is size of latte
# the *args is the conventinoal name but can be reanmed to *flavors and its a tupple
# the *kwargs is the conventinoal name but can be reanmed to **details and its a tupple
def order_coffee(size, *flavors, **details): 
    print(f"Ordered a {size} latte with these favlors:")
    # print(flavors)
    for flavor in flavors:
        print(f" - {flavor}")
    # print(details)
    print("\nThe detials of our oder are:")
    for key, value in details.items():
        print(f" - {key}: {value}")
    
# first input is size handled by size = 'grande'
# the rest of the inputs are positional arguments placed as tupples handled by *flavors *flavors = 'vanilla', 'lavender'
# deliery and tip are "keyword arguments" or "kwargs" placed in a dictionary as kv pairs and handled by **details = MobileOrder=True, tip=10
order_coffee('grande', 'vanilla', 'lavender', MobileOrder=True, tip=10) 