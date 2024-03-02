def data(**kwargs):
    return kwargs

res = data(name="Force", age=18, password=None, email="force@gmail.com")
print(res.keys())
print(res.values())

