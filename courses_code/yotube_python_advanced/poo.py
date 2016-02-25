'''docstring c'est important pour 
savoir de quoi il sagit '''


class Banque:
	def __init__(self):
		'''deux variable'''	
		self.nom= ""
		self.balance= 0


	#methodes 
	def ajouter_argent(self, montant):
		self.balance += montant
		print \
		"vous avez ajote {0} $ au compte de {1}"\
		.format(self.balance, self.nom)

	def retirer_argent(self, montant):
		self.balance -= montant
		print \
		"vous avez retirer {0} $ au compte de {1}"\
		.format(montant, self.nom)

	def afficher_balance(self):
		print "Balnace de {0} est de {1}"\
		.format(self.nom, self.balance)


clients={}
continuer = 'o'

while continuer =='o':
	nom = raw_input ("Votre nom : ")
	montant = raw_input("votre montant : ")
	clients[nom] = Banque()
	clients[nom].nom = nom
	clients[nom].balance = montant
	continuer = raw_input ("vous vouler rajouter d'autre personne ? o/n ")
	print ""
print ""

print "la liste de la banque"

for client in clients.values() :
	print "{0} : {1} en banque"\
	.format(client.nom, client.balance)
	




