# Andronic Alexandra - Grupa 231 - Pr_7 - Evadarea lui Mormocel

from collections import namedtuple 
import math
from copy import deepcopy
# Citesc datele de intrare din fisier

frunze = {}
Frunza = namedtuple("Frunza", ("id_frunza", "x", "y", "nr_insecte", "g_max"))
# Deschidem fisierul pentru citire
with open("proiect1.in", "r") as fin:
	raza = float(next(fin))
	greutate_curenta = float(next(fin))
	frunza_start = next(fin).strip()
	for linie in fin:
		id_frunza, x, y, nr_insecte, g_max = linie.split()
		frunze[id_frunza] = Frunza(id_frunza, float(x), float(y), int(nr_insecte), float(g_max))
	

# voi defini cateva functii utile pentru verificari
#
def functia_euristica(x, y, raza):
	# functia euristica este data de cat mai are de parcurs broasca de la pozitia curenta(x, y) pana la mal
	# distanta se calculeaza raportandu-ne la centrul cercului(0, 0)
	return raza - dist_puncte(x, y, 0, 0)

# functie care calculeaza distanta dintre doua puncte pentru a sti daca broasca poate sa sara de la o frunza la alta fara sa moara
def dist_puncte(x1, y1, x2, y2):
	return float(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))



class Nod:
	def __init__(self, frunze, id_frunza_curenta, greutate_curenta):
		self.frunze = frunze # tuplu cu toate frunzele
		self.id_frunza_curenta = id_frunza_curenta # frunza initala pe care se afla broscuta
		self.greutate_curenta = greutate_curenta
		# la fiecare pas(saritura pe alta frunza) trebuie sa avem toate frunzele disponibile, frunza pe care ne aflam in acel moment si greutatea curenta a broscutei
		self.info = (frunze, id_frunza_curenta, greutate_curenta, insecte)
		# functia euristica - distanta de la frunza initala pana la circumferinta
		frunza_curenta = self.frunze[self.id_frunza_curenta]
		self.h = functia_euristica(frunza_curenta.x, frunza_curenta.y, raza)
		
		
		

	
	def __str__ (self):
		return "({}, Greutate = {}, h={})".format(self.frunze[self.id_frunza_curenta],self.greutate_curenta, self.h)

	def __repr__ (self):
		
		return f"({self.frunze[self.id_frunza_curenta]}, Greutate = {self.greutate_curenta}, h = {self.h})"


class Arc:
	def __init__(self, capat, varf, cost):
		self.capat = capat
		self.varf = varf
		self.cost = cost 




""" Clase folosite in algoritmul A* """

