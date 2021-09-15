dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk","Baahubali",
                "Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user_1 = {"Ironman","KGF","Dhamaal","Aquaman","Thor","It","Kahani"}
user_2 = {"Ironman","KGF","Gravity","Avengers","Thor","Master","Hulk"}

common = user_1.intersection(user_2)
scores = {}

for item in dataset:
    movies = dataset[item]
    numer = common.intersection(set(movies))
    denom = common.union(set(movies))
    score = len(numer) / len(denom)
    scores[item] = round(score,2)

print(scores)

max_value = max(scores.values())

for key in scores:
    if scores[key] == max_value:
        category = key
        break
print("Category is :",category)

recommended = set(dataset[category]).intersection(user_1) - user_2
print("Recommended for User_2 ::",recommended)

