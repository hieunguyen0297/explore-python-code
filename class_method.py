class User:

	active_user = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_user} active users"
	
	def __init__(self, first, last, age):
		# print("A new user has been made!")
		self.first = first
		self.last = last
		self.age =age
		# every time, a new user is created it, it will add to User class
		User.active_user += 1


	def logout(self):
		User.active_user -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initial(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def seniors(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

user1 = User('Joe', 'Smith', 68)
user2 = User('JOwe', 'Nguyen', 55)
user1.logout()
print(User.display_active_users())
