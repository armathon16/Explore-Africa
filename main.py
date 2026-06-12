import random

# -----------------------------
# Explore Africa
# Code in Place Final Project
# By: AbdulRahman Masamba
# -----------------------------


def main():
    """
    Main function.
    Keeps showing the menu until the user decides to quit.
    """

    while True:
        print_banner()

        print("1. Play Capitals Quiz")
        print("2. Play Wildlife Quiz")
        print("3. Play Fun Facts Quiz")
        print("4. Instructions")
        print("5. Exit")
        print()

        choice = input("Choose an option (1-5): ")

        print()

        if choice == "1":
            capitals_quiz()

        elif choice == "2":
            wildlife_quiz()

        elif choice == "3":
            facts_quiz()

        elif choice == "4":
            show_instructions()

        elif choice == "5":
            print("Thank you for exploring Africa!")
            break

        else:
            print("Invalid choice. Please try again.\n")


# ------------------------------------------------
# Prints the title of the project
# ------------------------------------------------
def print_banner():

    print("=" * 50)
    print("        🌍 EXPLORE AFRICA 🌍")
    print("=" * 50)
    print("Learn • Play • Discover")
    print()


# ------------------------------------------------
# Displays instructions
# ------------------------------------------------
def show_instructions():

    print("Instructions")
    print("-" * 30)

    print("Choose a quiz category.")
    print("Type your answer.")
    print("Each correct answer earns one point.")
    print("Your score will be shown at the end.")
    print()

    input("Press Enter to return to the menu...")
    print()



# Capitals Quiz
# ------------------------------------------------
def capitals_quiz():
    """
    Quiz the user on African capitals.
    Questions are shuffled so the quiz
    is different each time.
    """

    # Dictionary:
    # Key = Country
    # Value = Capital
    capitals = {
        "Malawi": "Lilongwe",
        "Kenya": "Nairobi",
        "Nigeria": "Abuja",
        "Ghana": "Accra",
        "South Africa": "Pretoria",
        "Egypt": "Cairo",
        "Zambia": "Lusaka",
        "Tanzania": "Dodoma",
        "Uganda": "Kampala",
        "Rwanda": "Kigali"
    }

    # Convert dictionary keys into a list
    countries = list(capitals.keys())

    # Shuffle the order of questions
    random.shuffle(countries)

    # Store the user's score
    score = 0

    print("=" * 40)
    print("🌍 AFRICAN CAPITALS QUIZ")
    print("=" * 40)
    print()

    # Ask every question
    for country in countries:

        answer = input(
            f"What is the capital city of {country}? "
        )

        # Compare answers without worrying
        # about upper/lower case
        if answer.lower() == capitals[country].lower():

            print("✅ Correct!\n")
            score += 1

        else:

            print(
                f"❌ Incorrect! The correct answer is {capitals[country]}.\n"
            )

    # -------------------------
    # Final Results
    # -------------------------
    print("=" * 40)
    print("Quiz Complete!")
    print("=" * 40)

    print(f"You scored {score}/{len(capitals)}")

    percentage = (score / len(capitals)) * 100

    if percentage == 100:
        print("🏆 PERFECT! You are an Africa Legend!")

    elif percentage >= 80:
        print("⭐ Excellent! You are an Africa Expert!")

    elif percentage >= 60:
        print("👍 Great job! Keep exploring!")

    elif percentage >= 40:
        print("🙂 Nice effort! You're learning fast!")

    else:
        print("📚 Keep studying and try again!")

    print()

    input("Press Enter to return to the main menu...")


