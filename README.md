If you wish to try to do something similair to what I have done here, I'll provide some pointers as I couldn't find many reasources online:
- to do a while loop, you can do list(map(lambda x:... , a))
     - this works if a is a list and in the lambda function, you append values to a
- you can also make functions and variables by using the walrus operator (ex. function := lambda x: x**2)
- to chain together instructions, you'll need to put them all inside the lambda function and use a lot of brackets and boolean operators ((a:=1) and (b:=2) and...)
