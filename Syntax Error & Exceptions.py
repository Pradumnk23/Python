# tuna = int(input("What is your jersey number\n"))
# print(tuna)
# When i will write string in int valur defined , it is exception ,
# but st the same time if we will write inp ut in place of input it is syntax error..

while True:
    try:
        number = int(input("What is ur fav number?\n"))
        print(24/number)
        break
    except ValueError:
        print("Make sure u entered number")
    except ZeroDivisionError:
        print("Don't take zero")
    except:
        break
    finally:
        print("Loop completed")