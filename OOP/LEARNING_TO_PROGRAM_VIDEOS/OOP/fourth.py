#!/usr/bin/python3
# import the datetime module since we will be
# using it to calculate the age
# first import the date class from datetime module
# then use the today function from the date class to get the current date.
import datetime


class USER:
    """A member of Friends.For now, I am simply storing their
    full name and their birthday."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        # let us extract first and last names
        # and store them in an array.
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """This method returns the age of the user in years."""
        today = datetime.date.today()
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[-2:])
        dob = datetime.date(yyyy, mm, dd)
        print(dob)
        age_of_user_in_days = (today - dob).days
        age_in_years = (age_of_user_in_days) / 365
        return int(age_in_years)


makena = USER("Makena Wambui", "19920903")
print(makena.name, makena.birthday)
print(makena.first_name)
# print(last_name will give attribute error because the variable last_name does not exist outside of the init method)
print(makena.last_name)
# what happens when you call the help function on this class?
# help(USER)
print(makena.age())
jake = USER("Jake Tendai", '20170217')
print(jake.age())
