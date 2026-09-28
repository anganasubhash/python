 #Given a matrix (list of lists) [[1,2,3],[4,5,6],[7,8,9]], create a list of the diagonal
#elements
lst1=[[1,2,3],[4,5,6],[7,8,9]]
diagonal = [lst1[i][i] for i in range(len(lst1))]
print(diagonal)