def get_gender(sex = 'None'):
    if sex=='m':
         sex = "male"
# Here sex ix'm' run but showing syntax error, there should be == sign to show is statement
    elif sex=='f':
        sex = "female"
    else:
        sex = "none"
    print(sex)
get_gender('m')
get_gender('f')
get_gender()
# R2

