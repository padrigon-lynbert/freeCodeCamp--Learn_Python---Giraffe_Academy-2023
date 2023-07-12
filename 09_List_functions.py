lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]; print(friends)
friends.extend(lucky_numbers); print(friends)
friends.append("Creed"); print(friends) #append to the end of the list
friends.insert(0, "Kelly"); print(friends)
friends.remove("Creed"); print(friends)
friends.pop(); print(friends) #pop removes the last element on the list
print(friends.index("Jim"))

friends.insert(0, "Kelly"); print(friends.count("Kelly"))

friends.clear(); print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]; friends.sort(); print(friends)
 
lucky_numbers.reverse(); print(lucky_numbers)

friends2 = friends.copy(); friends2.append("nowaynoway"); print(friends2)