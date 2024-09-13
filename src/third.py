def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(prompt.strip(), ", ".join(options))
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(", ".join(options)))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

lower_bound, upper_bound = 1, 20

while True:
    guess = (lower_bound + upper_bound) // 2
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"],
    )
    if result == "high":
        upper_bound = guess
    elif result == "low":
        lower_bound = guess
    if result == "hit":
        print("Wuhuu!")
        break

    print("I must have been too low, right?", result)
