def check_blank(question, error_msg):
    while True:
        response =  input(question)
        if response == "":
            print(error_msg)
        else:
            return response.capitalize()