monthConversions = {
    1 : "January", "Feb" : "Febuary", "Mar" : "March", "Apr" : "April", "Jun" : "June", "Jul" : "July", "Aug" : "August", 
    "Sep" : "September", "Oct" : "October", "Nov" : "Novermber", "Dec" : "December"
}

print(monthConversions); print(monthConversions["Dec"]); 
print(monthConversions.get("Slav")); print(monthConversions.get("Slav", "Not a Valid Key"))