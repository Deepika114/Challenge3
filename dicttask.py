obj={"x":{"y":{"z":"a"}}}

all_keys = []
all_val = ''
def fun(obj):
    for ob in obj:
        all_keys.append(ob)
        if isinstance(obj[ob], dict): 
            global all_val
            all_val = list(obj[ob].values())[0]
            fun(obj[ob])
            
    return 'key = '+'/'.join(all_keys)+'\nvalue = '+all_val

print(fun(obj))