class NodParcurgere:
	"""O clasa care cuprinde informatiile asociate unui nod din listele open/closed
		Cuprinde o referinta catre nodul in sine (din graf)
		dar are ca proprietati si valorile specifice algoritmului A* (f si g).
		Se presupune ca h este proprietate a nodului din graf

	"""

	


	def __init__(self, nod_graf, parinte = None, g = 0, f = None):
		self.nod_graf = nod_graf  	# obiect de tip Nod
		self.parinte = parinte  	# obiect de tip Nod
		self.g = g  	# costul drumului de la radacina pana la nodul curent
		if f is None :
			self.f = self.g + self.nod_graf.h
		else:
			self.f = f


	def drum_arbore(self):
		"""
			Functie care calculeaza drumul asociat unui nod din arborele de cautare.
			Functia merge din parinte in parinte pana ajunge la radacina
		"""
		nod_c = self
		# lista cu drumul
		drum = [nod_c]
		while nod_c.parinte is not None :
			drum = [nod_c.parinte] + drum
			nod_c = nod_c.parinte
		return drum


	def contine_in_drum(self, nod):
		"""
			Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
			Verificarea se face mergand din parinte in parinte pana la radacina
			Se compara doar informatiile nodurilor (proprietatea info)
			Returnati True sau False.

			"nod" este obiect de tip Nod (are atributul "nod.info")
			"self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
		"""
		### TO DO ... DONE
		nod_c = self
		while nod_c.parinte is not None :
			if nod.info == nod_c.nod_graf.info:
				return True
			nod_c = nod_c.parinte
		return False


	#se modifica in functie de problema
	def expandeaza(self):
		
		"""Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
		si sa returnati o lista de tupluri (nod_fiu, cost_muchie_tata_fiu),
		sau lista vida, daca nu exista niciunul.
		(Fiecare tuplu contine un obiect de tip Nod si un numar.)"""
		
		### TO DO ... DONE
		l_succesori = []
		
		
		frunze, id_frunza_curenta, greutate_curenta = self.nod_graf.info
		# trebuie sa aflu frunza pe care sunt(Tuplul corespunzator ei)
		frunza_curenta = frunze[id_frunza_curenta]

		
		for frunza in frunze.values():
			
			if frunza.id_frunza == frunza_curenta.id_frunza:
				continue
			# nu se poate sari deloc pe o frunza daca greutatea broastei adunate cu numarul de insecte de pe frunza depaseste greutatea maxima pe care o poate sustine frunza
			
			for insecte in range(0, frunza_curenta.nr_insecte + 1):
				
				greutate_noua = greutate_curenta + insecte
				
				if dist_puncte(frunza_curenta.x, frunza_curenta.y, frunza.x, frunza.y) > greutate_noua / 3:
					# print()
					# print(f"{dist_puncte(frunza_curenta.x, frunza_curenta.y, frunza.x, frunza.y)} > {greutate_noua / 3}")
					
					# print(frunza)
					# print("Frunza asta nu-i buna pentru frunza asta")
					# print(frunza_curenta)
					# print("deoarece distanta nu este buna")
					# print(dist_puncte(frunza_curenta.x, frunza_curenta.y, frunza.x, frunza.y))
					# print("greutatea fiind asta")
					# print(greutate_noua)
					# print()
					continue
				# se scade 1 la fiecare salt
				greutate_noua -= 1
				# nu am cum sa sar pe acea frunza
				if greutate_noua > frunza.g_max:
					continue
				if greutate_noua == 0:
					continue
				# print()
				# print("Sunt la frunza asta", end = " ")
				# print(frunza_curenta)
				# print("si incerc sa sar pe frunza asta", end = " ")
				# print(frunza)
				# print("si am greutatea asta", end = " ")
				# print(greutate_noua)
				# print("distanta dintre frunze fiind")
				# print(dist_puncte(frunza_curenta.x, frunza_curenta.y, frunza.x, frunza.y))
				# print()

				frunze_noi = deepcopy(frunze)
				
				# acum trebuie sa modific frunza curenta in tuplu, sa actualizez numarul de insecte consumate
				frunze_noi[frunza_curenta.id_frunza] = Frunza(
					frunza_curenta.id_frunza,
					frunza_curenta.x,
					frunza_curenta.y,
					frunza_curenta.nr_insecte - insecte,
					frunza_curenta.g_max
				)
				nod = Nod(frunze_noi, frunza.id_frunza, greutate_noua)
				# fiecare drum are costul 1
				l_succesori.append((nod, 1))					 

				
		
		# returnam lista de succesori
		# print(f"Pentru frunza curenta {frunza_curenta} avem urmatorii succesori")
		# print(l_succesori)
		return l_succesori


			

		


	#se modifica in functie de problema
	def test_scop(self):
		frunza = self.nod_graf.frunze[self.nod_graf.id_frunza_curenta]
		greutate = self.nod_graf.greutate_curenta
		# determin daca pot sa sar de la frunza pe care se afla acuma broasca la mal
		return functia_euristica(frunza.x, frunza.y, raza) <= greutate / 3

	def __str__ (self):
		parinte=self.parinte if self.parinte is None else self.parinte.nod_graf.info
		return f"({self.nod_graf}, Parinte = {parinte}, f = {self.f}, g = {self.g})"



""" Algoritmul A* """


def str_info_noduri(l):
	"""
		o functie folosita strict in afisari - poate fi modificata in functie de problema
	"""
	sir = "["
	for x in l:
		sir += str(x) + "  "
	sir += "]"
	return sir


def afis_succesori_cost(l):
	"""
		o functie folosita strict in afisari - poate fi modificata in functie de problema
	"""
	sir = ""
	for (x, cost) in l:
		sir += "\nnod: "+str(x)+", cost arc:"+ str(cost)
	return sir


def in_lista(l, nod):
	"""
		lista "l" contine obiecte de tip NodParcurgere
		"nod" este de tip Nod
	"""
	for i in range(len(l)):
		if l[i].nod_graf.info == nod.info:
			return l[i]
	return None


