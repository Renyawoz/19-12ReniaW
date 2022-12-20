def lista(*args):
    print(args)

lista()
lista( 1,1 )
lista(  11,11  )
lista(  11111,11111  )
lista(  1111111,11111111  )


def lista(imie,*args):
    print(imie)
    print(args)
lista('YETI')
lista(1)
lista(1,11)
