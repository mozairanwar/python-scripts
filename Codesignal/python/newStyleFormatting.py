import re # Already imported on Codesignal
def newStyleFormatting(s):
    return re.sub('%[a-z]', '{}', s.replace('%%','{%}')).replace('{%}','%')
