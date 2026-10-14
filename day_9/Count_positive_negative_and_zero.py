numbers = [12, -7, 0, 15, -20, 0, 44]

positive = 0
negative = 0
zero = 0

for i in numbers:
  if i>0:
    positive=positive+1
  elif i==0:
    zero=zero+1
  else:
    negative=negative+1
    

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)