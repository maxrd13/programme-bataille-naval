import random ##import pour utiliser la librairie random, donc obligatoire pour avoir des coordonée aléatoire 

def l_v_t(liste):
    ''' cette fonction prend en paramètre une liste et renvoie un tuple
    des deux premiere valeur et utiliser par la le dictionnaire d_info pour recuperer
    les coordonnés et les ettre en relation avec les valeur [N,S,E,W] '''
    return liste[0],liste[1]

def cible():
    ''' cette fonction renvoie la liste stock qui contient les coordonné
    de chaque cible utiliser par l'ordinateur et le joueur  '''
    stock=[]
    while len(stock)<5:
        x=random.randint(0,10)
        y=random.randint(0,10)
        if [x,y] in stock:
            x=random.randint(0,10)
            y=random.randint(0,10)
        else:
            stock.append([x,y])
    return stock

def joueur():
    ''' cette fonction demande les coordonner ou le joueur ouhaite attaquer une cible de
    l'ordinateur et la renvoie sous forme d'une liste  '''
    ligne=int(input("Choisis une ligne (entre 0 et 9)"))
    colone=int(input("Choisis une colone (entre 0 et 9)"))
    return [ligne, colone]

def ordi():
    ''' cette fonction renvoie aléatoirement les coordonnées d'attaque de l'ordinateur sur
    les cibles des joueurs '''
    ligne=random.randint(0,10)
    colone=random.randint(0,10)
    while (ligne, colone) in d_info: ## pour ne pas tiré 2 fois les mêmes cordonnées 
        ligne=random.randint(0,10)
        colone=random.randint(0,10)
    return [ligne, colone]

def joueur_1(coord):
    '''cette fonction a pour but de faire jouer la fonction joueur() et de renvoyer si il
    a touché ou non. Puis si il n'a pas touché elle renvoie et affiche la direction dans laquel se
    trouve les cibles de l'ordinateur en donnant leur une direction en fonction de Nord
    Sud Est et West '''
    if coord in l_cible:
        print("Toucher !")
        l_cible.remove(coord)        
    else:
        print ("Rater !")
    N=0
    S=0
    E=0
    W=0
    for i in l_cible: ## permet de renvoyer la position des cibles par rapport à l'endroit ciblé
        if coord[0]>i[0]:
            N=N+1
        elif coord[0]<i[0]:
            S=S+1
        if coord[1]>i[1]:
            W=W+1
        elif coord[1]<i[1]:
            E=E+1
    print ("Nord :",N,",Sud:",S,",Est:",E,",West:",W,)

    
            
def j_ordi(coord_ordi):
    '''cette fonction a pour but de faire jouer la fonction ordi() et de renvoyer si il
    a touché ou non. Puis si il n'a pas touché elle renvoie mais n'affiche pas la
    direction dans laquel se trouve les cibles de l'ordinateur en donnant leur une
    direction en fonction de Nord, Sud, Est et West '''
    if coord_ordi in l_cible_j:
        print ("Il a touché")
        l_cible_j.remove(coord_ordi)    
    else:
        print ("Il a raté")
    N=0
    S=0
    E=0
    W=0
    for i in l_cible:
        if coord_ordi[0]>i[0]:
            N=N+1
        elif coord_ordi[0]<i[0]:
            S=S+1
        if coord_ordi[1]>i[1]:
            W=W+1
        elif coord_ordi[1]<i[1]:
            E=E+1
    return [N,S,E,W]
    
def strat():
    co=0
    cor=0
    ''' cette fonction a pour but d'élaborer une stratégie mais elle n'est pas terminé.
    On souhaitait utiliser le dictionnaire d_info qui récolte les info Nord, Sud, Est et West
    pour pas que l'ordi ne joue aléatoirement. Elle aurais donc due ajouter a la liste
    d_info les coordonner des ligne et colonne ou ne se trouve aucune cible grace au nombre
    de cible qu'on nous indique'''
    ligne=random.randint(0,9)
    colone=random.randint(0,9)
    while (ligne,colone) in d_info: ## pour ne pas tiré 2 fois les mêmes cordonnées 
        ligne=random.randint(0,9)
        colone=random.randint(0,9)
    (ligne2,colone2)=(ligne,colone)
    print(len(l_cible))
    if d_info=={}:
        return[ligne,colone]
    for i in d_info:
        if d_info[i][0]+d_info[i][1]==-2:
            return[ligne,colone]
        if d_info[i][0]+d_info[i][1]==len(l_cible_j):
            co=ligne
        elif d_info[i][2]+d_info[i][3]==len(l_cible_j):
            cor=colone
    if co!=0:
        for n in range(0,10):
            d_info[co,n]=[-1,-1,-1,-1]
    if cor!=0:
        for n in range(0,10):
            d_info[n,cor]=[-1,-1,-1,-1]
    return[ligne,colone]
            
    



### initialisation
l_cible=cible()     ##les cibles que doit toucher le joueur defnie aleatoirement comme cible appartenant a lordinateur
l_cible_j=cible()   ## les cibles que doit toucher l'ordinateur defini aleatoirement comme cible appartenant au joueur
d_info={}   ## dictionnaire qui collecte les info Nord, Sud, Est et West ainsi que les coordonées qui ont déjà été tiré afin de ne pas avoir 2 fois les mêmes
n=0
while l_cible !=[] and l_cible_j !=[]:## déroulé d'une partie sans interruption
    n=n+1
    print(n)
    coord=joueur()  ## donne a coord les valeur que le joueur a defini
    joueur_1(coord) ## la fonction est appeler avc coord comme paramêtre 
    coord_ordi=ordi()   ## donne a coord_ordi les valeur que l'odrinateur à defini aléatoirement
    print("Il joue en",coord_ordi)  ## donne l'info au joueur des coordonné jouer par l'ordinateur
    s_info=j_ordi(coord_ordi)   ## s_info prend les valeur [N,S,E,W] que la fonction j_ordi a definie avec les coord_ordi comme paramêtre
    d_info[l_v_t(coord_ordi)]=s_info ##on ajoute ensuite a d_info les [N,S,E,W] qui sont mise en lien avec les coord_ordi utilisé  
if l_cible==[]: ## condition de fin, si la liste de cible de l'ordinateur est vide
    print ('Bravo tu as gagné') 
elif l_cible_j==[]:## condition de fin, si la liste de cible du joueur est vide
    print ('Ton adversaire a gagné')
## informe le joueur du gagnant de la partie
