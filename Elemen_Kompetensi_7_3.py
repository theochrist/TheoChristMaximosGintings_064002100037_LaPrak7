def main(a):
    if a %3==0:
        a**3 
        print ("Hasil: ",a**3)
    else:
        cek(num)
def cek(a):
    if a %3!=0:
        print ("Hasil : false")
        exit(0)
num=int(input("masukan nilai: "))
main(num)