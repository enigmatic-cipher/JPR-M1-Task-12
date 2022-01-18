"""
Given n as input, print the following pattern.
Input-> n=5
Output-> +1-2+3-4+5=3
"""

n = 5
p1 = "+"
p2 = "-"
st = ""
total = 0
for i in range(1,n+1):
  if(i%2==0):
    total = total-i
    st = st + p2 + str(i)
  else:
    total = total+i
    st = st + p1 + str(i)
print(st,"=",total)
