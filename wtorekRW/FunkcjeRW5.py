def lista(*args):
    print(args)

lista()
lista( 1,1 )
lista(  11,11  )
lista(  11111,11111  )
lista(  1111111,11111111  )


def lista(imie="" ,/,*args, **kwargs):
    print(imie)
    print(args)
    print(kwargs)
lista('YETI')
lista('YETI',1)
lista("Teofil",1, imie ='YETI')
lista('YETI',1,11)
