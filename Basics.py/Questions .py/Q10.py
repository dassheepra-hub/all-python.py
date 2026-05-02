def good_years (papers):
    max= 0
    for i in papers :
        if i[1]> max:
            max = i[1]
    years = []
    for i in papers:
        if i[1] == max :
            years.append (i[0])
        return years 
a =good_years[(2002,3),(2005,8),(2008,9),(2009,6)]
print(a)

