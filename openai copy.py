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
