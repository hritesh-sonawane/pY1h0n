def title_decorator(print_name_function):
  def wrapper():
    print("Professor:")
    print_name_function()
  return wrapper

@title_decorator
def print_my_name():
  print("Ryuk")

@title_decorator
def print_Ls_name():
  print("L")

print_Ls_name()
print_my_name()