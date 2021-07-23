def isTestSolvable(ids, k):
    digitSum = lambda ids: sum(int(n) for n in str(ids))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
