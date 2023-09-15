with open('invited_names.txt') as name:
    names = name.readlines()

with open('starting_letter.txt') as f:
    x = f.read()
    for i in names:
        stripped_name = i.strip()
        y = x.replace('[name]',stripped_name)
        print(y)
        with open(f'/letter_for_{stripped_name}','w') as w:
            w.write(y)




