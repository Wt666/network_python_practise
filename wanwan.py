# import pandas as pd
# data={
#     'brand':['娃','哇','挖','瓦','🐸'],
#     "A":[1,2,3,4,5],
#     "B":[2,5,7,8,8],
#     "C":[44,55,66,77,88888]

# }
# df=pd.DataFrame(data=data)
# print(df.query('brand =="娃"'))
a= [4]
def h(a):
    a[0]=a[0]+1
k=0
while k<5:
    h(a)
    k+=1
    print(a)