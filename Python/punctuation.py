
input_string = "Hello, world! Let's remove punctuations from this string."

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punctuations = ""

for char in input_string:
   
    if char not in punctuations:
        no_punctuations += char

print("Original String:", input_string)
print("String without punctuations:", no_punctuations)
