import cProfile

def my_dict(name,age,my_place):
    d= {"Name": "name",
    "Age" : "age",
    "place": "my_place"
    }
    return d

cProfile.run('my_dict("Nipun","32","Muzaffarnagar")')











