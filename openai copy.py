import requests

# Define the API endpoint
url = "https://www.dex.inside.philips.com/philips-ai-chat/chat/api/user/SendImageMessage"

# Define the headers with the cookie
headers = {
    'Cookie': '.AspNetCore.Cookies=CfDJ8KMy4_c-Wz5PjYx8z8V0OI6X9mfAfNIFv7JM3m4npf4GWwi8UZSa45_fwViSYioAAnP1DZ_LPgUmgujAsrTUxKUEkmPPeIzCXOQxAdda5uw0BsTjNcU_NpLUbPoaKGnob3oC3His37hjzv8gqGdzIu0xhxaXSTzGsM6ZMut6KsU3A2R8v6XnzlrIoc6gh0Qpjv_y1WR41PloTDlDMPp5Qy5IOWD7eA1YTCpCqb_6s0poFtbADoGSH8WMvEMtE85UTQfiKJfB8JkJU0UOGBG_Rrd0BJbdPOpiOL8TYrgp7jOodTOrws_yB1kr4JIPbakMuCjnrvvIxahFJ0mqCEIsArytAO1wj15ObnVDdepS7xUylLojEcRkDOkxk-xASWwzVwnIH3quxt3yqcBHWAK8VbRs_5jpHhZKP-akrrZIHLiWtEovUrSuY15GGfRJBMZUYqqEyHCON9JyAG2zg1s5AFNrXQhyfgWXMk5K4P7LGE3pNMqdpj5hX5_Yy_JiU0tj2KFvZxdc9Zpykca6vAfD9UZma5f7ROErVozy7U2AV-Ub4F97smDe6RvdlCxtwY4GZ7nHtjS-K8D3ILz6PL5g22WXN5BGo9Pz4DpG5dOrQ93YcHJ14hoJn-TEaHCKDpWvevZxWmBTJlGO5d4aCYEdo5dq_ehetUNdFy56RY8wfuZU-O7estmhnS-BJH9u5IAce3t4Z40aCxKrf7wVLh9x6-VqeK5IOXVzYKg0HaQdgwyzgPekipX4xRckR-dCWGaBiLIemjGRdArnoo8UfDZOWr7WCnlQVL4HGdZ_ZN3dc0qUXm8M4c1POFlnbvpvTVB_YNgbFNMfzg9eKwlmbk1AOq9QdzuqxaBxkDZ5xP9n6Selg3l_g1AinbWuefFemkcr2RktMliowTczMeiPqx1DFr0bIu_qSO9Ap7AlnQIOu60CdauIyG777FJ6O0sQaJ2_ZeaTfzwY9pnjFbJ9s6dsxTkwPcLA4x3_2j6bQ4sFCuQkOLwM92KpvrqM_lhojLgBPfbzEUKoliNGdhj4Y5ThH9o3rq5QBwfeLkFNOithALu_EKzX2ICtSH8C6lVNh3vaQ6wQvkael0T4GpzUeskjCF7D515qh6qhfldh_eCpwLvz4nwMU-LKpU499N0lLpsJ6nEkHJUiD_Z1eKEh4G3aGiSL4A3TrEiTIJGu1wNzAPxE-FqOuPjORBgDTfkEUY9Tb1tcgirvWj5LZhjK1ZXXqb2DIb0-A_EknjwaS3cKZQOu2YAhYdNy09Y5aGQ3Jq0CYQnbuxteyyi5oh8ImRV3y2cZmJ5CJSBd6VING2YoxIqygqc0q058bosvY7REllcT__EpkqHLvqSsG-CjmWf29Y0bngGzteetlRporvYGBLP5lw2HZD83IRJdHdfxZTj1GUSpBoX1QflyEX4EiS6szHAZY-rJsXnp3POiObYGmPAsM41QDWHJcAOY9Pos8Kt9Li30tzNc875XpDx6QBEoiobP4nBb2NknoKDk8vHHjpUXI1VYkDKeBNMKfJ287oNPEAYffgHy44Qj3c-RSWxzM5PgE06zmYM2s-F-SIEwUnr9hQSRHsgx3XeiAL0MODuFkAggFOazKbfb6n9WURMWTZ5RTX8b2mLpMD1EJt8R7Vdjik9MEId2X1blyEBG8Af9-RSQj09fe8M_46_rb43KIKR0wf4ySrQxn9rFjMCjON9cQQwRa2xg2iiRiSbTeM8JJ-FEFivCtfoIyrXMbmwDTJQYgn8APcSIHkPYQmR3xyslT-U_bxmZzgvrpU96Gy7m7qYcjA57LnC7RxgMZleIIa8x7PhXB0dMvYIxlpTZygkSAq6XxmJ665fZ7bhe3tvvx669VP2Jqo0reN1kZo3AHuETQUpKmINpKAKCym99o5o1HDcVEiFeA5MqN1UDSo-5LO3ZkGFK7rkiwYy1HlLBj9QICT0-zhZh5bZa6WMGZ0FaCHfB68bTPuQjWG_vsQQRlxz5wkH1eTFQvzZmDidIe7vbXRtMA_MApLqkab9yDGQA8G-a__O_JozKgSNQO56JccuMX0j7agbtFk5ZQnBWja9bLOsJ1d8z4rQk0EtFI1wOWecF-jFD8fxsRWuFElIodi6GVQEU24isErJP25tNO4XwrcD3HeEr7t4PstEf2PQytKS8MYhll1BV3kdgZ6pZleAL-PY5EnNWn_7_FXZo-nhVA9Oq2K_0zBdLeVtP-nCtvatbPzDkwDf1I9OnU8gQ8wr1E3gaEfPoN2tsM87rXTXVJv3Wsnp7jrwfSzNM-Tj1zJ8DzU9ogfZvl_3oPaRu2WGLDnsj6f6EgmXdAnRnshWpvR6sSJR4hJ0_Hi0E_S6AWd1kpy8Wd2ODkAQ-I_LqLyIGPI_IFb2y0dLgPpvhZFwNbSPcPzMQg8Sdl4ANUon2Z2_cYtoB8fQ43SQl4HPdRncZpjomDaMndt44VVliKPD0tcf7Y5Z5eWSx9PQk0uxZBV-XFn5VO1AZIQZ5cweRrgNf2LtM2dn4ZViKbjokkubbMM4tHGVOVsb7z0eEEug01QgXvbuzRfWwv_jdpWxGtRbOMW6pig61wuIBKVq7ivRma9nPsl-gJnMK1SGQQxjJZsqvASgm_PGZHumkS6o5lTie3SMNQ-JsF8ppa3t5F6OHk__EbjQklsqhbPLNSJFgwK5XOeQr3kYMcp1ilws8YsfOE4twxzxYNT91R1SDrtnAKIoWvRCuMYQri22ApsKdcDRPaxs4vmrd77YfEKrUKyXuaxswxcuadhRnZrK6BAQ; ai_user=V5697lqIHSnfr+8ozVDooj|2024-07-23T07:32:44.735Z; ARRAffinitySameSite=8da8ccc8fe610cb85ae6bee641a7cdab56856c5b0031afc971de42132583be1e; ai_session=8ovnE+MUKwSVCL20sII5OV|1722580808141|1722580810784; ARRAffinity=8da8ccc8fe610cb85ae6bee641a7cdab56856c5b0031afc971de42132583be1e',
    'Content-Type': 'application/json'
}

