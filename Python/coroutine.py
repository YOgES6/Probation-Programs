def simple_coroutine():
    print("coroutine has been started!")
    while True:
        x = yield "foo"
        print("coroutine received: ", x)
     
 
cr = simple_coroutine()
cr
