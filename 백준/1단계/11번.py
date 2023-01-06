a = int(input())
b = input()

rs1 = a * int(b[2])
rs2 = a * int(b[1])
rs3 = a * int(b[0])
rs4 = a * int(b)

print(rs1, rs2, rs3, rs4, sep='\n')