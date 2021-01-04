def contarFrec(l_list):
    freq = {}
    freq_sorted = {}
    for i in l_list:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1
    # for clave, valor in freq.items():
    #     print('% s : % d'%(clave, valor))

        
    #Lista de claves cuyo valor está ordenado.
    l_sort = sorted(freq, key=freq.get, reverse=True)
    for d in l_sort:
        freq_sorted[d] = freq[d]
    print(freq_sorted) 

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)