global_var = 10

def increment_global():
  global global_var
  global_var += 1

def print_global():
  print(global_var)

#for print
print_global()  
increment_global()
print_global()
increment_global()
print_global()  