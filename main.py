def Begin():
    print('Hello, user !')
    name = input('Enter your name : ')
    print('Done !')
    password = input('Enter your password : ')
    password2 = input('Repit your password : ')
    if password != password2:
        print('Error')
    country = input('Enter your country : ')
    town = input('Enter your town : ')
    pet = input('Enter your pet or favourite pet : ')
    food = input('Enter your favourite food or dish : ')
    print('Well done!')
    print('Register is ready!')
    print('Your static :')
    print(name)
    print('Country : ',country)
    print('Town : ',town)
    print('Pet : ',pet)
    print('Food : ',food)


Begin()