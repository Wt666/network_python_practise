# import pandas as pd
# data1=pd.read_excel('')
# data2=pd.read_excel('')
# a=123456
# stra=str(a)
# b = "{:.2}".format(stra)
# c = "{:.4}".format(stra)
# # list_a=list(a)
# print(b)
# print(c)

# n3=3.14158
# print(n3)
# print(f'2 decimals: {n3:.2f}')
# print(f'n3:.3f')
a=[1,2,3,4]
b=[]
for i in a:
    i=i+2
    # print(i)
    b.append(i)
print(b)
# import this

from matplotlib.pyplot import title
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = "One of Python's strengths is its diverse community."
print(message)

car=['b','bmw','audi']
sentence=f'my first car is '+car[2].title()
sentence1=f'my first car is {car[1].title()}'
print(sentence)
print(sentence1)
