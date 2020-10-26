#parent local
#def outer() :
#    x = "local"
#    def inner() :
#        nonlocal x
#        x = "nonlocal"
#        print("inner:",x)

#    inner()
#    print("outer:", x)


#outer()

def func1() :
    x = "sai kumar"
    def func2() :
        #nonlocal x
        x = "sai kumar mullapudi"
        print("func2():",x)

    func2()
    print("func1():",x)

func1()