# Define the payload
payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is ML?"
                }
            ]
        }
    ]
}

# Make the POST request
#response = requests.post(url, json=payload, headers=headers)
response = requests.pot(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())


response = requests.pot(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())

##########################$$$$$$$$$$$$$$$$$$$$$$$$$$

import requests

# Define the API endpoint
url = "https://www.dex.inside.philips.com/philips-ai-chat/chat/api/user/SendImageMessage"

# Define the headers with the cookie
headers = {
    'Cookie': '.AspNetCore.Cookies=CfDJ8KMy4_c-Wz5PjYx8z8V0OI6X9mfAfNIFv7JM3m4npf4GWwi8UZSa45_fwViSYioAAnP1DZ_LPgUmgujAsrTUxKUEkmPPeIzCXOQxAdda5uw0BsTjNcU_NpLUbPoaKGnob3oC3His37hjzv8gqGdzIu0xhxaXSTzGsM6ZMut6KsU3A2R8v6XnzlrIoc6gh0Qpjv_y1WR41PloTDlDMPp5Qy5IOWD7eA1YTCpCqb_6s0poFtbADoGSH8WMvEMtE85UTQfiKJfB8JkJU0UOGBG_Rrd0BJbdPOpiOL8TYrgp7jOodTOrws_yB1kr4JIPbakMuCjnrvvIxahFJ0mqCEIsArytAO1wj15ObnVDdepS7xUylLojEcRkDOkxk-xASWwzVwnIH3quxt3yqcBHWAK8VbRs_5jpHhZKP-akrrZIHLiWtEovUrSuY15GGfRJBMZUYqqEyHCON9JyAG2zg1s5AFNrXQhyfgWXMk5K4P7LGE3pNMqdpj5hX5_Yy_JiU0tj2KFvZxdc9Zpykca6vAfD9UZma5f7ROErVozy7U2AV-Ub4F97smDe6RvdlCxtwY4GZ7nHtjS-K8D3ILz6PL5g22WXN5BGo9Pz4DpG5dOrQ93YcHJ14hoJn-TEaHCKDpWvevZxWmBTJlGO5d4aCYEdo5dq_ehetUNdFy56RY8wfuZU-O7estmhnS-BJH9u5IAce3t4Z40aCxKrf7wVLh9x6-VqeK5IOXVzYKg0HaQdgwyzgPekipX4xRckR-dCWGaBiLIemjGRdArnoo8UfDZOWr7WCnlQVL4HGdZ_ZN3dc0qUXm8M4c1POFlnbvpvTVB_YNgbFNMfzg9eKwlmbk1AOq9QdzuqxaBxkDZ5xP9n6Selg3l_g1AinbWuefFemkcr2RktMliowTczMeiPqx1DFr0bIu_qSO9Ap7AlnQIOu60CdauIyG777FJ6O0sQaJ2_ZeaTfzwY9pnjFbJ9s6dsxTkwPcLA4x3_2j6bQ4sFCuQkOLwM92KpvrqM_lhojLgBPfbzEUKoliNGdhj4Y5ThH9o3rq5QBwfeLkFNOithALu_EKzX2ICtSH8C6lVNh3vaQ6wQvkael0T4GpzUeskjCF7D515qh6qhfldh_eCpwLvz4nwMU-LKpU499N0lLpsJ6nEkHJUiD_Z1eKEh4G3aGiSL4A3TrEiTIJGu1wNzAPxE-FqOuPjORBgDTfkEUY9Tb1tcgirvWj5LZhjK1ZXXqb2DIb0-A_EknjwaS3cKZQOu2YAhYdNy09Y5aGQ3Jq0CYQnbuxteyyi5oh8ImRV3y2cZmJ5CJSBd6VING2YoxIqygqc0q058bosvY7REllcT__EpkqHLvqSsG-CjmWf29Y0bngGzteetlRporvYGBLP5lw2HZD83IRJdHdfxZTj1GUSpBoX1QflyEX4EiS6szHAZY-rJsXnp3POiObYGmPAsM41QDWHJcAOY9Pos8Kt9Li30tzNc875XpDx6QBEoiobP4nBb2NknoKDk8vHHjpUXI1VYkDKeBNMKfJ287oNPEAYffgHy44Qj3c-RSWxzM5PgE06zmYM2s-F-SIEwUnr9hQSRHsgx3XeiAL0MODuFkAggFOazKbfb6n9WURMWTZ5RTX8b2mLpMD1EJt8R7Vdjik9MEId2X1blyEBG8Af9-RSQj09fe8M_46_rb43KIKR0wf4ySrQxn9rFjMCjON9cQQwRa2xg2iiRiSbTeM8JJ-FEFivCtfoIyrXMbmwDTJQYgn8APcSIHkPYQmR3xyslT-U_bxmZzgvrpU96Gy7m7qYcjA57LnC7RxgMZleIIa8x7PhXB0dMvYIxlpTZygkSAq6XxmJ665fZ7bhe3tvvx669VP2Jqo0reN1kZo3AHuETQUpKmINpKAKCym99o5o1HDcVEiFeA5MqN1UDSo-5LO3ZkGFK7rkiwYy1HlLBj9QICT0-zhZh5bZa6WMGZ0FaCHfB68bTPuQjWG_vsQQRlxz5wkH1eTFQvzZmDidIe7vbXRtMA_MApLqkab9yDGQA8G-a__O_JozKgSNQO56JccuMX0j7agbtFk5ZQnBWja9bLOsJ1d8z4rQk0EtFI1wOWecF-jFD8fxsRWuFElIodi6GVQEU24isErJP25tNO4XwrcD3HeEr7t4PstEf2PQytKS8MYhll1BV3kdgZ6pZleAL-PY5EnNWn_7_FXZo-nhVA9Oq2K_0zBdLeVtP-nCtvatbPzDkwDf1I9OnU8gQ8wr1E3gaEfPoN2tsM87rXTXVJv3Wsnp7jrwfSzNM-Tj1zJ8DzU9ogfZvl_3oPaRu2WGLDnsj6f6EgmXdAnRnshWpvR6sSJR4hJ0_Hi0E_S6AWd1kpy8Wd2ODkAQ-I_LqLyIGPI_IFb2y0dLgPpvhZFwNbSPcPzMQg8Sdl4ANUon2Z2_cYtoB8fQ43SQl4HPdRncZpjomDaMndt44VVliKPD0tcf7Y5Z5eWSx9PQk0uxZBV-XFn5VO1AZIQZ5cweRrgNf2LtM2dn4ZViKbjokkubbMM4tHGVOVsb7z0eEEug01QgXvbuzRfWwv_jdpWxGtRbOMW6pig61wuIBKVq7ivRma9nPsl-gJnMK1SGQQxjJZsqvASgm_PGZHumkS6o5lTie3SMNQ-JsF8ppa3t5F6OHk__EbjQklsqhbPLNSJFgwK5XOeQr3kYMcp1ilws8YsfOE4twxzxYNT91R1SDrtnAKIoWvRCuMYQri22ApsKdcDRPaxs4vmrd77YfEKrUKyXuaxswxcuadhRnZrK6BAQ; ai_user=V5697lqIHSnfr+8ozVDooj|2024-07-23T07:32:44.735Z; ARRAffinitySameSite=8da8ccc8fe610cb85ae6bee641a7cdab56856c5b0031afc971de42132583be1e; ai_session=8ovnE+MUKwSVCL20sII5OV|1722580808141|1722580810784; ARRAffinity=8da8ccc8fe610cb85ae6bee641a7cdab56856c5b0031afc971de42132583be1e',
    'Content-Type': 'application/json'
}

