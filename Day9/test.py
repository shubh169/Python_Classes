auction_dict={'a':10,'b':20}

result=0
for key in auction_dict:
    if auction_dict[key]>result:
        result=auction_dict[key]  
    
print(result)