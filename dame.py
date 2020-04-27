# Andronic Alexandra Grupa 231 Problema Dame 

import time
from copy import deepcopy

def mutare(tabla, linie_plecare, coloana_plecare, directie_mutare_sd, directie_mutare_sj, capturare, piesa, verif_piesa_blocata):
	# Explicatie parametri
	# linie_plecare - linia la care se afla piesa pe care vreau s-o mut(daca se poate)
	# coloana_plecare - coloana la care se afla piesa pe care vreau s-a mut(daca se poate)
	# directia_mutare_sd - se refera la directia in care vreau sa mut piesa(in drepta sau in stanga)
	# directia_mutare_sj - daca este piesa de tip JMAX simpla , directia va fi in jos, daca este piesa de tip JMIN simpla va fi in sus
	# capturare - variabila de tip bool ce va fi True doar in cazul in care mutarea va fi de tip capturare, va fi dat ca True, daca se face capturare si False daca nu
	# verif_piesa_blocata -  variabila ce va fi True doar cand apelam aceasta functie din metoda ce verifica daca piesele sunt blocate pentru metoda final

	# variabila de tip boolean ce va deveni True in momentul in care se va realiza mutarea, daca nu se va "schimba" inseamna ca nu s-a putut realiza mutarea data si asa returnam False in loc de matricea modificata
	mutare_realizata = False
	if directie_mutare_sj == 'sus':
		
		if capturare == False:
			
			if directie_mutare_sd == 'dreapta':
				if outside(linie_plecare - 1, coloana_plecare + 1):
					if tabla[linie_plecare - 1][coloana_plecare + 1] == Joc.GOL:
						# se va returna True doar in cazul in care facem aceasta verificare pentru metoda piesa_blocata()
						if verif_piesa_blocata == True:
							return True
						mutare_realizata = True
						tabla[linie_plecare][coloana_plecare] = Joc.GOL
						tabla[linie_plecare - 1][coloana_plecare + 1] = piesa
			elif directie_mutare_sd == 'stanga':
				
				if outside(linie_plecare - 1, coloana_plecare - 1):
					if tabla[linie_plecare - 1][coloana_plecare - 1] == Joc.GOL:
						if verif_piesa_blocata == True:
							return True
						mutare_realizata = True
						tabla[linie_plecare][coloana_plecare] = Joc.GOL
						tabla[linie_plecare - 1][coloana_plecare - 1] = piesa
		elif capturare == True:
			# mutare in sus cu capturare
			if directie_mutare_sd == 'dreapta':
				# capturarea se va face intr-un while deoarece trebuie sa facem toata capturarile posibile de pe o linie
				while outside(linie_plecare - 2, coloana_plecare + 2) and outside(linie_plecare - 1, coloana_plecare + 1) and tabla[linie_plecare - 1][coloana_plecare + 1] != piesa and tabla[linie_plecare - 1][coloana_plecare + 1] != piesa.upper() and tabla[linie_plecare - 1][coloana_plecare + 1] != Joc.GOL and tabla[linie_plecare - 2][coloana_plecare + 2] == Joc.GOL:
				
					if verif_piesa_blocata == True:
						return True
					mutare_realizata = True
					tabla[linie_plecare][coloana_plecare] = Joc.GOL
					tabla[linie_plecare - 1][coloana_plecare + 1] = Joc.GOL
					tabla[linie_plecare - 2][coloana_plecare + 2] = piesa
					linie_plecare -= 2
					coloana_plecare += 2
			elif directie_mutare_sd == 'stanga':
				while outside(linie_plecare - 2, coloana_plecare - 2) and outside(linie_plecare - 1, coloana_plecare - 1) and tabla[linie_plecare - 1][coloana_plecare - 1] != piesa and tabla[linie_plecare - 1][coloana_plecare - 1] != piesa.upper() and tabla[linie_plecare - 1][coloana_plecare - 1] != Joc.GOL and tabla[linie_plecare - 2][coloana_plecare - 2] == Joc.GOL:
					
					if verif_piesa_blocata == True:
						return True
					mutare_realizata = True
					tabla[linie_plecare][coloana_plecare] = Joc.GOL
					tabla[linie_plecare - 1][coloana_plecare - 1] = Joc.GOL
					tabla[linie_plecare - 2][coloana_plecare - 2] = piesa
					linie_plecare -= 2
					coloana_plecare -= 2
	
	elif directie_mutare_sj == 'jos':
		if capturare == False:
			if directie_mutare_sd == 'dreapta':
				# inseamna ca este o mutare simpla in care piesa merge doar o casuta pe diagonala
				if outside(linie_plecare + 1, coloana_plecare + 1):
					if tabla[linie_plecare + 1][coloana_plecare + 1] == Joc.GOL:
						if verif_piesa_blocata == True:
							return True
						mutare_realizata = True
						tabla[linie_plecare][coloana_plecare] = Joc.GOL
						tabla[linie_plecare + 1][coloana_plecare + 1] = piesa
			elif directie_mutare_sd == 'stanga':
				if outside(linie_plecare + 1, coloana_plecare - 1):
					if tabla[linie_plecare + 1][coloana_plecare - 1] == Joc.GOL:
						if verif_piesa_blocata == True:
							return True
						mutare_realizata = True
						tabla[linie_plecare][coloana_plecare] = Joc.GOL
						tabla[linie_plecare + 1][coloana_plecare - 1] = piesa
		elif capturare == True:
			# mutare in sus cu capturare
			if directie_mutare_sd == 'dreapta':
				while outside(linie_plecare + 2, coloana_plecare + 2) and outside(linie_plecare + 1, coloana_plecare + 1) and tabla[linie_plecare + 1][coloana_plecare + 1] != piesa and tabla[linie_plecare + 1][coloana_plecare + 1] != piesa.upper() and tabla[linie_plecare + 1][coloana_plecare + 1] != Joc.GOL and tabla[linie_plecare + 2][coloana_plecare + 2] == Joc.GOL:
					
					if verif_piesa_blocata == True:
						return True
					mutare_realizata = True
					tabla[linie_plecare][coloana_plecare] = Joc.GOL
					tabla[linie_plecare + 1][coloana_plecare + 1] = Joc.GOL
					tabla[linie_plecare + 2][coloana_plecare + 2] = piesa
					linie_plecare += 2
					coloana_plecare += 2
			elif directie_mutare_sd == 'stanga':
				while outside(linie_plecare + 2, coloana_plecare - 2) and outside(linie_plecare + 1, coloana_plecare - 1) and tabla[linie_plecare + 1][coloana_plecare - 1] != piesa and tabla[linie_plecare + 1][coloana_plecare - 1] != piesa.upper() and tabla[linie_plecare + 1][coloana_plecare - 1] != Joc.GOL and tabla[linie_plecare + 2][coloana_plecare - 2] == Joc.GOL:
					
					if verif_piesa_blocata == True:
						return True
					mutare_realizata = True
					tabla[linie_plecare][coloana_plecare] = Joc.GOL
					tabla[linie_plecare + 1][coloana_plecare - 1] = Joc.GOL
					tabla[linie_plecare + 2][coloana_plecare - 2] = piesa
					linie_plecare += 2
					coloana_plecare -= 2

	# daca mutare_realizata a devenit True, inseamna ca putem sa returnam tabla modifica(cu mutarea realizata), in caz contrat returnam False
	if mutare_realizata == True:
		return tabla
	else:
		return False #daca returnam False inseamna ca nu s-a putut realiza mutarea, deci nu avem ce succesori sa returnam din acea pozitie / acea piesa este BLOCATA	
	
			
