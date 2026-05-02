#papers is a list of tuples that contains information about the number of papers published by a researcher during his career 
#each element is a form of the form (year,num): the researcher has published (num) papers in the (year) year.
# Write a function named good_years that accepts (papers) as arguments and returns the list of year in which the researcher has published the maximum number of papers.
# You do not have to accept input from the user or print output to the console. you just have to write the function definition.
# The order of years in the returned list doesn't matter.

# def good_years (paper1):

def good_years(papers):
    if not papers:
        return [] 
    if papers:
        getnum=(num for year, num in papers)
        getmaxnum = max(getnum)
        getmaxyear = [year for year ,num in papers if num == getmaxnum]
        return getmaxyear

paper1 = [(2000,5),(2001,7),(2002,3),(2003,7)]
print(good_years(paper1))





