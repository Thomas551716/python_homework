"""import traceback

try: 
    # Open diary.txt in append mode using with statement
    with open("diary.txt", "a")as diary_file:
        prompt = "what happened today?"

        while True:
            try:
                user_input = input(prompt)
            except EOFError: #Handles Ctrl-D (EOF) gracefully
                print ("\nEnd of input detected.Exiting program.")
                break
            diary_file.write(user_input + "\n") # write input to file

            if user_input.lower() == "done for now":
                break #Exit loop if special phrase is entered

            prompt = "What else? " #update prompt for subsequent inputs
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = [f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {tace[2]}, Message: {trace[3]}' for trace in trace_back]

    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print (f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")"""
