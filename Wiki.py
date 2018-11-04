import wikipedia

nupage = wikipedia.page("Northwestern University")
#print(nupage.content)

mjpage = wikipedia.page("Michael Jackson")
#print(mjpage.content)

odpage = wikipedia.page("One Direction") #case insensitive 
#print(odpage.images)

results = wikipedia.search("Hannah Montana") #searches for the page with keywords "string"
results[0] # takes the first of those results
HannahMontanapage = wikipedia.page(results[0])
print(HannahMontanapage.categories)
