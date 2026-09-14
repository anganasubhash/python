#7. Movie Collection
#Write a function movie_library().
#•  Store movie names.
#•  Use a loop to count movies beginning with 'A'.
#•  Replace one movie.
#•  Reverse the list


def movie_libary():
    count=0
    for i in range(len(movie_name)):
        if movie_name[i][0]=="A":
            count+=1
    print(count)
    movie_name[2]="iron man"
    print(movie_name)
    movie_name.reverse()
    print(movie_name)

movie_name=["Home alone","Mummy2","Spiderman","Anabella"]
movie_libary()