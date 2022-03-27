def h_index(case_num):
    num_of_papers = int(input())
    paper_citations = list(map(int, input().split()))
    published_papers = 0
    indexing = []
    for i in range(num_of_papers):
        published_papers += 1
        if paper_citations[i] > published_papers:
            indexing.append(published_papers)
            print(indexing)
        else:
            indexing.append(indexing[-1])
            print(indexing)

num_cases = int(input())
for i in range(num_cases):
    h_index(i+1)
