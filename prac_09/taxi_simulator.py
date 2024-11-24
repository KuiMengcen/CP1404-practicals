from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    user_choice = input(">>> ").upper()
    user_choice = check_input(total_bill, user_choice)

    while user_choice != "Q":
        if user_choice == "C":
            current_taxi = choose_taxi()

        if user_choice == "D":
            total_bill = drive_car(current_taxi, total_bill)

        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").upper()
        user_choice = check_input(total_bill, user_choice)

    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    for i, j in zip(taxis, range(0, len(taxis))):
        print(f"{j} - {i}")