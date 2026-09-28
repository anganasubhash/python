#Given a list of file names ['report.pdf', 'image.png', 'notes.txt', 'data.csv',
#'photo.jpg'], create a list of only the file extensions
files = ['report.pdf', 'image.png', 'notes.txt', 'data.csv', 'photo.jpg']
extensions = [i.split(".")[1] for i in files]
print(extensions)