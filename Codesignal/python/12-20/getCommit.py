import re # Already imported on Codesignal
def getCommit(commit):
    return re.sub('[0+?!]', '', commit)
