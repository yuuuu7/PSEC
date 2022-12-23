
import json
  
details = {'Name': "Bob",
          'Age' :28}
  
with open('wordlist.txt', 'w') as convert_file:
     convert_file.write(json.dumps(details))
    