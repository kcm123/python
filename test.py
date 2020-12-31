def add_10(value):
    if value < 40:
        return 10
    else:
        result = value + 10
        return result
print(add_10(32))
print("test")
print("{} {} 테스트".format('2', '4'))
print()
test = [{'id':'cat'}, {'id':'dog'},{'id':'bird'} ]
for t in test:
    print(t.get('id'))
