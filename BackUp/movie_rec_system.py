dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk","Baahubali",
                "Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user = {"Ironman","KGF","Dhamaal","Aquaman","Thor","It","Kahani"}

scores = {}

for item in dataset:
    movies = dataset[item]
    numer = user.intersection(set(movies))
    denom = user.union(set(movies))
    score = len(numer) / len(denom)
    scores[item] = round(score,2)

print(scores)
