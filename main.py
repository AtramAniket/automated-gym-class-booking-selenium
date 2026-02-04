from datetime import datetime as dt
from datetime import timedelta
from session import Session
gym_class = None
booking_date = None
class_timing = None

def display_options():

	global gym_class, booking_date, class_timing

	print("*********AUTOMATED GYM CLASS BOOKING*********")

	

	name_of_gym_class = input("Which class do you want to book(Yoga, Spin, HIIT): ")

	if(name_of_gym_class.upper() in "YOGA, SPIN, HIIT".split(", ")):
		
		gym_class = name_of_gym_class
	
	else:
		
		print(f"Unknown input {name_of_gym_class}. EXPECTED:: Yoga, Spin, HIIT")
		
		display_options()




	print("Enter the time for which you want to book the class\n")

	gym_class_timing = input("Available timings are 7:00 AM, 8:00 AM, 9:00 AM, 5:00 PM, 6:00 PM, 7:00 PM: ")

	if(gym_class_timing in "7:00 AM, 8:00 AM, 9:00 AM, 5:00 PM, 6:00 PM, 7:00 PM".split(", ")):

		timing = dt.strptime(gym_class_timing, "%I:%M %p")
		class_timing = timing
	
	else:
		print(f"Time error {gym_class_timing}. No bookings allowed at this time.")
		
		display_options()



	booking_date = input("Which date you want to book the class? available options::Today, Tomorrow, Custom: ")

	if(booking_date.lower() == "tomorrow"):

		booking_date = dt.now().date() + timedelta(days = 1)
	
	elif(booking_date.lower() == "today"):
	
		booking_date = dt.now().date()
	
	elif(booking_date.lower() == "custom"):
	
		custom_date = input("Enter date in YY-MM-DD format: ")
		booking_date = dt.strptime(custom_date, "%Y-%m-%d")
	else:
		print(f"Unknown option: {booking_date}. EXPECTED:: Today, Tomorrow, Custom")

	confirm = input(f"You would like to book {name_of_gym_class} at {gym_class_timing} on {booking_date}? (Y/N): ")

	if confirm.lower() == "y":
		print("Booking Class")
	else:
		display_options()



display_options()

session = Session()

# login
session.login_to_gym_site()

# check and book class
session.book_gym_class(class_to_book = gym_class, class_booking_date = booking_date, class_booking_time = class_timing)