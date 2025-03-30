"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    result = s
    letters = {
        'a':'@',
        'e':'3',
        'i':'¡',
        'o':'0',
        'u':'v',
        'q':'Q'
    }


    for key in letters:
        for i in result:
            if(i==key):
                result = result.replace(i, letters[key])
    if (len(result)>2):
        firstupper = result[0].upper()
        lastupper = result[-1].upper()
        result = firstupper + result[1:-1] + lastupper

    return result

fn_hack_3("qux")
