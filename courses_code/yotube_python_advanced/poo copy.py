class personnage():
	
	def __init__(self, pos, v, p, t, e):
		self.position= pos
		self.vie= v
		self.puissance= p
		self.type= t
		self.endurance= e
##methods 	
	def estvivant(self):
		return self.vie>0
	def sedeplacer (self, dh,dv):
		self.position[0]+=dh
		self.position[1]+=dv
	##https://www.youtube.com/watch?v=-wHd6xtmHBY
	
mus= personnage([0,0],100, 50, "age", 20)	
autreperso= personnage (11,120, 30, "nnn", 50)
print mus.estvivant()
print autreperso.position





#	def direbonjour(self, nom):
#		print "bonjour", nom
#		
##	def chanter(self, paroles):
#		print "lalalalal", paroles 
		
##objtes 
#musicien.direbonjour("mohamed")
#musicien.chanter("llllll") 
#barde= personnage ()
#barde.direbonjour("momo")
#barde.chanter("zzzzzzzzz")