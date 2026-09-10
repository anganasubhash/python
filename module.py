#import packagename.modulename.operation

import Functions.operation
data=Functions.operation.add(20,30)
print(data)
print(Functions.operation.sub(20,30))
print(Functions.operation.mul(20,30))
print(Functions.operation.div(20,30))


#import* used to get  all from the file
#not need mention packagename modulename ifwe use 
#from packagename.modulename import*
from Functions.operation import*
print(add(20,30))
print(sub(20,30))
print(mul(20,30))
print(div(20,30))


