
filename = "part_number.csv"
f = open(filename, "w")

headers = "part_number\n"

f.write(headers)

mec_serires=['A1','A2']
shematic=['009','502','805','811']
left_color=['N','A','B']
right_color=['N','A','B']
op_temperature=['CW','EW']
gold_plating=['2']
part_identification=[]
for code0 in mec_serires:
    for code1 in shematic:
        for code2 in left_color:
            for code3 in right_color:
                for code4 in op_temperature:
                    for code5 in gold_plating:
                        part_identification.append('ARJM12'+code0+'-'+code1+'-'+code2+code3+'-'+code4+code5)
print(part_identification) 
print("part_number; " + part_identification) 

f.write(part_identification + "\n")

f.close()