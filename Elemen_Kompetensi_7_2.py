print ("@@@@@ @   @ @@@@@ @@@@@")
print ("  @   @   @ @     @   @")
print ("  @   @@@@@ @@@@@ @   @")
print ("  @   @   @ @     @   @")
print ("  @   @   @ @@@@@ @@@@@")

string = list(map(str, input("masukan suatu kalimat: ").lower()))

def vokal_kon(n):
  consonan=0
  vokal=0
  for i in range(0, len(string)):
    if string[i]=='a' or string[i]=='i' or string[i]=='u' or string[i]=='e' or string[i]=='o':
      vokal+=1
    else:
      consonan+=1
  print("Jumlah huruf Vokal: ",vokal)
  print("Jumlah huruf konsonan:",consonan)
vokal_kon(string)
