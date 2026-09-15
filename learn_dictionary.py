

myCarInfo = {
    "name": "Mercedes",
    "model": "C-Class",
    "year": 2020,
    "release": "2020-02-15"
    }
print(myCarInfo)

myCarName = myCarInfo["name"]
print(myCarName)

myCarModel = myCarInfo.get("model")
print(myCarModel)



learn = {
    "description": "learn dictionary in python",
    "icon_code": "fa-fa-book",
    "id": 1,
    "name": "Learn Dictionary",
    "popularity": "high",
    "recommanded_age":"13-35"
}

learn["description"]= "Learn dictionary in python programming"

learn["icon_code"]= "dictionary-icon"
print(learn)

learn.pop("popularity")
print(learn)


print(learn)

LearnDescription = learn["description"]
print(LearnDescription)

myLearnIconCode = learn.get("icon_code")
print(myLearnIconCode)