# Define the payload
payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is ML?"
                }
            ]
        }
    ]
}

# Make the POST request
#response = requests.post(url, json=payload, headers=headers)
response = requests.pot(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())


response = requests.pot(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())



def add(x, y):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first and returns the result.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second and returns the result.
    
    Parameters:
    x (float): The numerator.
    y (float): The denominator.
    
    Returns:
    float or str: The quotient if y is not zero; otherwise, an error message.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def validate_input(input_str):
    """
    Validates user input to ensure it is a numeric value.
    
    Parameters:
    input_str (str): The user input to validate.
    
    Returns:
    float: The validated numeric value, or raises a ValueError if invalid.
    """
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")


def validate_input(input_str):
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")
    
def validate_input(input_str):
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")
def validate_input(input_str):
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")

def validate_input(input_str):
    """
    Validates user input to ensure it is a numeric value.
    
    Parameters:
    input_str (str): The user input to validate.
    
    Returns:
    float: The validated numeric value, or raises a ValueError if invalid.
    """
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")

def calculator():
    """
    Runs the calculator program, allowing users to perform basic arithmetic operations.
    
    The user selects an operation (add, subtract, multiply, divide) and inputs two numbers.
    The function then performs the selected operation and displays the result.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in {'1', '2', '3', '4'}:
        print("Invalid input! Please choose a number between 1 and 4.")
        return

    try:
        num1 = validate_input(input("Enter first number: ").strip())
        num2 = validate_input(input("Enter second number: ").strip())
    except ValueError as e:
        print(e)
        return

    if choice == '1':
        result = add(num1, num2)
        operation = " + "
    elif choice == '2':
        result = subtract(num1, num2)
        operation = " - "
    elif choice == '3':
        result = multiply(num1, num2)
        operation = " * "
    elif choice == '4':
        result = divide(num1, num2)
        operation = " / "

    print(f"{num1}{operation}{num2} = {result}")

if __name__ == "__main__":
    # Entry point for the calculator application.
    calculator()


import requests

# Define the API endpoint
url = "https://www.dex.inside.philips.com/philips-ai-chat/chat/api/user/SendImageMessage"

# Define the headers with the cookie
headers = {
    'Cookie': '.AspNetCore.Cookies=CfDJ8KMy4_c-Wz5PjYx8z8V0OI6X9mfAfNIFv7JM3m4npf4GWwi8UZSa45_fwViSYioAAnP1DZ_LPgUmgujAsrTUxKUEkmPPeIzCXOQxAdda5uw0BsTjNcU_NpLUbPoaKGnob3oC3His37hjzv8gqGdzIu0xhxaXSTzGsM6ZMut6KsU3A2R8v6XnzlrIoc6gh0Qpjv_y1WR41PloTDlDMPp5Qy5IOWD7eA1YTCpCqb_6s0poFtbADoGSH8WMvEMtE85UTQfiKJfB8JkJU0UOGBG_Rrd0BJbdPOpiOL8TYrgp7jOodTOrws_yB1kr4JIPbakMuCjnrvvIxahFJ0mqCEIsArytAO1wj15ObnVDdepS7xUylLojEcRkDOkxk-xASWwzVwnIH3quxt3yqcBHWAK8VbRs_5jpHhZKP-akrrZIHLiWtEovUrSuY15GGfRJBMZUYqqEyHCON9JyAG2zg1s5AFNrXQhyfgWXMk5K4P7LGE3pNMqdpj5hX5_Yy_JiU0tj2KFvZxdc9Zpykca6vAfD9UZma5f7ROErVozy7U2AV-Ub4F97smDe6RvdlCxtwY4GZ7nHtjS-K8D3ILz6PL5g22WXN5BGo9Pz4DpG5dOrQ93YcHJ14hoJn-TEaHCKDpWvevZxWmBTJlGO5d4aCYEdo5dq_ehetUNdFy56RY8wfuZU-O7estmhnS-BJH9u5IAce3t4Z40aCxKrf7wVLh9x6-VqeK5IOXVzYKg0HaQdgwyzgPekipX4xRckR-dCWGaBiLIemjGRdArnoo8UfDZOWr7WCnlQVL4HGdZ_ZN3dc0qUXm8M4c1POFlnbvpvTVB_YNgbFNMfzg9eKwlmbk1AOq9QdzuqxaBxkDZ5xP9n6Selg3l_g1AinbWuefFemkcr2RktMliowTczMeiPqx1DFr0bIu_qSO9Ap7AlnQIOu60CdauIyG777FJ6O0sQaJ2_ZeaTfzwY9pnjFbJ9s6dsxTkwPcLA4x3_2j6bQ4sFCuQkOLwM92KpvrqM_lhojLgBPfbzEUKoliNGdhj4Y5ThH9o3rq5QBwfeLkFNOithALu_EKzX2ICtSH8C6lVNh3vaQ6wQvkael0T4GpzUeskjCF7D515qh6qhfldh_eCpwLvz4nwMU-LKpU499N0lLpsJ6nEkHJUiD_Z1eKEh4G3aGiSL4A3TrEiTIJGu1wNzAPxE-FqOuPjORBgDTfkEUY9Tb1tcgirvWj5LZhjK1ZXXqb2DIb0-A_EknjwaS3cKZQOu2YAhYdNy09Y5aGQ3Jq0CYQnbuxteyyi5oh8ImRV3y2cZmJ5CJSBd6VING2YoxIqygqc0q058bosvY7REllcT__EpkqHLvqSsG-CjmWf29Y0bngGzteetlRporvYGBLP5lw2HZD83IRJdHdfxZTj1GUSpBoX1QflyEX4EiS6szHAZY-rJsXnp3POiObYGmPAsM41QDWHJcAOY9Pos8Kt9Li30tzNc875XpDx6QBEoiobP4nBb2NknoKDk8vHHjpUXI1VYkDKeBNMKfJ287oNPEAYffgHy44Qj3c-RSWxzM5PgE06zmYM2s-F-SIEwUnr9hQSRHsgx3XeiAL0MODuFkAggFOazKbfb6n9WURMWTZ5RTX8b2mLpMD1EJt8R7Vdjik9MEId2X1blyEBG8Af9-RSQj09fe8M_46_rb43KIKR0wf4ySrQxn9rFjMCjON9cQQwRa2xg2iiRiSbTeM8JJ-FEFivCtfoIyrXMbmwDTJQYgn8APcSIHkPYQmR3xyslT-U_bxmZzgvrpU96Gy7m7qYcjA57LnC7RxgMZleIIa8x7PhXB0dMvYIxlpTZygkSAq6XxmJ665fZ7bhe3tvvx669VP2Jqo0reN1kZo3AHuETQUpKmINpKAKCym99o5o1HDcVEiFeA5MqN1UDSo-5LO3ZkGFK7rkiwYy1HlLBj9QICT0-zhZh5bZa6WMGZ0FaCHfB68bTPuQjWG_vsQQRlxz5wkH1eTFQvzZmDidIe7vbXRtMA_MApLqkab9yDGQA8G-a__O_JozKgSNQO56JccuMX0j7agbtFk5ZQnBWja9bLOsJ1d8z4rQk0EtFI1wOWecF-jFD8fxsRWuFElIodi6GVQEU24isErJP25tNO4XwrcD3HeEr7t4PstEf2PQytKS8MYhll1BV3kdgZ6pZleAL-PY5EnNWn_7_FXZo-nhVA9Oq2K_0zBdLeVtP-nCtvatbPzDkwDf1I9OnU8gQ8wr1E3gaEfPoN2tsM87rXTXVJv3Wsnp7jrwfSzNM-Tj1zJ8DzU9ogfZvl_3oPaRu2WGLDnsj6f6EgmXdAnRnshWpvR6sSJR4hJ0_Hi0E_S6AWd1kpy8Wd2ODkAQ-I_LqLyIGPI_IFb2y0dLgPpvhZFwNbSPcPzMQg8Sdl4ANUon2Z2_cYtoB8fQ43SQl4HPdRncZpjomDaMndt44VVliKPD0tcf7Y5Z5eWSx9PQk0uxZBV-XFn5VO1AZIQZ5cweRrgNf2LtM2dn4ZViKbjokkubbMM4tHGVOVsb7z0eEEug01QgXvbuzRfWwv_jdpWxGtRbOMW6pig61wuIBKVq7ivRma9nPsl-gJnMK1SGQQxjJZsqvASgm_PGZHumkS6o5lTie3SMNQ-JsF8ppa3t5F6OHk__EbjQklsqhbPLNSJFgwK5XOeQr3kYMcp1ilws8YsfOE4twxzxYNT91R1SDrtnAKIoWvRCuMYQri22ApsKdcDRPaxs4vmrd77YfEKrUKyXuaxswxcuadhRnZrK6BAQ; ai_user=V5697lqIHSnfr+8ozVDooj|2024-07-23T07:32:44.735Z; ARRAffinitySameSite=8da8ccc8fe610cb85ae6bee641a7cdab56856c5b0031afc971de42132583be1e; ai_session=8ovnE+MUKwSVCL20sII5OV|1722580808141|1722580810784; ARRAffinity=8da8ccc8fe610cb85ae6bee641a7cdab56856c5b0031afc971de42132583be1e',
    'Content-Type': 'application/json'
}

# Define the payload
payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is ML?"
                }
            ]
        }
    ]
}

# Make the POST request
#response = requests.post(url, json=payload, headers=headers)
response = requests.pot(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())


response = requests.pot(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())


#########################################$$$$$$$$$$$$$$$$$$$$$$$$


import os
import sys
import json
import requests

# GitHub environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
PR_NUMBER = os.getenv('PR_NUMBER')
GITHUB_API_URL = 'https://api.github.com'
custom_service_cookie = os.getenv('CUSTOM_SERVICE_COOKIE')

# Philips OpenAI API URL
AZURE_OPENAI_API_URL = 'https://www.dex.inside.philips.com/philips-ai-chat/chat/api/user/SendImageMessage'

# Headers for GitHub API requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Check if cookie is set, or exit
if not custom_service_cookie:
    print("Error: CUSTOM_SERVICE_COOKIE environment variable is not set")
    sys.exit(1)

# Custom headers for Philips API
philips_headers = {
    'Cookie': f'{custom_service_cookie}',  # Custom service authentication via cookie
    'Content-Type': 'application/json'
}

def get_changed_files():
    """Fetch the list of changed files in the PR."""
    url = f'{GITHUB_API_URL}/repos/{GITHUB_REPOSITORY}/pulls/{PR_NUMBER}/files'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    files = response.json()
    return files

def filter_relevant_files(files):
    """Filter files based on extensions."""
    relevant_extensions = (
        '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cs', '.c', '.cpp', '.h', '.hpp',  
        '.go', '.rb', '.php', '.html', '.css', '.kt', '.swift', '.scala', '.rs', '.sh', 
        '.dart', '.sql'
    )
    return [f for f in files if f['filename'].endswith(relevant_extensions)]

def fetch_added_lines_only(file):
    """Fetch only the added lines (lines starting with '+') from the diff."""
    patch = file.get('patch', '')
    added_lines = [line for line in patch.splitlines() if line.startswith('+') and not line.startswith('+++')]
    return '\n'.join(added_lines)

def get_pull_request_commit_id():
    """Fetch the head commit ID of the pull request."""
    url = f'{GITHUB_API_URL}/repos/{GITHUB_REPOSITORY}/pulls/{PR_NUMBER}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    pr_data = response.json()
    return pr_data['head']['sha']

def send_diff_to_openai(diff, rules):
    """Send the diff to the Azure OpenAI API for code review with cookie-based authentication."""
    payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Act as a senior code reviewer. Review the code changes provided in the diff below with a focus on critical issues:\n\n"
                            + rules +
                            "\n\nIf the code meets all the standards, respond with: 'Everything looks good.'"
                            " If there are critical issues that need attention, provide a brief summary (max 2 sentences) of the key areas needing improvement."
                            " Keep the response short, like a human reviewer might provide, and ignore non-critical issues or minor improvements."
                            "\n\nHere is the diff with only the added lines:\n\n"
                            + diff
                        )
                    }
                ]
            }
        ]
    }

    print("Payload being sent to DEX API:")
    print(json.dumps(payload, indent=2))

    try:
        response = requests.post(AZURE_OPENAI_API_URL, json=payload, headers=philips_headers)
        response.raise_for_status()

        print(f"API response status code: {response.status_code}")
        print(f"Raw response content: {response.text}")

        # Parse the response content as JSON
        response_data = response.json()

        # Extract the content from the API's response
        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            print("Unexpected response format from DEX API.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Failed to get a response from DEX API: {e}")
        return None

def post_review(content, commit_id, file):
    """Post a review comment on the PR."""
    review_comments = [{
        'path': file['filename'],
        'position': 1,  # General comment at the start of the diff
        'body': content
    }]

    url = f'{GITHUB_API_URL}/repos/{GITHUB_REPOSITORY}/pulls/{PR_NUMBER}/reviews'
    review_data = {
        'commit_id': commit_id,
        'body': 'Automated Code Review by OpenAI Azure 4o',
        'event': 'COMMENT',
        'comments': review_comments
    }

    try:
        response = requests.post(url, headers=headers, json=review_data)
        response.raise_for_status()
        print("Review posted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to post review: {e}")
        print(f"Response content: {response.content}")

def main():
    files = get_changed_files()
    relevant_files = filter_relevant_files(files)
    if not relevant_files:
        print("No relevant files to analyze.")
        sys.exit(0)

    # Fetch the correct commit ID from the PR
    commit_id = get_pull_request_commit_id()

    # Define the rules with detailed instructions for a focused review
    rules = """
    Focus only on critical issues in the code changes:
    - Identify potential bugs, security vulnerabilities, or significant performance issues.
    - Ignore non-critical style preferences, minor naming improvements, or trivial changes.
    - Summarize any critical issues with a maximum of 2 sentences.
    - If there are no critical issues, respond with 'Everything looks good.'
    """

    for file in relevant_files:
        print(f"Analyzing {file['filename']}...")
        added_lines = fetch_added_lines_only(file)
        if added_lines:
            print("Sending added lines to DEX API for review...")
            feedback = send_diff_to_openai(added_lines, rules)
            if feedback:
                post_review(feedback, commit_id, file)
            else:
                print(f"No feedback received for {file['filename']}.")
        else:
            print(f"No added lines found for {file['filename']}.")

if __name__ == '__main__':
    if not all([GITHUB_TOKEN, GITHUB_REPOSITORY, PR_NUMBER]):
        print("Missing environment variables.")
        sys.exit(1)
    main()

