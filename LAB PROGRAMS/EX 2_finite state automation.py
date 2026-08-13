def finite_automaton(string):
    state = "q0"
    path = [state]

    for symbol in string:
        if state == "q0":
            if symbol == "a":
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if symbol == "a":
                state = "q1"
            elif symbol == "b":
                state = "q2"
            else:
                state = "q0"

        elif state == "q2":
            if symbol == "a":
                state = "q1"
            else:
                state = "q0"

        path.append(state)

    print("Transition Path:", " → ".join(path))

    if state == "q2":
        print("Accepted")
    else:
        print("Rejected")


string = input("Enter a string: ")

finite_automaton(string)