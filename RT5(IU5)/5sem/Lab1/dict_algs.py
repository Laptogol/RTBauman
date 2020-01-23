def main():
  ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
      "name": "vasja",
      "age": 12,
    },{
      "name": "petja",
      "age": 10,
    }],
  }
  
  darja = {
    "name": "darja",
    "age": 41,
    "children": [{
      "name": "kirill",
      "age": 21,
    },{
      "name": "pavel",
      "age": 15,
    }],
  }
  
  emps = [ivan, darja]
  for parent in emps:
   for child in parent.get('children',()):
    if child.get('age') > 18:
      print (parent.get('name'))
      break


if __name__ == 'builtins':
  main()
