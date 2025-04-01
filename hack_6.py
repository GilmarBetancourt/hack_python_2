"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    if(len(result)==0):
        result = ["0"]
    else:
        for i in range(len(result)):
            if((i%2!=0)and(i!=0)):
                result[i] = "-"
            else:
                result[i] = str(i+1)
    
    return result

