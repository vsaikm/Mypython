def do_stuff(num):
    try:
        return num + 5
        
    except ValueError as err1:
        return err1
    
    except AssertionError as err2:
        return err2

    

    
