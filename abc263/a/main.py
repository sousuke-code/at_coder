ls = input().split()
ls.sort()
if (ls[0] == ls[1] == ls[2] and ls[3] == ls[4]):
  print("Yes")
  exit()
print("No")