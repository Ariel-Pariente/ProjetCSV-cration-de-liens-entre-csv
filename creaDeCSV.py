import csv
from math import sqrt
import matplotlib.pyplot as pyplot

#fonction qui calcule du coef de corelation
def coefCorrelation (element1, element2):
    moyenneElement1=sum(element1)/len(element1)
    moyenneElement2=sum(element2)/len(element2)
    #defini le haut du denominateur
    haut=0
    for i in range(len(element1)):
        haut+=(element1[i]-moyenneElement1)*(element2[i]-moyenneElement2)
    #definit le bas du denominateur
    bas=0
    sum1DuBas=0
    sum2DuBas=0
    for a in range(len(element1)):
        sum1DuBas+=(element1[a]-moyenneElement1)**2
        sum2DuBas+=(element2[a]-moyenneElement2)**2
    bas=sqrt((sum1DuBas)*(sum2DuBas))
    coef=haut/bas
    return(coef)

def coefCorelAnneIdhMedail(anne):
#creation d'un nouveau ficher csv avec les pays et leurs nombre de medailes en 1988, 1992, 1998, 2002 et 2010
    MedailBrute=open("medailInchCaMarche.csv","r")
    IDH=open("IDH.csv","r")
    initPays=open("sql-pays.csv","r")

    listeIDH=list(csv.reader(IDH,delimiter=";"))
    listeINIPAYS=list(csv.reader(initPays,delimiter=";"))
    ListeMedailBrute=list(csv.reader(MedailBrute,delimiter=";"))


#modification des nom des pays par leurs initials dans IDH
    for i in range (len(listeIDH)):
        for a in range(len(listeINIPAYS)):
            if listeIDH[i][1]==listeINIPAYS[a][5]:
                listeIDH[i][1]=listeINIPAYS[a][3]


#initialise pour pouvoir faire des operation dessu separé car opperation separé
    dicoPays1988={}
    for el in listeIDH:
        dicoPays1988[el[1]]=0
    for p in ListeMedailBrute:
        if p[1]==str(anne):
            dicoPays1988[p[4]]=0
    for p in ListeMedailBrute:
        if p[1]==str(anne): #si on est bien dans en 1988
            dicoPays1988[p[4]]+=1  #ajoute 1 a au pays aillant une medaill
#on arange les pb
        dicoPays1988v2={}
    for k,v in dicoPays1988.items():
        if k =='GER':
            dicoPays1988v2["DEU"]=v
        elif k =='SUI':
            k="CHE"
            dicoPays1988v2["CHE"]=v
        elif k =='YUG':
            k="MKD"
            dicoPays1988v2["MKD"]=v
        elif k =='TCH':
            k="CZE"
            dicoPays1988v2["CZE"]=v
        elif k =='NED':
            k="NLD"
            dicoPays1988v2["NLD"]=v
        elif k =='URS':
            k="RUS"
            dicoPays1988v2["RUS"]=v
        elif k =='LAT':
            k="LVA"
            dicoPays1988v2["LVA"]=v
        elif k =='SLO':
            k="SVN"
            dicoPays1988v2["SVN"]=v
        elif k =='CRO':
            k="HRV"
            dicoPays1988v2["HRV"]=v
        elif k =='BUL':
            k="BGR"
            dicoPays1988v2["BGR"]=v
        elif k =='DEN':
            k="DNK"
            dicoPays1988v2["DNK"]=v
        elif k =='PRK':
            k="KOR"
            dicoPays1988v2["KOR"]=v
        elif k =='EUN':
            k="RUS"
            dicoPays1988v2["RUS"]=v
        else:
            dicoPays1988v2[k]=v

#creation d'un nouveau fichier avec 2 colomne: l'idh et la medaille qui lui est associé
#d'abord uniquepent les pays et medailes
    ihdSmedail=open("IDHmedailles.csv","w")
    strPaysIdh=""
    for k in dicoPays1988v2:
        strPaysIdh+=k
        strPaysIdh+=";"
        strPaysIdh+=str(dicoPays1988v2[k])
        strPaysIdh+="\n"
    ihdSmedail.write(strPaysIdh)
    ihdSmedail.close()


#ceci etant fait nous passons a la modification des noms de ville par leurs IDH
    ihdSmedail=open("IDHmedailles.csv","r")
    listeIhdSmedail=list(csv.reader(ihdSmedail,delimiter=";"))

    for w in range (len(listeIhdSmedail)):
        for j in range(len(listeIDH)):
            if listeIhdSmedail[w][0]==listeIDH[j][1]:
                listeIhdSmedail[w].append(listeIDH[j][2])
        if listeIhdSmedail[w][0]=="CZE":
            listeIhdSmedail[w].append('0,73')
        if listeIhdSmedail[w][0]=="MKD":
            listeIhdSmedail[w].append('0,54')

    for z in listeIhdSmedail:
        if len(z)!=3:
            listeIhdSmedail.remove(z)

#calcule du coef de correlation
    medail=[]
    listeIDHTrie=[]
    for nk in range (len(listeIhdSmedail)):
        medail.append(float((listeIhdSmedail[nk][1]).replace(',','.')))
        listeIDHTrie.append(float((listeIhdSmedail[nk][2]).replace(',','.')))
    print("recherche en cour...")
    #creation de graph
    
    x=listeIDHTrie
    y=medail
    pyplot.scatter(x,y,s=20,c="m",marker='*')
    
    MedailBrute.close()
    IDH.close()
    initPays.close()
    
    return(coefCorrelation(medail,listeIDHTrie))

def coefCorelationPIBetMedail(anné):
    MedailBrute=open("medailInchCaMarche.csv","r")
    pib=open("pib.csv","r")

    listePib=list(csv.reader(pib,delimiter=";"))
    ListeMedailBrute=list(csv.reader(MedailBrute,delimiter=";"))

