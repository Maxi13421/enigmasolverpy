import math
import time

chargrid = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def chartoint(character):
    return chargrid.index(character)%26

def inttochar(integer):
    return chargrid[integer]

  
def classicprint(string):
    for i in range(len(string)):
        print(string[i], end="")
        if ((i+1)%5==0):
            print(" ", end="")




class Enigma:
    def __init__(self,w1,position1,w2,position2,w3,position3,umkehrwalze,steckbrettpaare = []):
        self.walzen = [Walze(w1,chartoint(position1)),Walze(w2,chartoint(position2)),Walze(w3,chartoint(position3)),Walze(umkehrwalze,0)]
        self.steckbrett = Steckbrett(steckbrettpaare)
        
    def walzenschalten(self):
        if(self.walzen[0].position+1 in self.walzen[0].übertragskerbe):
            self.walzen[1].position=(self.walzen[1].position+1)%26
        else:
            if(self.walzen[1].position+1 in self.walzen[1].übertragskerbe):
                self.walzen[1].position=(self.walzen[1].position+1)%26
        if(self.walzen[1].position+1 in self.walzen[1].übertragskerbe):
            self.walzen[2].position=(self.walzen[2].position+1)%26
        self.walzen[0].position=(self.walzen[0].position+1)%26
        
        

    def schlüsselnChar(self,integer):
        self.walzenschalten()
        curint = integer
        curint = (self.steckbrett.verdrahtung[curint]-1)%26
        for i in range(3):
            curint = (self.walzen[i].verdrahtung[(curint+self.walzen[i].position)%26]-1-self.walzen[i].position)%26
        curint = self.walzen[3].verdrahtung[curint]-1
        for i in range(3):
            curint = (self.walzen[2-i].verdrahtung.index((curint+self.walzen[2-i].position)%26+1)-self.walzen[2-i].position)%26
        curint = (self.steckbrett.verdrahtung.index(curint+1))%26
        return curint

    def schlüsselnstr(self,string):
        newstring = ""
        for i in string:
          if(i in chargrid):
            integer = chartoint(i)
            newstring += inttochar(self.schlüsselnChar(integer))
        return newstring
    
          
            
class Steckbrett:
    def __init__(self,paare):
        self.verdrahtung = [i+1 for i in range(26)]
        for i in range(int(len(paare)/2)):
            self.verdrahtung[chartoint(paare[2*i])] = chartoint(paare[2*i+1]) + 1
            self.verdrahtung[chartoint(paare[2*i+1])] = chartoint(paare[2*i]) + 1
    
    

class Walze:
    def __init__(self,nummer,position):
        self.position = position
        if(nummer==1):
            self.verdrahtung=[5,11,13,6,12,7,4,17,22,26,14,20,15,23,25,8,24,21,19,16,1,9,2,18,3,10]
            self.übertragskerbe=[17]
            
        if(nummer==2):
            self.verdrahtung=[1,10,4,11,19,9,18,21,24,2,12,8,23,20,13,3,17,7,26,14,16,25,6,22,15,5]
            self.übertragskerbe=[5]
            
        if(nummer==3):
            self.verdrahtung=[2,4,6,8,10,12,3,16,18,20,24,22,26,14,25,5,9,23,7,1,11,13,21,19,17,15]
            self.übertragskerbe=[22]
            
        if(nummer==4):
            self.verdrahtung=[5,19,15,22,16,26,10,1,25,17,21,9,18,8,24,12,14,6,20,7,11,4,3,13,23,2]
            self.übertragskerbe=[10]
            
        if(nummer==5):
            self.verdrahtung=[22,26,2,18,7,9,20,25,21,16,19,4,14,8,12,24,1,23,13,10,17,15,6,5,3,11]
            self.übertragskerbe=[26]
            
        if(nummer==6):
            self.verdrahtung=[10,16,7,22,15,21,13,6,25,17,2,5,14,8,26,18,4,11,1,19,24,12,9,3,20,23]
            self.übertragskerbe=[13,26] #zwei Kerben!
            
        if(nummer==7):
            self.verdrahtung=[14,26,10,8,7,18,3,24,13,25,19,23,2,15,21,6,1,9,22,12,16,5,11,17,4,20]
            self.übertragskerbe=[13,26] #zwei Kerben!
            
        if(nummer==8):
            self.verdrahtung=[6,11,17,8,20,12,24,15,3,2,10,19,16,4,26,18,1,13,5,23,14,9,21,25,7,22]
            self.übertragskerbe=[13,26] #zwei Kerben!
            
        if(nummer==100):
            self.verdrahtung=[5,10,13,26,1,12,25,24,22,2,23,6,3,18,17,21,15,14,20,19,16,9,11,8,7,4]
        if(nummer==101):
            self.verdrahtung=[25,18,21,8,17,19,12,4,16,24,14,7,15,11,13,9,5,2,6,26,3,23,22,10,1,20]
        if(nummer==102):
            self.verdrahtung=[6,22,16,10,9,1,15,25,5,4,18,26,24,23,7,3,20,11,21,17,19,2,14,13,8,12]
                     
