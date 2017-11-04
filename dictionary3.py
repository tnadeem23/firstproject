cars={
    'Bmw':{
        'Model':'12345',
        'Price':'100000',
        'Type':'Sedan'
    },
    'Mercedes':{
        'Model':'34324',
        'Price':'200000',
        'Type':'SUV'
    },
    'Audi':{
        'Model':'25425',
        'Price':'300000',
        'Type':'Luxury'
    }
}

for name,details in cars.items():
    print('The '+name+' has these specifications :\n')
    for feature,value in details.items():
        print(feature+' = '+value)
    print("\n")