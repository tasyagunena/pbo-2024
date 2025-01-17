def konversisuhu():
    indeks ={
        "celcius   ": "c",
        "Reamur    ": "r",
        "Farenheit ": "f",
        "kelvin    ": "k",
    } 
    print("=======Indeks Satuan Skala Suhu=======")
    for i in indeks:
        print("Satuan suhu :", i, "\t  indeks : ",  indeks[i])
            
    suhu =  float(input("masukan suhu : "))
    satuan = input ("Masukan indeks satuan skala suhu : ")
        
    if (satuan == "c"):
        print(suhu, "derajat celcius : ")
        print("Reamur = ", (suhu*4/5), "derajat")
        print("Farenheit =  ", (suhu*9/5)+32, "derajat")
        print("Kelvin = ", suhu + 273, "derajat")
    elif(satuan == "r"):
        print(suhu, "derajat reamur : ")
        print("Celcius = ", (suhu*5/4), "derajat")
        print("Farenheit = ", (suhu*9/4)+32, "derajat")
        print("Kelvin = ", (suhu*5/4 + 273, "derajat"))
    elif(satuan == "f"):
        print(suhu, "derajat farenheit : ")
        print("Celcius = ", (5/9)*(suhu-32), "derajat")
        print("Reamur =  ", (4/9 * (suhu-32)), "derajat")
        print("Kelvin = ", (5/9)*(suhu-32)+273, "derajat")
    elif(satuan == "k"):
        print(suhu, "derajat kelvin : ")
        print("Celcius = ", suhu-273, "derajat")
        print("Reamur = ", (4/9 * (suhu-32)), "derajat")
        print("Farenheit = ",  (5/9)*(suhu-32) + 273, "derajat")
        
