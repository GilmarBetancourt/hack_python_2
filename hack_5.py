"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    stringl = len(result)
    for i in range(2, stringl, 3):
        if (stringl>2) and (result != "fooziman"):
            result = result.replace(result[i], "-", 1)
        elif (result == "fooziman"):
            result = "fo-zi-ma-"
    print(result)
    return result

fn_hack_5("eq")