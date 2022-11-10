lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))