def a_star():
	"""
		Functia care implementeaza algoritmul A-star
	"""
	# determinam tuplul corespunzator frunzei de plecare
	### TO DO ... DONE
	

	nod_start = Nod(frunze, frunza_start, greutate_curenta, 0)
	# print("Nod start este" + str(nod_start))
	rad_arbore = NodParcurgere(nod_start)
	# print("Radacina arbore este" + str(rad_arbore))
	# mai intai se va pune in lista open nodul de start iar lista closed va fi vida
	open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
	closed = []  # closed va contine elemente de tip NodParcurgere

	while len(open) > 0 :

		
		# print("Open=" + str_info_noduri(open))	# afisam lista open
		# print("Closed= " + str_info_noduri(closed)) # afisam lista closed
		nod_curent = open.pop(0)	# scoatem primul element din lista open
		closed.append(nod_curent)	# si il adaugam la finalul listei closed

		#testez daca nodul extras din lista open este nod scop (si daca da, ies din bucla while)
		if nod_curent.test_scop():
			break
		
		l_succesori = nod_curent.expandeaza()	# contine tupluri de tip (Nod, numar)
		
		for (nod_succesor, cost_succesor) in l_succesori:
			# "nod_curent" este tatal, "nod_succesor" este fiul curent

			# daca fiul nu e in drumul dintre radacina si tatal sau (adica nu se creeaza un circuit)
			if (not nod_curent.contine_in_drum(nod_succesor)):

				# calculez valorile g si f pentru "nod_succesor" (fiul)
				g_succesor = nod_curent.g + cost_succesor # g-ul tatalui + cost muchie(tata, fiu)
				f_succesor = g_succesor + nod_succesor.h # g-ul fiului + h-ul fiului

				#verific daca "nod_succesor" se afla in closed
				# (si il si sterg, returnand nodul sters in nod_parcg_vechi
				nod_parcg_vechi = in_lista(closed, nod_succesor)

				if nod_parcg_vechi is not None:	# "nod_succesor" e in closed
					# daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
					# 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista closed)
					# atunci actualizez parintele, g si f
					# si apoi voi adauga "nod_nou" in lista open
					
					if (f_succesor < nod_parcg_vechi.f):
						closed.remove(nod_parcg_vechi)	# scot nodul din lista closed
						nod_parcg_vechi.parinte = nod_curent # actualizez parintele
						nod_parcg_vechi.g = g_succesor	# actualizez g
						nod_parcg_vechi.f = f_succesor	# actualizez f
						nod_nou = nod_parcg_vechi	# setez "nod_nou", care va fi adaugat apoi in open

				else :
					# daca nu e in closed, verific daca "nod_succesor" se afla in open
					nod_parcg_vechi = in_lista(open, nod_succesor)

					if nod_parcg_vechi is not None:	# "nod_succesor" e in open
						# daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
						# 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista open)
						# atunci scot nodul din lista open
						# 		(pentru ca modificarea valorilor f si g imi va strica sortarea listei open)
						# actualizez parintele, g si f
						# si apoi voi adauga "nod_nou" in lista open (la noua pozitie corecta in sortare)
						if (f_succesor < nod_parcg_vechi.f):
							open.remove(nod_parcg_vechi)
							nod_parcg_vechi.parinte = nod_curent
							nod_parcg_vechi.g = g_succesor
							nod_parcg_vechi.f = f_succesor
							nod_nou = nod_parcg_vechi

					else: # cand "nod_succesor" nu e nici in closed, nici in open
						nod_nou = NodParcurgere(nod_graf=nod_succesor, parinte=nod_curent, g=g_succesor)
						# se calculeaza f automat in constructor

				if nod_nou:
					# inserare in lista sortata crescator dupa f
					# (si pentru f-uri egale descrescator dupa g)
					i=0
					while i < len(open):
						if open[i].f < nod_nou.f:
							i += 1
						else:
							while i < len(open) and open[i].f == nod_nou.f and open[i].g > nod_nou.g:
								i += 1
							break

					open.insert(i, nod_nou)


	print("\n------------------ Concluzie -----------------------")
	if len(open) == 0:
		print("Broasca nu poate ajunge la mal")
	else:
		drum = nod_curent.drum_arbore()
		for nod in drum:
			nod_graf = nod.nod_graf
			fr, ident_frunza, greutate, insecte = nod_graf.info
			print(f"Broscuta a sarit la {ident_frunza}. Greutate: {greutate}")




if __name__ == "__main__":
	a_star()
	