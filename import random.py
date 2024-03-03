import random
def get_numbers_ticket(min,max,quantity):
    if (min<1 or max>1000 or max<min or quantity not in range(min,max)) or (quantity>(max-min)):
        return 'Error'
    gnlist=[]
    while (len(gnlist)<quantity):
        a=random.randint(min,max)
        if a not in gnlist:
            gnlist.append(a)
    gnlist.sort()
    return gnlist
print(get_numbers_ticket(1,36,6))