#Write a Python script to concatenate dictionaries and create a new one.

d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}

d4=d1
d4.update(d2)
d4.update(d3)
print(d4)