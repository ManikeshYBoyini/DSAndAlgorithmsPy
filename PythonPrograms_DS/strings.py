a_sentence = "Hello team, this is to inform you that I will be out of office today."

print(a_sentence.split())

print(a_sentence.split(","))

split_sentence = a_sentence.split(",")
full_sentence = "-".join(split_sentence)
print(full_sentence)

hello_string = "Hello"

print(hello_string*5)

hello_string_list = ["Hello"]

print(hello_string_list*5)


input_str = ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] 

string_1 = " $ ".join(input_str)
print(string_1)