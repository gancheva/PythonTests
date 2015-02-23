def ArithGeo(arr): 
  if len(arr) < 3:
    return '-1'
  
  dif = arr[1] - arr[0]
  div = arr[1] / arr[0]
  arith, geo = True, True

  for i in range (1, len(arr) - 1):
    if arr[i] + dif != arr[i+1]:
      arith = False
    if arr[i] * div != arr[i+1]:
      geo = False
  
  if arith == geo:
    return '-1'
  elif arith:
    return 'Arithmetic'
  else:
    return 'Geometric'


# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeo(raw_input())           