#Enigma1 = Enigma("1","F","4","Z","8","A","B",["A","B","C","D"])
#classicprint(Enigma1.schlüsselnstr("Ein Testsatz mit Sonder- und Leerzeichen."))

def logbd(n,p,x):
    if(x==0):
        return n*math.log(1-p)
    return math.log(math.sqrt(n))+n*math.log(n)-math.log(math.sqrt(2*math.pi*x*(n-x)))-x*math.log(x)-(n-x)*math.log(n-x)+x*math.log(p)+(n-x)*math.log(1-p)

propabilitygrid = [
    0.0648988136775994,
    0.0188415910676902,
    0.0305054331572126,
    0.0506430066792942,
    0.173462266972386,
    0.0165486990329977,
    0.0300069783670621,
    0.0474528960223308,
    0.0752666733127305,
    0.00269165586681288,
    0.0120626059216429,
    0.0342936895623567,
    0.025221812381617,
    0.0974977569534443,
    0.0250224304655568,
    0.00787558568437843,
    0.000199381916060213,
    0.0697836706210747,
    0.0724753264878875,
    0.0613099391885156,
    0.0433655667430964,
    0.00667929418801715,
    0.0188415910676902,
    0.00029907287409032,
    0.000398763832120427,
    0.0112650782574021,

]

#string = "HJAMVEBZLBSZIIPGQWXCIUBJKZJFKXSSKBDSBOAKBJIJUSMHKKWTFIRYGWORKICMBJBMMOHLWEDAYLKOUXSKTLUGMOQGUJZZYBRTQHRBJTAOAONNMTSQCZCYDJCGPBZLGWYNDSGSKTTHFOMGGBBGHHPJXUVYJDCERAWPNHJGPBGKIDHEJANSOXIBDFJVAQTCQDRUKJRYRXRJMTWDKUPGQWTJTPHXWLEYHAXNCGLQIINMNHWSLTRHXLNZYKPHZRITZWGOHGJFITJVYDIOMWWCZUJKSMEPJTKJLAGUAIGPPQLUZTZVJDPGGZYJIZOXCAGNGDVQVEPXKZYXLJZIUZOYNXBBBUGSAWJTTPXBKYSKHPQPZWXPIMJEHUGWKKCWYVZAISDXGJNZPXNQIRCNHMCASXPURODJPMGVZFLJOJKCSLWRQAZJFSINYUPUZLAONTGTZWJSHSMYWP"
#string = "HLPICLOWJQDPOLWXLYINJAHOYIEPZP"
string = "QLVVZIXULGXBPGMJYNLGQAPXCV"
#string = "HEOTNSDUQLVDPIHLLNXZX"
maxprob = [(-100000000000,"")]*100
beststring = ""
bestcomb = []

starttime = time.time()

for aaa in range(3):
    print(str(aaa) + "/3")
    for aab in range(26):
        print("+" + str(aab) + "/26")
        for aac in range(3):
            print("+" + str(aac) + "/3")
            for aad in range(26):
                for aae in range(3):
                    for aaf in range(26):
                        for aag in range(3):
                            newEnigma = Enigma(aaa+1,chargrid[aab],aac+1,chargrid[aad],aae+1,chargrid[aaf],aag+100)
                            newstring = newEnigma.schlüsselnstr(string[0:3000])
                            prob = 0
                            for aba in range(26):
                                prob += logbd(len(newstring),propabilitygrid[aba],newstring.count(chargrid[aba]))
                            if(prob>maxprob[0][0]):
                                bestcomb =  [aaa,aab,aac,aad,aae,aaf,aag]
                            if(prob>maxprob[-1][0]):
                                maxprob.pop(-1)
                                newEnigma = Enigma(aaa+1,chargrid[aab],aac+1,chargrid[aad],aae+1,chargrid[aaf],aag+100)
                                maxprob.append((prob,newEnigma.schlüsselnstr(string)))
                                maxprob.sort(reverse = True, key=lambda x: x[0])
                                print(prob)
                                print(newstring)                                


print("Laufzeit in sek: " + str(time.time()-starttime))
for aaa in bestcomb:
    print(aaa)
for aaa in maxprob:
    print(aaa[0])
    print(aaa[1])

                
