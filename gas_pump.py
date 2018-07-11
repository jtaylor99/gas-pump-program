def price_for(gallons):
    ''' int -> float
    Returns the amount of gallons in a money amount

    >>> price_for(15)
    35.1
    >>> price_for(20)
    46.8
    >>> price_for(25)
    58.5
    '''
    return round(gallons * 2.34, 2)


def how_many_gallons(dollars):
    ''' int -> float
    Returns the amount of money into gallons

    >>> how_many_gallons(20)
    8.55
    >>> how_many_gallons(25)
    10.68
    >>> how_many_gallons(40)
    17.09
    '''
    return round(dollars / 2.34, 2)


def write_the_history(payment, dollars, gallons):
    text = '\n {}\n ${} \n {} \n '.format(payment, dollars, gallons)

    with open('history.txt', 'a') as file:
        file.write(text)


def is_valid_gallons(gallons):
    if gallons.isdigit() and gallons != '0':
        return True
    else:
        return False


def input_gallons():
    gallons = input('gallons:').strip()
    while not (is_valid_gallons(gallons)):
        print('Please choose a valid option!')
        gallons = input('gallons:').strip()

    return int(gallons)


def input_dollars():
    while True:
        dollars = input('dollars:').strip()
        if dollars.isdigit():
            return int(dollars)
        else:
            print('Please choose a valid option!')


def is_what_to_do(what_to_do):
    if what_to_do == 'buy gas' or 'shop for food':
        return True
    else:
        return False


def input_what_to_do():
    what_to_do = input('what_to_do').strip()
    while not (is_what_to_do(what_to_do)):
        print('Please choose a valid option!')
        what_to_do = input('Do want to buy gas or shop for food?')
        return what_to_do


def main():
    print('''
            _
                       ,S/  .e.##ee
                     ,SS/_ /#####""
                   ,SSSSSS`|##|
                 ,'|SSSSSS/%##|
                 | ;SSSSS/%%%/ .-""-._                           __..ooo._.sSSSSSSSSS"7.
                 |/SSSSS/%%%/.'       `._ __               _.od888888888888"'  '"SSSSS"
             ___  `"SSS/%%%/"-.,sSSs._   8888o._    __.o888888888""SS""    `-._    `7Sb
      _.sssSSSSSSSSSSS/`%%/ ,sSSSSSSSSS-.888888888888888888888"'.S"         ,SSS""   `7b
   ,+""       ```""SS/%%./,sSSSSSSSS".   `"888888888888888"'.sSS"         ,SS"'        `S.
                    /%%%/sSSSSSSSS"   `s.   `"88888888"'.sSSSS"         ,S"'             7
                   /%%%/ `SSSSSSS$$,..sSS`-.   `"88'.sSSSSSSSS._     ,-'
                  /%%%/    `SSSS$$$$SSS",\\\`-.   `"SSSSSS"  8"""7.-'
                  /`%/      `SS$$$SSS,dP,s.\\//`-.   `SS" ,'`8       ,ee888888ee.
        ,oo8888oo/ /         `"""",d88Pd8888./,-'/`.  `,-._`d'    ,d88888888888888b.
     ,d888888888/ /8b.          d8888Pd8888888bd88b`.  :_._`8   ,888888"'    '""88888.
   ,888P'      / /"888b.       d88888`8888888Pd8888 :  :_`-.( ,d8888.__           7888b.
  d88P        / /   `788b     (88888:. `8888Pd88888 ;  ; `-._ 8888P_Z_.>-""--.._   `8888
 d88'     ,--/ /      `88b     `88888b`. `8P 78888";  ;      `"*88_,"   s88s.       `888b
d88'    ,',$/ /$$$$.   `88b      `8888b `. `"'88"_/_,'`-._         `-.d8"88"8P.      `888.
888    ; ,$$$$$$$$$'    888        `"8'   `---------------`-.._      8888888888       888'
888    : `$$$$$$$':     888                                 '888b`-._8s888888"P      .888'
788.   `  `$$$$'  ;     88P                                  8888.   "8878888P'      d888
 88b    `.  `"' ,'     d88'                                  '888b     '88s8"'     .d888'
 `88b.    `-..-'      d88'                                    '888b.             .dd888'
   788b.            ,888'                                       7888b._       _.d8888P
    `7888oo..__..oo888'                                          `"8888888888888888"'
      `"7888888888P"'                                               `"788 mGk 8P"'

    ''')
    print('Welcome to the Gas Station!')
    what_to_do = input('Do you want to buy gas or shop for food?')
    if what_to_do == 'buy gas':

        payment = input('Would you like to prepay or pay after?')

        if payment == 'prepay':
            dollars = input_dollars()
            gallons = how_many_gallons(dollars)
            print(dollars)
        elif payment == 'pay after':
            gallons = input_gallons()
            dollars = price_for(gallons)
            print(gallons)

        pump = input('Which pump are you on?')
        gas = input(
            'Would you like: \nunleaded:2.34\nplus:2.70\npremium:3.00 \n')

        receipt = input('Would you like a receipt yes or no?')
        if receipt == 'yes':
            print('The Gas Station')
            print('dollars:{}\ngallons:{}'.format(dollars, gallons))
            print('Thank you and you have a good day')
            if receipt == 'no':
                print('Thank you and you have good day!')


if __name__ == '__main__':
    main()
