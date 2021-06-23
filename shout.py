
tokens = {"use": 1, "async": 2, "await": 3, "loop": 4, "if": 5, "else": 6}
variables = {}
def parse(t):
    if len(t) == 1 and t[0].isalpha():
       return variables[t[0]]
    elif t[1] == '=':
       if t[2].isnumeric():
           variables[t[0]] = int(t[2])
       else:
           variables[t[0]] = t[2]
    elif t[0] == 'if':
        pass

print("hello sid")
print("type help for help")
s = ""
while True:
    s = s+input("")
    if len(s) == 1 and s[0] == ';':
        s = ""
        print("no input provided")
    elif s[len(s)-1] == ';':
        s = s.replace(";","")
        t = s.split(" ")
        s = ""
        print("running command")
        output = parse(t)
        if output == None:
            print("output: none")
        else: 
            print("output: ",output)