class Joc:
	"""
	Clasa care defineste jocul. Se va schimba de la un joc la altul.
	"""
	NR_COLOANE = 8
	NR_LINII = 8
	SIMBOLURI_JUC = ['a', 'n']
	JMIN = None
	JMAX = None
	GOL = '.'

	# stabilim configuratia initiala a jocului
	def __init__(self, tabla = None):
		# astfel ca intotdeauna, indiferent de culoare, JMAX va fi in partea de sus a tablei, iar JMIN(omul) in partea de jos(pentru a avea piesele in dreptul sau)
		if tabla == None:
			# daca este prima oara cand initializam tabla
			tabla = [[Joc.GOL for i in range(Joc.NR_COLOANE)] for j in range(Joc.NR_LINII)]
			# piesele calculatorului
			for i in range(3):
				if i % 2 == 0:
					# daca este linie para trebuie sa pun piese doar pe coloane impare
					for j in range(1, Joc.NR_COLOANE, 2):
						tabla[i][j] = self.JMAX
				else:
					# daca este linie impara trebuie sa pun piese doar pe coloane pare
					for j in range(0, Joc.NR_COLOANE, 2):
						tabla[i][j] = self.JMAX
			
			# piesele omului
			for i in range(Joc.NR_LINII - 1, Joc.NR_LINII - 4, -1):
				
				if i % 2 != 0:
					# daca linia este impara trbuie sa pun piese pe pozitii pare
					for j in range(0, Joc.NR_COLOANE, 2):
						tabla[i][j] = self.JMIN
				else:
					for j in range(1, Joc.NR_COLOANE, 2):
						tabla[i][j] = self.JMIN
		
		self.matr = deepcopy(tabla)


	# metoda ce numara piesele de tip PIESA(dat ca parametru) - metoda ce ne va ajuta pentru metoda final() ce verifica daca la un moment dat a castigat cineva
	def nr_piese(self, jucator):
		nrPiese = 0  
		for i in range(Joc.NR_LINII):
			for j in range(Joc.NR_COLOANE):
				if self.matr[i][j] == jucator or self.matr[i][j] == jucator.upper():
					nrPiese += 1
		return nrPiese


	# metoda ce verifica daca n-am iesit din matrice cumva intr-o parcurgere
	def in_matrice(self, linie, coloana):
		return 0 <= linie < Joc.NR_LINII and 0 <= coloana < Joc.NR_COLOANE
	
	def piesa_blocata(self, jucator):

		# pentru toate piesele unul jucator verific daca aceasta ar mai putea face o mutare dintr-un loc, daca NU => acesta este blocat
		for i in range(Joc.NR_LINII):
			for j in range(Joc.NR_COLOANE):
				linie = i
				coloana = j
				# daca este o piesa normala ce n-a devenit rege(insa si daca a devenit rege poate sa mute si corespunzator piesei)
				if self.matr[linie][coloana] == jucator or self.matr[linie][coloana] == jucator.upper():

					if self.matr[linie][coloana] == Joc.JMIN or self.matr[linie][coloana] ==  Joc.JMIN.upper():
						# pentru o piese normala de tip JMIN - se poate muta in "sus"
						if self.in_matrice(linie - 1, coloana + 1):
							if mutare(self.matr, linie, coloana, 'dreapta', 'sus', False, self.matr[linie][coloana], True):	
								return True
							# capturare
							if self.matr[linie - 1][coloana + 1] == Joc.JMAX or self.matr[linie - 1][coloana + 1] == Joc.JMAX.upper():
								if self.in_matrice(linie - 2, coloana + 2):
									if mutare(self.matr, linie, coloana, 'dreapta', 'sus', True, self.matr[linie][coloana], True):
										return True
						if self.in_matrice(linie - 1, coloana - 1):
							if mutare(self.matr, linie, coloana, 'stanga', 'sus', False, self.matr[linie][coloana], True):
								return True
						
							if self.matr[linie - 1][coloana - 1] == Joc.JMAX or self.matr[linie - 1][coloana - 1] == Joc.JMAX.upper():
								if self.in_matrice(linie - 2, coloana - 2):
									if mutare(self.matr, linie, coloana, 'stanga', 'sus', True, self.matr[linie][coloana], True):
										return True

						
					elif self.matr[linie][coloana] == Joc.JMAX or self.matr[linie][coloana] == Joc.JMAX.upper():
						# daca este piesa de tip JMAX poate muta in "jos"
						if self.in_matrice(linie + 1, coloana + 1):
							if mutare(self.matr, linie, coloana, 'dreapta', 'jos', False, self.matr[linie][coloana], True):
								return True
							
							if self.matr[linie + 1][coloana + 1] == Joc.JMIN or self.matr[linie + 1][coloana + 1] == Joc.JMIN.upper():
								if self.in_matrice(linie + 2, coloana + 2):
									if  mutare(self.matr, linie, coloana, 'dreapta', 'jos', True, self.matr[linie][coloana], True):
										return True
						if self.in_matrice(linie + 1, coloana - 1):
							# daca este libera casuta => pot sa mut
							if mutare(self.matr, linie, coloana, 'stanga', 'jos', False, self.matr[linie][coloana], True):
								return True
							
							if self.matr[linie + 1][coloana - 1] == Joc.JMIN or self.matr[linie + 1][coloana - 1] == Joc.JMIN.upper():
								if self.in_matrice(linie + 2, coloana - 2):
									if mutare(self.matr, linie, coloana, 'stanga', 'jos', True, self.matr[linie][coloana], True):
										return True

					if self.matr[linie][coloana] == Joc.JMIN.upper():
						# adaug mutarile inverse pentru regi
						# daca o piesa de tip JMIN este rege atunci poate muta si in "joc"

						if self.in_matrice(linie + 1, coloana + 1):
							if mutare(self.matr, linie, coloana, 'dreapta', 'jos', False, self.matr[linie][coloana], True):
								return True
							
							if self.matr[linie + 1][coloana + 1] == Joc.JMAX or self.matr[linie + 1][coloana + 1] == Joc.JMAX.upper():
								if self.in_matrice(linie + 2, coloana  + 2):
									if mutare(self.matr, linie, coloana, 'dreapta', 'jos', True, self.matr[linie][coloana], True):
										return True
						if self.in_matrice(linie + 1, coloana - 1):
							if mutare(self.matr, linie, coloana, 'stanga', 'jos', False, self.matr[linie][coloana], True):
								return True
							
							if self.matr[linie + 1][coloana - 1] == Joc.JMAX or self.matr[linie + 1][coloana - 1] == Joc.JMAX.upper():
								if self.in_matrice(linie + 2, coloana  - 2):
									if mutare(self.matr, linie, coloana, 'stanga', 'jos', True, self.matr[linie][coloana], True):
										return True
					if self.matr[linie][coloana] == Joc.JMAX.upper():
							
						if self.in_matrice(linie - 1, coloana + 1):
							if mutare(self.matr, linie, coloana, 'dreapta', 'sus', False, self.matr[linie][coloana], True):
								return True
							
							if self.matr[linie - 1][coloana + 1] == Joc.JMIN or self.matr[linie - 1][coloana + 1] == Joc.JMIN.upper():
								if self.in_matrice(linie - 2, coloana  + 2):
									if mutare(self.matr, linie, coloana, 'dreapta', 'sus', True, self.matr[linie][coloana], True):
										return True
						if self.in_matrice(linie - 1, coloana - 1):
							if mutare(self.matr, linie, coloana, 'stanga', 'sus', False, self.matr[linie][coloana], True):
								return True
							
							if self.matr[linie - 1][coloana - 1] == Joc.JMIN or self.matr[linie - 1][coloana - 1] == Joc.JMIN.upper():
								if self.in_matrice(linie - 2, coloana - 2):
									if mutare(self.matr, linie, coloana, 'stanga', 'sus', True, self.matr[linie][coloana], True):
										return True
						
					
		# daca n-a returnat nimic pana acum inseamna ca nu mai am nicio pozitie libera
		return False






	# matoda ce verifica daca cineva a pierdut la un moment dat

	def final(self):
		# se pierde cand
		# 1. Daca un jucator nu mai are piese de mutat => numarul pieselor este 0
		# 2. Un jucator nu mai poate muta nicio piesa => piesele lui sunt blocate

		# Caz 1
		if self.nr_piese(Joc.JMIN) == 0:
			return Joc.JMAX
		if self.nr_piese(Joc.JMAX) == 0:
			return Joc.JMIN
		
		# Caz 2
		blocaj_JMAX = self.piesa_blocata(Joc.JMAX)
		blocaj_JMIN = self.piesa_blocata(Joc.JMIN)
		if blocaj_JMAX == False and blocaj_JMIN == False:
			# inseamna ca ambii jucatori sunt blocati si este remiza
			return 'remiza'
		if blocaj_JMAX == True and blocaj_JMIN == False:
			return Joc.JMAX
		if blocaj_JMAX == False and blocaj_JMIN == True:
			return Joc.JMIN
		# nu s-a ajuns la final -> inca putem sa mai jucam
		return False

	# mutari posibile dintr-o anumita configuratie a jocului

	def mutari_joc(self, jucator):

		l_mutari=[]
		
		for i in range(Joc.NR_LINII):
			for j in range(Joc.NR_COLOANE):
				linie = i
				coloana = j
				
				if self.matr[linie][coloana] == jucator or self.matr[linie][coloana] == jucator.upper():
					
				# daca jucatorul este de tip JMAX indiferent daca a devenit rege sau nu, poate muta in jos
					if self.matr[linie][coloana] == Joc.JMAX or self.matr[linie][coloana] == Joc.JMAX.upper():
						# poate muta doar in jos 
						
						
						# mutare in jos la dreapta(mutare fara capturare)
						if self.in_matrice(linie + 1, coloana + 1):
							# poate muta acolo pentru ca este loc gol
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'jos', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'jos', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
								
							
							
						# mutare in jos la stanga(mutare fara capturare)
						if self.in_matrice(linie + 1, coloana - 1):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'jos', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'jos', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						# mutare in jos la dreapta cu capturare
						if self.in_matrice(linie + 1, coloana + 1) and self.in_matrice(linie + 2, coloana + 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'jos', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'jos', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						# mutare in jos la stanga cu capturare
						if self.in_matrice(linie + 1, coloana - 1) and self.in_matrice(linie + 2, coloana - 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'jos', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'jos', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
					elif self.matr[linie][coloana] == Joc.JMIN or self.matr[linie][coloana] == Joc.JMIN.upper():
						
						# daca jucatorul este de tip JMIN indiferent daca a devenit rege sau nu, poate muta in sus
						if self.in_matrice(linie - 1, coloana + 1):
							
							# poate muta acolo pentru ca este loc gol
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'sus', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'sus', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
								# sa vad daca pot sa capturez ceva din aceasta pozitie
						# mutare in sus la stanga(mutare fara capturare)
						if self.in_matrice(linie - 1, coloana - 1):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'sus', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'sus', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						# mutare in sus la dreapta cu capturare
						if self.in_matrice(linie - 1, coloana + 1) and self.in_matrice(linie - 2, coloana + 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'sus', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'sus', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						# mutare in sus la stanga cu capturare
						if self.in_matrice(linie - 1, coloana - 1) and self.in_matrice(linie - 2, coloana - 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'sus', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'sus', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
					
					# mutari inverse pentru regi
					if self.matr[i] == Joc.JMAX.upper():
						
						if self.in_matrice(linie - 1, coloana + 1):
							
							# poate muta acolo pentru ca este loc gol
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'sus', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'sus', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
								
						# mutare in jos la stanga(mutare fara capturare)
						if self.in_matrice(linie - 1, coloana - 1):
						
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'sus', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'sus', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						# mutare in jos la dreapta cu capturare
						if self.in_matrice(linie - 1, coloana + 1) and self.in_matrice(linie - 2, coloana + 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'sus', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'sus', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						# mutare in jos la stanga cu capturare
						if self.in_matrice(linie - 1, coloana - 1) and self.in_matrice(linie - 2, coloana - 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'sus', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'sus', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
					elif self.matr[i][j] == Joc.JMIN.upper():
						
						
						# mutare in sus la dreapta(mutare fara capturare)
						if self.in_matrice(linie + 1, coloana + 1):
							
							# poate muta acolo pentru ca este loc gol
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'jos', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'jos', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
								# sa vad daca pot sa capturez ceva din aceasta pozitie
						# mutare in sus la stanga(mutare fara capturare)
						if self.in_matrice(linie + 1, coloana - 1):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'jos', False, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'jos', False, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
								
						# mutare in sus la dreapta cu capturare
						if self.in_matrice(linie + 1, coloana + 1) and self.in_matrice(linie + 2, coloana + 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'dreapta', 'jos', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'dreapta', 'jos', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
							
						# mutare in sus la stanga cu capturare
						if self.in_matrice(linie + 1, coloana - 1) and self.in_matrice(linie + 2, coloana - 2):
							
							new_tabla = deepcopy(self.matr)
							if mutare(new_tabla, linie, coloana, 'stanga', 'jos', True, self.matr[linie][coloana], True) != False:
								new_tabla = mutare(new_tabla, linie, coloana, 'stanga', 'jos', True, self.matr[linie][coloana], False)
								l_mutari.append(Joc(new_tabla))
						

		return l_mutari


	def fct_euristica(self):
		return self.nr_piese(Joc.JMAX) - self.nr_piese(Joc.JMIN)

	def estimeaza_scor(self, adancime):
		t_final = self.final()
		if t_final == Joc.JMAX :
			return (9999 + adancime)
		elif t_final == Joc.JMIN:
			return (-9999 - adancime)
		elif t_final == 'remiza':
			return 0
		else:
			return self.fct_euristica()
	
	# metoda ce afiseaza configuratia tablei de joc

	def __str__(self):
		# mai intai concatenez numerele coloanelor(0, Joc.NR_LINII)
		sir = '   '
		for nr_col in range(ord('a'), ord('h') + 1):
			sir += chr(nr_col) + ' '
		sir += '\n'
		
		# trebuie sa pun o linie de "-" ce desparte linia cu litera corespunzatoare coloanei
		sir += "   "
		for _ in range(8):
			sir += "-"
			sir += " "
		sir += '\n'
		for nr_linie in range(self.NR_LINII):
			
			sir += str(nr_linie)
			sir += ' '
			sir += '|'
			for carac in range(self.NR_COLOANE):
				sir += str(self.matr[nr_linie][carac]) + ' '
			sir += '\n'
		return sir


class Stare:
	"""
	Clasa folosita de algoritmii minimax si alpha-beta
	Are ca proprietate tabla de joc
	Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
	De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
	configuratiile posibile in urma mutarii unui jucator
	"""

	ADANCIME_MAX = None

	def __init__(self, tabla_joc, j_curent, adancime, parinte = None, scor = None):
		self.tabla_joc = tabla_joc
		self.j_curent = j_curent

		#adancimea in arborele de stari
		self.adancime = adancime

		#scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
		self.scor = scor

		#lista de mutari posibile din starea curenta
		self.mutari_posibile = []

		#cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
		self.stare_aleasa = None

	def jucator_opus(self):
		if self.j_curent == Joc.JMIN:
			return Joc.JMAX
		else:
			return Joc.JMIN
	
	def mutari(self):

		l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
		juc_opus = self.jucator_opus()
		# pregatim tabla pentru urmatoarea mutare cu toate posibilitatile
		l_stari_mutari = [Stare(mut, juc_opus, self.adancime - 1, parinte = self) for mut in l_mutari]

		return l_stari_mutari


	def __str__(self):
		sir = str(self.tabla_joc) + "\n(Jucatorul curent este: " + self.j_curent + ")"
		return sir



""" Algoritmul MinMax """

def min_max(stare):

	#calculez toate mutarile posibile din starea curenta
	
	if stare.adancime == 0 or stare.tabla_joc.final() != False:
		stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
		return stare

	stare.mutari_posibile = stare.mutari()
	

	#aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
	mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

	if stare.j_curent == Joc.JMAX :
		#daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
		stare.stare_aleasa = max(mutari_scor, key = lambda x: x.scor)
	else:
		#daca jucatorul e JMIN aleg starea-fiica cu scorul minim
		stare.stare_aleasa = min(mutari_scor, key = lambda x: x.scor)

	stare.scor = stare.stare_aleasa.scor
	return stare



def alpha_beta(alpha, beta, stare):
	
	if stare.adancime == 0 or stare.tabla_joc.final() != False:
		stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
		return stare

	if alpha >= beta:
		return stare #este intr-un interval invalid deci nu o mai procesez

	stare.mutari_posibile = stare.mutari()

	if stare.j_curent == Joc.JMAX :
		scor_curent = float('-inf')

		for mut in stare.mutari_posibile:
			#calculeaza scorul
			
			stare_noua = alpha_beta(alpha, beta, mut)

			if (scor_curent < stare_noua.scor):
				stare.stare_aleasa = stare_noua
				scor_curent = stare_noua.scor
			if(alpha < stare_noua.scor):
				alpha = stare_noua.scor
				if alpha >= beta:
					break

	elif stare.j_curent == Joc.JMIN :
		scor_curent = float('inf')

		for mut in stare.mutari_posibile:
			stare_noua = alpha_beta(alpha, beta, mut)

			if (scor_curent > stare_noua.scor):
				stare.stare_aleasa = stare_noua
				scor_curent = stare_noua.scor

			if(beta > stare_noua.scor):
				beta = stare_noua.scor
				if alpha >= beta:
					break

	stare.scor = stare.stare_aleasa.scor

	return stare


def afis_daca_final(stare_curenta):
	final = stare_curenta.tabla_joc.final()
	if(final):
		if (final == "remiza"):
			print("Jocul s-a terminat! Este remiza")
		else:
			print("A castigat " + final)

		return True

	return False

# metoda ce verifica daca linia si coloana au depasit marginile tablei de joc
def outside(linie, coloana):
	return 0 <= linie < Joc.NR_LINII and 0 <= coloana < Joc.NR_COLOANE


# metoda ce transforma piesele de pe ultimul/primul rand in rege/dama
def transformare_dama(tabla, jucator):

	if jucator == Joc.JMIN:
		for coloana in range(Joc.NR_COLOANE):
			if tabla[0][coloana] == jucator:
				tabla[0][coloana] = tabla[0][coloana].upper()
	if jucator == Joc.JMAX:
		for coloana in range(Joc.NR_COLOANE):
			if tabla[7][coloana] == jucator:
				tabla[7][coloana] = tabla[7][coloana].upper()
	return tabla

def main():
	#initializare algoritm
	raspuns_valid = False
	while not raspuns_valid:
		tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
		if tip_algoritm in ['1','2']:
			raspuns_valid = True
		else:
			print("Nu ati ales o varianta corecta.")

	# initializare ADANCIME_MAX
	raspuns_valid = False
	while not raspuns_valid:
		n = input("Care doriti sa fie nivelul de dificultate al jocului:usor(1), mediu(2), greu(3): ")
		# nivelul "adancimii" va creste odata cu nivelul de dificultate pentru precizia jocului
		if n.isdigit():
			if int(n) == 1:
				Stare.ADANCIME_MAX = 2
			if int(n) == 2:
				Stare.ADANCIME_MAX = 3
			if int(n) == 3:
				Stare.ADANCIME_MAX = 4
			raspuns_valid = True
		else:
			print("Trebuie sa introduceti un numar natural nenul.")
	
		

	# initializare jucatori
	[s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
	raspuns_valid = False
	while not raspuns_valid:
		Joc.JMIN = str(input("Doriti sa jucati cu {} sau cu {}? Trebuie sa luati in calcul ca jucatorul cu piesa neagra muta intotdeauna primul: ".format(s1, s2)))
		if (Joc.JMIN in Joc.SIMBOLURI_JUC):
			raspuns_valid = True
		else:
			print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
	Joc.JMAX = s1 if Joc.JMIN == s2 else s2

	#initializare tabla - obiect de tip Joc
	tabla_curenta = Joc()
	print("Tabla initiala este urmatoarea: ")
	print(str(tabla_curenta))

	# creare stare initiala
	# intodeauna incepe sa joace negru
	stare_curenta = Stare(tabla_curenta, 'n', Stare.ADANCIME_MAX)

	linie = -1
	coloana = -1

	while True :
		
		if (stare_curenta.j_curent == Joc.JMIN):
			#muta omul
			# trebuie sa vad daca pot sa mai mut(fac acest lucru cu ajutorul metodei piesa_blocata)
			mutari_disponibile = stare_curenta.tabla_joc.piesa_blocata(Joc.JMIN)
			if mutari_disponibile == False:
				print("Jocul s-a terminat")
				print(f"Jucatorul {stare_curenta.j_curent.juc_opus()} a castigat!")
				break

			# daca nu a intrat in if, inseamna ca pot momentan mai am mutari posibile
			raspuns_valid = False
			iesire = str(input("Doriti sa opriti jocul(y / n)? "))
			if iesire == 'y':
				print("Scorul pentru jucator:", end = "")
				print(12 - stare_curenta.tabla_joc.nr_piese(Joc.JMAX))
				print("Scorul pentru calculator:", end = "")
				print(12 - stare_curenta.tabla_joc.nr_piese(Joc.JMIN))
				break

			while not raspuns_valid:
				try:
					
					t_inainte_jucator = int(round(time.time() * 1000))
					print("Ce piesa vrei sa muti. Alege linia si coloana: ")
					linie = int(input("linie = "))
					coloana =  ord(str(input("coloana = "))) - 97
					
					if outside(linie, coloana):
						# verific daca pozitia pe care am dat-o contine o piesa de culoarea celei pe care am ales-o
						if stare_curenta.tabla_joc.matr[linie][coloana] != Joc.JMIN and stare_curenta.tabla_joc.matr[linie][coloana] != Joc.JMIN.upper():
							print("Acea pozitie nu contine piesa corespunzatoare culorii pe care ati ales-o")
							continue
						# trebuie sa ii dau posibilitatea jucatorului sa aleaga linia si coloana in care doreste sa mute si sa verific daca acea mutare este una valida
						directia = str(input("Directia in care vreau sa mut(sus(s) / jos(j)): "))
						diagonala = str(input("Diagonala pe care vreau sa mut(dreapta(d) / stanga(s)): "))
						capturare = str(input("Doriti sa capturati piesa adversarului (da(y) / nu(n))? "))
						if capturare == 'y':
							capturare = True
						elif capturare == 'n':
							capturare = False
						
						directia = 'sus' if directia == 's' else 'jos'
						diagonala = 'dreapta' if diagonala == 'd' else 'stanga'
						if stare_curenta.tabla_joc.matr[linie][coloana] == Joc.JMIN and directia == 'jos':
							print("Nu ati ales o mutare valida. Piesa nu este rege")
							continue
						
						if mutare(stare_curenta.tabla_joc.matr, linie, coloana, diagonala, directia, capturare, stare_curenta.tabla_joc.matr[linie][coloana], True) == False:
							print("Nu ati ales o miscare valida")
							continue
						
						
						# daca n-a intrat in acel if inseamna ca este o miscare valida
						raspuns_valid = True
						
					else:
						print("Linia sau coloana nu au valori valide")
				
				except ValueError:
					print(f"Linia trebuie sa fie un numar intreg intre (0, {Joc.NR_LINII}), iar coloana o litera intre (a, h)")

			#dupa iesirea din while sigur am validat datele
			#deci pot muta simbolul pe "tabla de joc"

			piesa = stare_curenta.tabla_joc.matr[linie][coloana]
			stare_curenta.tabla_joc.matr = mutare(stare_curenta.tabla_joc.matr, linie, coloana, diagonala, directia, capturare, piesa, False)
			stare_curenta.tabla_joc.matr = transformare_dama(stare_curenta.tabla_joc.matr, Joc.JMIN)

			print("\nTabla dupa mutarea jucatorului")
			print(str(stare_curenta))
			print("Scorul jucatorului este: ", end = "")
			# scorul este reprezentat de cate piese a capturat fiecare jucator
			print(12 - stare_curenta.tabla_joc.nr_piese(Joc.JMAX))
			t_dupa_jucator = int(round(time.time() * 1000))
			print("Jucatorul a gandit timp de " + str(t_dupa_jucator - t_inainte_jucator) + " milisecunde.")
			#S-a realizat o mutare. Schimb jucatorul cu cel opus
			stare_curenta.j_curent = stare_curenta.jucator_opus()

		#--------------------------------
		else: #jucatorul e JMAX (calculatorul)
		#Mutare calculator
			
			#preiau timpul in milisecunde de dinainte de mutare
			t_inainte=int(round(time.time() * 1000))
			if tip_algoritm=='1':
				stare_actualizata = min_max(stare_curenta)
			else: #tip_algoritm==2
				stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)
			
			stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
			stare_curenta.tabla_joc.matr = transformare_dama(stare_curenta.tabla_joc.matr, Joc.JMAX)
			print("Tabla dupa mutarea calculatorului")
			print(str(stare_curenta))
			print("Scorul calculatorului este: ", end = "")
			# scorul este reprezentat de cate piese a capturat fiecare jucator
			print(12 - stare_curenta.tabla_joc.nr_piese(Joc.JMIN))
			
			#preiau timpul in milisecunde de dupa mutare
			t_dupa=int(round(time.time() * 1000))
			print("Calculatorul a \"gandit\" timp de "+str(t_dupa-t_inainte)+" milisecunde.")

			if (afis_daca_final(stare_curenta)):
				break

			#S-a realizat o mutare. Schimb jucatorul cu cel opus
			stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__" :
		t_inainte_joc_total = int(round(time.time() * 1000))
		main()
		t_dupa_joc_total = int(round(time.time() * 1000))
		print("Tot jocul a durat: " + str(t_dupa_joc_total-t_inainte_joc_total) + " milisecunde.")