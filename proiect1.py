# Andronic Alexandra - Grupa 231 - Pr_7 - Evadarea lui Mormocel

from collections import namedtuple 
import math
from copy import deepcopy
import time


frunze = {}
Frunza = namedtuple("Frunza", ("id_frunza", "x", "y", "nr_insecte", "g_max"))
insecte_final = 0

def functia_euristica(x, y, raza):
	# functia euristica este data de cat mai are de parcurs broasca de la pozitia curenta(x, y) pana la mal
	# distanta se calculeaza raportandu-ne la centrul cercului(0, 0)
	return raza - dist_puncte(x, y, 0, 0)

# functie care calculeaza distanta dintre doua puncte pentru a sti daca broasca poate sa sara de la o frunza la alta fara sa moara
def dist_puncte(x1, y1, x2, y2):
	return float(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))



class Nod:
	def __init__(self, frunze, id_frunza_curenta, greutate_curenta, insecte_consumate):
		self.frunze = frunze # tuplu cu toate frunzele
		self.id_frunza_curenta = id_frunza_curenta # frunza initala pe care se afla broscuta
		self.greutate_curenta = greutate_curenta
		# la fiecare pas(saritura pe alta frunza) trebuie sa avem toate frunzele disponibile, frunza pe care ne aflam in acel moment si greutatea curenta a broscutei
		self.info = (frunze, id_frunza_curenta, greutate_curenta, insecte_consumate)
		frunza_curenta = self.frunze[self.id_frunza_curenta]
		self.h = functia_euristica(frunza_curenta.x, frunza_curenta.y, raza)
		self.insecte_consumate = insecte_consumate
		
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
		"""
		nod_c = self
		while nod_c.parinte is not None :
			if nod.info == nod_c.nod_graf.info:
				return True
			nod_c = nod_c.parinte
		return False


	
	def expandeaza(self):
		
		# pentru nodul curent trebuie sa gasim toate nodurile in care putem "merge" respectand anumite proprietati
		
		# lista in care retin succesorii
		l_succesori = []
		
		# extrag informatia utila din nod
		frunze, id_frunza_curenta, greutate_curenta, insecte_consumate = self.nod_graf.info

		# trebuie sa aflu frunza pe care sunt(Tuplul corespunzator ei)
		frunza_curenta = frunze[id_frunza_curenta]

		
		for frunza in frunze.values():
			# pentru fiecare "frunza" din lista, dar care sa nu fie frunza curenta
			if frunza.id_frunza != frunza_curenta.id_frunza:
				# pentru fiecare insecta mancata in plus trebuie sa luam toate variantele(1 -> numarul total de insecte de pe frunza) si sa "contruim" un succesor separat pentru fiecare

				for insecte in range(0, frunza_curenta.nr_insecte + 1):
					# greutatea noua a broastei se calculeaza insumand greutatea sa curenta cu numarul de insecte consumate de pe frunza
					greutate_noua = greutate_curenta + insecte
					
					if dist_puncte(frunza_curenta.x, frunza_curenta.y, frunza.x, frunza.y) <= greutate_noua / 3:
					
						
						# daca greutatea curenta depaseste greutatea maxima suportata de frunza pe care doresc sa sar, atunci saltul nu poate fi facut
						if greutate_noua - 1 < frunza.g_max:
							# se scade 1 la fiecare salt
							greutate_noua -= 1
							if greutate_noua:
								# daca broscuta a ajuns la greutate 0 in urma saltului aceasta moare
								# fac o copie a listei de frunze
								frunze_noi = deepcopy(frunze)
								
								# acum trebuie sa modific frunza curenta in tuplu, sa actualizez numarul de insecte consumate
								frunze_noi[frunze[id_frunza_curenta]] = Frunza(frunza_curenta.id_frunza, frunza_curenta.x, frunza_curenta.y, frunza_curenta.nr_insecte - insecte, frunza_curenta.g_max)
								nod = Nod(frunze_noi, frunza.id_frunza, greutate_noua, insecte)
								# fiecare drum are costul 1
								l_succesori.append((nod, 1))					 

		
		return l_succesori


			

		


	
	def test_scop(self):
		frunza_curenta = self.nod_graf.frunze[self.nod_graf.id_frunza_curenta]
		greutate = self.nod_graf.greutate_curenta
		# determin daca pot sa sar de la frunza pe care se afla acuma broasca la mal
		return (raza - dist_puncte(frunza_curenta.x, frunza_curenta.y, 0 ,0)) <= greutate / 3
		

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


def a_star(stare_initiala_finala):
	"""
		Functia care implementeaza algoritmul A-star
	"""
	
	
	# determinam nodul corespunzator frunzei de plecare
	# initial a mancat 0 insecte(de pe frunza de start)
	nod_start = Nod(frunze, frunza_start, greutate_curenta, 0)
	rad_arbore = NodParcurgere(nod_start)
	open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
	closed = []  # closed va contine elemente de tip NodParcurgere

	while len(open) > 0 :
		
		nod_curent = open.pop(0)	# scoatem primul element din lista open
		closed.append(nod_curent)	# si il adaugam la finalul listei closed
		
		#testez daca nodul extras din lista open este nod scop (si daca da, ies din bucla while)
		if nod_curent.test_scop():
			# daca atunci cand verificam scopul lista open nu mai contine niciun element
			# inseamna ca primul nod(frunza de plecare) este si nodul scop, deci dupa acea frunza poate sa sara direct la mal
			if len(open) == 0:
				# adica starea initiala este si finala(adica broscuta poate sari direct de pe frunza pe care se afla la mal, insa trebuie sa indepleineasca toate conditiile)
				f.write("Starea initiala este si finala.\n")
				f.write(f"Broscuta a sarit de la frunza {frunza_start}({int(frunze[frunza_start].x)}, {int(frunze[frunza_start].y)}) direct la mal.")
				
				stare_initiala_finala = True
			# trebuie sa vad cate insecte mai poate consuma de la ultima frunza pana la mal
			# o sa ii dau varianta sa manance cat de multe insecte poate de pe ultima frunza din drum asta pana nu mai este indeplinita conditita
			greutate = nod_curent.nod_graf.greutate_curenta
			insecte_frunza = nod_curent.nod_graf.frunze[nod_curent.nod_graf.id_frunza_curenta].nr_insecte
			poz_x = nod_curent.nod_graf.frunze[nod_curent.nod_graf.id_frunza_curenta].x
			poz_y = nod_curent.nod_graf.frunze[nod_curent.nod_graf.id_frunza_curenta].y
			
			for insecte in range(0, insecte_frunza + 1):
				greutate_noua = greutate + insecte
				if raza - dist_puncte(poz_x, poz_y, 0, 0) <= greutate_noua / 3:
					insecte_final = insecte
				else:
					break
				
			break
		
		l_succesori = nod_curent.expandeaza()	
		
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
						nod_nou = NodParcurgere(nod_graf = nod_succesor, parinte = nod_curent, g = g_succesor)
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

	
	
	
	
	t_dupa = int(round(time.time() * 1000))
	# afisez cat a durat gasirea drumului pentru fiecare fisier
	f.write("Gasirea drumului a durat " + str(t_dupa-t_inainte) + " milisecunde.\n")
	if len(open) == 0 and stare_initiala_finala == False:
		f.write("Broscuta nu a putut sa ajunga la mal\n")
	elif stare_initiala_finala == False:
		drum = nod_curent.drum_arbore()
		
		id_linie = 1
		for i in range(len(drum) - 1):
			# frunze, id_plecare, greutate_broasca, insecte_consumate = drum.nod_graf.info
			frunza_curenta = drum[i].nod_graf.frunze[drum[i].nod_graf.id_frunza_curenta]
			frunza_tinta = drum[i+1].nod_graf.frunze[drum[i+1].nod_graf.id_frunza_curenta]
			# afisam configuratie pentru frunza initiala cu greutatea broastei de plecare, luata din fisierul de intrare
			if drum[i].parinte == None:
				f.write(f"{id_linie}) Broscuta se afla pe frunza initiala {frunza_curenta.id_frunza}({int(frunza_curenta.x), int(frunza_curenta.y)}). Greutate broscuta este {int(greutate_curenta)}.\n")
				id_linie += 1
			
			if i + 2 < len(drum):
				f.write(f"{id_linie}) Broscuta a sarit de la {frunza_curenta.id_frunza}({int(frunza_curenta.x)}, {int(frunza_curenta.y)}) la {frunza_tinta.id_frunza}({int(frunza_tinta.x)}, {int(frunza_tinta.y)}). Broscuta a mancat {drum[i+2].nod_graf.insecte_consumate} insecte si acum are greutate {int(drum[i+2].nod_graf.insecte_consumate + drum[i+1].nod_graf.greutate_curenta)}\n")
			else:
				f.write(f"{id_linie}) Broscuta a sarit de la {frunza_curenta.id_frunza}({int(frunza_curenta.x)}, {int(frunza_curenta.y)}) la {frunza_tinta.id_frunza}({int(frunza_tinta.x)}, {int(frunza_tinta.y)}). De pe ultima frunza broscuta a mancat {insecte_final} insecte si acum are greutatea {int(drum[i+1].nod_graf.greutate_curenta)}\n")
				
			
			id_linie += 1
		
		f.write(f"{id_linie}) Broscuta a ajuns la mal din {len(drum)} sarituri\n")




if __name__ == "__main__":

	lista_fisiere = ["input_1.in", "input_2.in", "input_3.in", "input_4.in"]
	# primul fisier -> 
	nr_fisier = 1
	for fisier in lista_fisiere:
		stare_initiala_finala = False
		with open(fisier, "r") as fin:
			raza = float(next(fin))
			greutate_curenta = float(next(fin))
			frunza_start = next(fin).strip()
			for linie in fin:
				id_frunza, x, y, nr_insecte, g_max = linie.split()
				frunze[id_frunza] = Frunza(id_frunza, float(x), float(y), int(nr_insecte), float(g_max))
		t_inainte = int(round(time.time() * 1000))
		fisier_output = "output_" + str(nr_fisier) + ".out"
		f = open(fisier_output, 'w')
		nr_fisier += 1
		a_star(stare_initiala_finala)
	