# ------------------------------------------------
# Placeholder for Wildlife Quiz
# ------------------------------------------------
# ------------------------------------------------
# Wildlife Quiz
# ------------------------------------------------
def wildlife_quiz():
    """
    Tests the user's knowledge of African wildlife.
    """

    # Each question is stored as a tuple:
    # (question, correct_answer)
    questions = [
        ("Which is the largest land animal in Africa?", "elephant"),
        ("Which animal is known as the King of the Jungle?", "lion"),
        ("Which African animal has black and white stripes?", "zebra"),
        ("Which is the tallest animal in the world?", "giraffe"),
        ("Which animal is famous for its large horn and is endangered?", "rhino"),
        ("Which fast-running spotted cat lives in Africa?", "cheetah"),
        ("Which huge animal spends much of its time in rivers?", "hippo"),
        ("Which reptile is one of the deadliest predators in the Nile River?", "crocodile")
    ]

    # Shuffle the order of questions
    random.shuffle(questions)

    # Keep track of score
    score = 0

    print("=" * 40)
    print("🦁 AFRICAN WILDLIFE QUIZ")
    print("=" * 40)
    print()

    # Ask every question
    for question, answer in questions:

        user_answer = input(question + " ")

        # Ignore uppercase/lowercase differences
        if user_answer.lower() == answer.lower():

            print("✅ Correct!")

            # Bonus educational fact
            if answer == "elephant":
                print("Fun Fact: African elephants are the world's largest land animals!")

            elif answer == "lion":
                print("Fun Fact: Lions live in groups called prides!")

            elif answer == "giraffe":
                print("Fun Fact: Giraffes can grow over 5 meters tall!")

            elif answer == "cheetah":
                print("Fun Fact: Cheetahs can run over 100 km/h!")

            print()

            score += 1

        else:

            print(f"❌ Incorrect! The answer is {answer}.")
            print()

    # -----------------------------
    # Final Results
    # -----------------------------
    print("=" * 40)
    print("Wildlife Quiz Complete!")
    print("=" * 40)

    print(f"Your score: {score}/{len(questions)}")

    percent = (score / len(questions)) * 100

    if percent == 100:
        print("🏆 Wildlife Master!")

    elif percent >= 80:
        print("🦁 Safari Expert!")

    elif percent >= 60:
        print("🌿 Great Explorer!")

    elif percent >= 40:
        print("🙂 Nice effort!")

    else:
        print("📚 Time to learn more about African wildlife!")

    print()

    input("Press Enter to return to the main menu...")

# ------------------------------------------------
# Placeholder for Fun Facts Quiz
# ------------------------------------------------
# ------------------------------------------------
# Africa Fun Facts Quiz
# ------------------------------------------------
def facts_quiz():
    """
    A quiz that teaches users interesting facts
    about Africa.
    """

    # Each tuple contains:
    # (Question, Correct Answer)
    facts = [
        ("Which desert is the largest in Africa?", "sahara"),
        ("Which river is the longest in Africa?", "nile"),
        ("Which country is famous for the pyramids?", "egypt"),
        ("Which ocean lies on Africa's east coast?", "indian"),
        ("Which country is known as the Warm Heart of Africa?", "malawi"),
        ("Which mountain is the highest in Africa?", "kilimanjaro"),
        ("Which island nation lies off Africa's southeast coast?", "madagascar"),
        ("Which sea lies north of Africa?", "mediterranean")
    ]

    # Shuffle the questions
    random.shuffle(facts)

    score = 0

    print("=" * 45)
    print("🌍 AFRICA FUN FACTS QUIZ")
    print("=" * 45)
    print()

    # Ask every question
    for question, answer in facts:

        user_answer = input(question + " ")

        # Ignore uppercase/lowercase differences
        if user_answer.lower() == answer.lower():

            print("✅ Correct!")

            # Display an educational fact
            if answer == "sahara":
                print("Fun Fact: The Sahara covers over 9 million square kilometers!")

            elif answer == "nile":
                print("Fun Fact: The Nile flows through 11 countries!")

            elif answer == "egypt":
                print("Fun Fact: Egypt's pyramids are over 4,500 years old!")

            elif answer == "malawi":
                print("Fun Fact: Malawi is often called 'The Warm Heart of Africa' because of its friendly people!")

            elif answer == "kilimanjaro":
                print("Fun Fact: Mount Kilimanjaro stands about 5,895 meters tall!")

            elif answer == "madagascar":
                print("Fun Fact: Over 90% of Madagascar's wildlife is found nowhere else!")

            print()

            score += 1

        else:

            print(f"❌ Incorrect! The correct answer is {answer.title()}.")
            print()

    # -----------------------------
    # Display Final Results
    # -----------------------------
    print("=" * 45)
    print("Quiz Finished!")
    print("=" * 45)

    print(f"You scored {score}/{len(facts)}")

    percentage = (score / len(facts)) * 100

    if percentage == 100:
        print("🏆 Amazing! You're an Africa Genius!")

    elif percentage >= 80:
        print("⭐ Excellent! You know Africa very well!")

    elif percentage >= 60:
        print("🌍 Great job! Keep learning!")

    elif percentage >= 40:
        print("🙂 Nice attempt!")

    else:
        print("📚 Explore more about Africa and try again!")

    print()

    input("Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()
