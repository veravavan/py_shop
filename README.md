# py_shop
This program is based on the project example provided called '7 Shopping Cart', it is a simple grocery shopping game for Programming in Python class.. These were the instructions:
------------------------------------------------------------------------------------------------------------------------
Shopping Cart

The program will load data about possible shopping items from a file.
The file can be a .txt file and contain names and prices for example like this:

apple; 15
bread; 14
beans; 25
milk; 12
pasta; 31
water; 6

The program will allow user to shop by adding items to the shopping cart. Possible items
in the store and their prices should be displayed. The user can then type what they want to buy and how many times.
For example:

What you want to buy?
apple
How many?
3

The items will then be added to a virtual shopping cart.

The user can:
1. add more items to the cart
2. see the contents of their cart, and current total price
3. empty the cart
4. see the shopping list
5. stop shopping (exit the program)




BONUS:
1. Make it so that repeated buys of same item do not show up in the shopping cart multiple times.
	For example, if I buy 5 apples and then buy 10 apples, the shopping cart will show 15 apples and
	not two separate entries or 5 and 10.
2. Make it, so that the user can also save their shopping cart into an output file.
------------------------------------------------------------------------------------------------------------------------

I believe I tweaked it a little bit, but it still has the main functions. The program starts when you run main.py.
There are two classes, Item and ShoppingCart, and the program runs based on the methods in ShoppingCart that manage the
items in the cart.

I have also used some functions from our utilities script from class, but I have kept them in a separate file.

There are 2 files that are needed for the program to run, and those are given here as shopping_list.txt and items.txt.
shopping list is a file of items that the user wants to buy, constructed as name; price; quantity.
items is a file of items that the store offers, and the user can't buy anything else, constructed as name; price.

When the program starts, the user can choose what he wants to do by putting numbers as their choice on the menu.
If a user wants to add or remove an item, he has to type the name and the amount of the item, but the item has to
already exist in the store (from the items.txt file).
The user can also choose to save the things they bought in a new txt file, which will save the item names and amounts.
Enjoy~~
