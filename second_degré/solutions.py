
def entree_valeurs() -> tuple[int]:
	"""
	Fonction qui demande les valeurs de a, b et c dans le trinôme ax² + bx + c
	et renvoie un tuple correspondant aux trois valeurs
	"""
	a = eval(input("Entrez la valeur de a dans ax²: "))
	b = eval(input("Entrez la valeur de b dans bx: "))
	c = eval(input("Entrez la valeur de c: "))
	return a,b,c

def expression_trinome(a: int,b: int,c: int) -> str:
	"""
	Fonction qui prend en paramètre les valeurs de a, b et c puis retourne
	l'expression de l'équation
	"""
	equation = ""
	if a != 0:
		equation += str(a)+"x²"
	if b != 0:
		if b < 0:
			equation += " - " + str(abs(b))+"x"
		else:
			equation += (" + " if a != 0 else "") + str(b)+"x"
	if c != 0:
		if c < 0:
			equation+= " - "+str(abs(c))
		else:
			equation += " + "+str(c)

	return equation+" = 0"

def calcule_delta(a,b,c) -> int:
	"""
	Fonction qui calcule  et retourne la valeur du discriminant Δ
	(delta) définit par Δ = b² - 4ac à partir de la valeur des termes a, b et c du trinôme.
	"""
	return pow(b,2) - 4 * a * c

def cherche_solutions(a,b,c):
	"""
	Fonction qui cherche la ou les solutions à une équation du second degré s'il en existe et la/les retourne.
	"""
	delta = calcule_delta(a,b,c)
	if delta < 0:
		print(f"L'équation {expression_trinome(a,b,c)} n'a pas de solution réelle.")
		print("Elle n'a donc pas de forme factorisée")

	elif delta == 0:
		x0 = -b/2*a
		print(f"L'équation {expression_trinome(a,b,c)} a une unique solution:\nx0 = {x0}\n")
		signe = '-' if x0 < 0 else '+'
		print(f"Sa forme factorisée est : (x {signe} {abs(x0)})²")
	
	elif delta > 0:
		x1 = (-b-pow(delta,0.5))/(2*a)
		x2 = (-b+pow(delta,0.5))/(2*a)
		print(f"L'équation {expression_trinome(a,b,c)} a deux solutions distinctes:\nx1 = {x1}\tx2 = {x2}\n")
		signe1 = '-' if -x1 < 0 else '+'
		signe2 = '-' if -x2 < 0 else '+'
		print(f"Sa forme factorisée est : (x {signe1} {abs(x1)})(x {signe2} {abs(x2)})\n")


if __name__ == '__main__':
	a,b,c = entree_valeurs()
	print("\n",expression_trinome(a,b,c),'\n')
	print("delta = ", calcule_delta(a,b,c),"\n")
	cherche_solutions(a,b,c)