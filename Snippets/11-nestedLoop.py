sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

# nested loop
for location in sales_data:
  print(location)
  for _ in location:
    scoops_sold += _
print(scoops_sold)