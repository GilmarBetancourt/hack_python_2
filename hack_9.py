"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    for key in list(result.keys()):
        if(key=="foo"):
            result[key] = "Fooziman"
            result["Foo"] = result.pop(key)
        else:
            result.pop(key)
    print(result)
    return result


fn_hack_9({"foo":"fookziman","bar":"barziman"})