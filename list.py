letters = ["a", "b", "c","d","e","f"]
cisla = [0,1,2,3,4,5,6,7,8,9]
zeros = ["!","@","_","-","/"]
matrix =[[1,2,3],[4,5,6],[7,8,9]]
pismena = range(30)

second, *other = cisla
print (second)
print (other)

print("pismena: ", letters)
print("Cisla: ",cisla)
print("Znaky: ",zeros)
print("pismena[2] ", letters)
print("cisla[4] ", cisla)
print("zeros[3]: ", zeros)
print("cisla[4]", cisla[4:])
print("cisla[4]", cisla[:4])
print("pismena[4]", letters[:2])
print("pismena[4]", letters[2:])
print("znaky[4]", zeros[3:])
print("znaky[4]", zeros[:3])
print("znaky[4]", zeros[1][:3])
print("znaky[4]", matrix[1:])
print("sucet", letters + cisla)
print(len(cisla+letters))


print("znaky[4]", zeros[::-1])
print("znaky[4]", letters[::-1])
print("znaky[4]", cisla[::-1])
