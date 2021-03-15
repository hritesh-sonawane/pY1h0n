def title_decorator(print_name_function):
  def wrapper(*args, **kwargs):
    print("Professor:")
    print_name_function(*args, **kwargs)
  return wrapper

@title_decorator
def print_my_name():
  print("Ryuk")

@title_decorator
def print_Ls_name(name):
  print(name)

print_Ls_name("L")
print_my_name()