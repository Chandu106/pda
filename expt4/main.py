#4a
def return_cost(cost_dict, flavor):
    if flavor in cost_dict:
        return cost_dict[flavor]
    else:
        return 0
flavor_cost_dict = {
    "biriyani": 250,
    "chicken curry": 200,
    "vanilla icecreame": 225
}
flavor = "biriyani"
cost = return_cost(flavor_cost_dict, flavor)
print("The cost of" ,flavor, "is", cost)

flavor = "mint"
cost = return_cost(flavor_cost_dict, flavor)
print("The cost of" ,flavor, "is", cost)

#4b
def character_count():
  string_input=str(input())
  b=[]
  c=[]
  for i in range (len(string_input)):
    d=0
    if string_input[i] not in b:
      b.append(string_input[i])
      d=string_input.count(string_input[i])
      c.append(d)

  result=dict(zip(b,c))
  print(result)
character_count()
