def recognize_dialog_act(sentence):
    text = sentence.lower()

    if "?" in sentence:
        return "Question"

    if text.startswith(("hi", "hello", "hey")):
        return "Greeting"

    if text.startswith(("thank", "thanks")):
        return "Thanking"

    if text.startswith(("please", "tell me", "give me")):
        return "Request"

    if text.startswith(("yes", "okay", "sure")):
        return "Agreement"

    if text.startswith(("no", "not")):
        return "Disagreement"

    return "Statement"

dialog = input("Enter dialog: ")

print("\nDialog Act:", recognize_dialog_act(dialog))