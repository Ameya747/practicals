def intersection(l1,l2):
  res = []

  for student in l1:
    if student in l2:
      res.append(student)

  return res

def diff(l1,l2):
  res=l2.copy()

  for student in l1:
    if not student in l2:
      res.append(student)

  return res

  def symmetricdiff(l1,l2):
    


a=[1,2,4,5,7,8]
b=[1,4,5,8,4]
c=[4,5,6,2,3]   


print(diff(a,b))
    
  

  
    
  