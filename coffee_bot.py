class Order():
    def __init__(self, name, drinks, location, price):
        self.name = name
        self.drinks = drinks
        self.location = location
        self.price = price
    
    def __str__(self):
        return 'Okay, thats one of each: {}, to {}. Coming right up for {}! Total price is ${:.2f}'.format(self.drinks, self.location, self.name, self.price)   # noqa: E501

def coffee_bot():
    print("Welcome to the cafe!")

    order_another = 'y'
    drinks = []
    prices = {'Small' : 2.00, 'Medium' : 2.50, 'Large' : 3.00}
    price = 0.00
    while order_another == 'y':
        size = get_size()
        for key, val in prices.items():
            if size == key:
                price += val
        kind = drink_type()
        temp = hot_cold()
        drink = '{} {} {}'.format(size, temp, kind)
        drinks.append(drink)

        while True:
            order_another = input('Would you like to order another drink?\n [y]\n [n]\n> ')  # noqa: E501
            if order_another in ['y', 'n']:
                break


    name  = input('Can I get your name for the order please?\n> ')
    location = to_go()
    price = price * 1.15
    print(Order(name, drinks, location, price))
    
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')  # noqa: E501
    if res == 'a':
        return 'Small'
    if res == 'b':
        return 'Medium'
    if res == 'c':
        return 'Large'
    else:
        selection_error()
        get_size()
    return res

def selection_error():
    print('Your selection is not one of the options, please select again :)')

def drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')  # noqa: E501
    if res == 'a':
      return 'Brewed Coffee: ' + order_brewed()
    if res == 'b':
        return 'Mocha'
    if res == 'c':
        return 'Latte made with: ' + order_latte()
    else:
        selection_error()
        drink_type()
    return res

def order_latte():
    res = input('And what kind of milk would you like for your Latte? \n[a] 2% Milk \n[b] No-Fat Milk \n[c] Oat Milk \n[d] Almond Milk \n[e] Soy Milk\n> ')    # noqa: E501
    if res == 'a':
        return '2% Milk'
    if res == 'b':
        return 'No-Fat Milk'
    if res == 'c':
        return 'Oat Milk'
    if res == 'd':
        return 'Almond Milk'
    if res == 'e':
        return 'Soy Milk'
    else:
        selection_error()
        order_latte()
    return res

def order_brewed():
    m = input('Would you like any milk in your brewed coffee?\n [y]\n [n]\n> ')
    if m == 'y':
        milk = input('How many milks? (Enter 1, 2, or 3)\n> ')
        if milk in ['1', '2', '3']:
            s = input('What about sugar? \n [y]\n [n]\n> ')
            if s == 'y':
                sugar = input('How many sugars? (Enter 1, 2, or 3)\n> ')
                if sugar in ['1', '2', '3']:
                    return '{} milk(s), and {} sugar(s)'.format(milk, sugar)
                else:
                    selection_error()
                    order_brewed()
            if s == 'n':
                return '{} milk(s), and no sugar'.format(milk)
            else:
                selection_error()
                order_brewed()
        else:
            selection_error()
            order_brewed()
        return milk
    if m == 'n':
        s = input('What about sugar? \n [y]\n [n]\n> ')
        if s == 'y':
            sugar = input('How many sugars? (Enter 1, 2, or 3)\n> ')
            if sugar in ['1', '2', '3']:
                return ' with no milk, and {} sugars'.format(sugar)
            else:
                    selection_error()
                    order_brewed()
        if s == 'n':
            return 'black'
        else:
                selection_error()
                order_brewed()
    else:
        selection_error()
        order_brewed()

def hot_cold():
    res = input('Would you like that\n [a] hot or\n [b] iced\n> ')
    if res == 'a':
        return 'Hot'
    if res == 'b':
        return 'Iced'
    else:
        selection_error()
        hot_cold()
    return res

def to_go():
    res = input('Lastly, would you like that\n [a] Sit In or\n [b] To-Go\n> ')
    if res == 'a':
        return 'sit in'
    if res == 'b':
        return 'go'
    else:
        selection_error()
        to_go()
    return res

coffee_bot()


