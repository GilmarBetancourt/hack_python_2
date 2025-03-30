"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""
"""
Every third character must be replaced by a - NOT WORKING
"""

def fn_hack_5(s):
    result = s
    stringl = len(result)
    for i in range(2, stringl, 3):
        if (stringl>2):
            result = result.replace(result[i], "-",1)
    print(result)
    return result

fn_hack_5("fooziman")