#initialise pour pouvoir faire des operation dessu separé car opperation separé

    dicoPays1988={}
    for el in listePib:
        dicoPays1988[el[1]]=0
    for p in ListeMedailBrute:
        if p[1]==str(anné):
            dicoPays1988[p[4]]=0
    for p in ListeMedailBrute:
        if p[1]==str(anné): #si on est bien dans en 1988 ou anné conserné
            dicoPays1988[p[4]]+=1  #aj5ute 1 a au pays aillant une medaill
#on arange les pb
    #met a jour les nouveau codes des pays

    dicoPays1988v2={}
    for k,v in dicoPays1988.items():
        if k =='GER':
            dicoPays1988v2["DEU"]=v
        elif k =='SUI':
            k="CHE"
            dicoPays1988v2["CHE"]=v
        elif k =='YUG':
            k="MKD"
            dicoPays1988v2["MKD"]=v
        elif k =='TCH':
            k="CZE"
            dicoPays1988v2["CZE"]=v
        elif k =='NED':
            k="NLD"
            dicoPays1988v2["NLD"]=v
        elif k =='URS':
            k="RUS"
            dicoPays1988v2["RUS"]=v
        elif k =='LAT':
            k="LVA"
            dicoPays1988v2["LVA"]=v
        elif k =='SLO':
            k="SVN"
            dicoPays1988v2["SVN"]=v
        elif k =='CRO':
            k="HRV"
            dicoPays1988v2["HRV"]=v
        elif k =='BUL':
            k="BGR"
            dicoPays1988v2["BGR"]=v
        elif k =='DEN':
            k="DNK"
            dicoPays1988v2["DNK"]=v
        elif k =='PRK':
            k="KOR"
            dicoPays1988v2["KOR"]=v
        elif k =='EUN':
            k="RUS"
            dicoPays1988v2["RUS"]=v
        else:
            dicoPays1988v2[k]=v

#creation d'un nouveau fichier avec 2 colomne: le pib et la medaille qui lui est associé
#d'abord uniquepent les pays et medailes
    PibSmedail=open("PIBmedailles.csv","w")
    strPaysIdh=""
    for k in dicoPays1988v2:
        strPaysIdh+=k
        strPaysIdh+=";"
        strPaysIdh+=str(dicoPays1988v2[k])
        strPaysIdh+="\n"
    PibSmedail.write(strPaysIdh)
    PibSmedail.close()


    rangPibDeLanne=0
    if anné == 1988:
        rangPibDeLanne=30
    if anné == 1992:
        rangPibDeLanne=34
    if anné == 1998:
        rangPibDeLanne=40
    if anné == 2002:
        rangPibDeLanne=44
    if anné == 2010:
        rangPibDeLanne=52
#ceci etant fait on ajoute le PIB aux villes
    PibSmedail=open("PIBmedailles.csv","r")
    listePIBSmedail=list(csv.reader(PibSmedail,delimiter=";"))
    for w in range (len(listePIBSmedail)):
        for j in range(len(listePib)):
            if listePIBSmedail[w][0]==listePib[j][1]:
                listePIBSmedail[w].append(listePib[j][rangPibDeLanne])
    
    for deu in listePIBSmedail:
        if deu[2]=='':
            deu.pop(2)
    for z in listePIBSmedail:
        if len(z)!=3:
            listePIBSmedail.remove(z)
    for h in listePIBSmedail:
        if len(h)!=3:
            listePIBSmedail.remove(h)
    for h in listePIBSmedail:
        if len(h)!=3:
            listePIBSmedail.remove(h)

    #trie de ma fonction pr pouvoire suprimer les pluys grand
    for loap in listePIBSmedail:
        loap[0],loap[2]=float(loap[2]),loap[0]
    listePIBSmedail.sort()
    for bon in listePIBSmedail:
        bon[2],bon[0]=bon[0],bon[2]
    
    for i in range(2):
        listePIBSmedail.pop(len(listePIBSmedail)-1-i)

#calcule du coef de correlation
    medail=[]
    listePIBTrie=[]
    for i in range (len(listePIBSmedail)):
        medail.append(int(float(listePIBSmedail[i][1])))
        listePIBTrie.append(int(float(listePIBSmedail[i][2])))
    print("recherche en cour...")
    x=listePIBTrie
    y=medail
    pyplot.scatter(x,y,s=20,c="b")
    
    MedailBrute.close()
    pib.close()
    
    return(coefCorrelation(medail,listePIBTrie))

coefcor1988=coefCorelAnneIdhMedail(1988)
coefcor1992=coefCorelAnneIdhMedail(1992)
coefcor1998=coefCorelAnneIdhMedail(1998)
coefcor2002=coefCorelAnneIdhMedail(2002)
coefcor2010=coefCorelAnneIdhMedail(2010)

pyplot.show()

coefcor1988pib=coefCorelationPIBetMedail(1988)
coefcor1992pib=coefCorelationPIBetMedail(1992)
coefcor1998pib=coefCorelationPIBetMedail(1998)
coefcor2002pib=coefCorelationPIBetMedail(2002)
coefcor2010pib=coefCorelationPIBetMedail(2010)

pyplot.show()

print("corelation entre les medaille et le pib =")
moyencoefcorpib=(coefcor1988pib+coefcor1992pib+coefcor1998pib+coefcor2002pib+coefcor2010pib)/5
print(moyencoefcorpib)

print("corelation entre les medaille et l'IDH")
moyencoefcorIDH=(coefcor1988+coefcor1992+coefcor1998+coefcor2002+coefcor2010)/5
print(moyencoefcorIDH)