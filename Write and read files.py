fw = open('Sample.txt', 'w')
fw.write('Lets write something in text\n')
fw.write('Hence, we have written\nThank u')
fw.close()

fr = open('Sample.txt', 'r')
read = fr.read()
print(read)
fr.close()

# Here we have written fw for write and fr for read the samplen text file