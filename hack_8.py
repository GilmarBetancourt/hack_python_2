"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

""""
Si la longitud es impar, se reversa el array y se agrega - y posición. 
Si la longitud es par, se devuelve un array con las posiciones en reverso.

"""

def fn_hack_8(s):
    result = s
    resultl = (len(result))
    j = 0
    result = list(reversed(result))
    if (len(result)%2!=0):
        for i in range (resultl, 0, -1):
            result[j] = result[j] + "-" + str(i)
            j += 1
    else:
        for i in range(resultl, 0, -1):
            result[j] = str(i)
            j += 1        
    return result


