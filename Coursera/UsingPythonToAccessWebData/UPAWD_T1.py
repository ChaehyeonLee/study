import re
text = "from: emailaddress@dfa.dfa.df fsdf"
result = re.findall('\S+?@\S+?', text)
print(result)