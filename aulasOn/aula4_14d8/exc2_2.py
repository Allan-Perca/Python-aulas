def pg(numero, q):
    if numero <= 1:
        print(1)
        return 1
    else:
        r = q + pg(numero - 1, q)
        print(r)
        return r
		
