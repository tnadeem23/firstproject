def information(fname,lname,**userinfo):
    individuals = {}
    individuals['fname']=fname
    individuals['lname']=lname
    for key,value in userinfo.items():
        individuals[key]=value
    return individuals