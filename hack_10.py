"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    i = 1
    j = 0
    for item in result:
        new_item = {str(i):str(i+1)}
        result.insert(j, new_item)
        i += 2
        j += 1
        del result[j]
    return result
