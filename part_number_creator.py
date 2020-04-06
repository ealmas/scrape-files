package_size=['8']
shematic=['F10','F02','F00','F25']
op_temp=['E','D']
packaging=['B','T']
part_identification=[]
for code0 in package_size:
  for code1 in shematic:
    for code2 in op_temp:
      for code3 in packaging:
        part_identification.append('ALANM100X1'+'-'+code0+code1+code2+code3)
print(part_identification) 