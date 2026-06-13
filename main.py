import random
# -----------------------------
# Global Variables
# -----------------------------
player_name = ""

total_questions = 0
total_correct = 0
quizzes_played = 0

# -----------------------------
# Explore Africa
# Code in Place Final Project
# By: AbdulRahman Masamba
# -----------------------------

def welcome_screen():
    global player_name

    print("\n" * 2)

    print("=" * 80)

    print(r"""
 ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗
 ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
 █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗
 ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝
 ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗
 ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

                    🌍  EXPLORE AFRICA  🌍
    """)

    print("=" * 80)
    print("      Discover • Learn • Explore • Challenge Yourself")
    print()
    print("🦁 Test your knowledge of African Capitals")
    print("🐘 Discover Amazing Wildlife")
    print("🏔️ Learn Geography & Fun Facts")
    print()

    player_name = input("👤 Enter your name, Explorer: ")

    print()
    print(f"🌍 Welcome, {player_name}!")
    print("Get ready for an exciting journey across Africa!")
    print()

    input("Press Enter to begin your adventure...")

    # Clear screen
    for i in range(25):
        print()

def main():
    """
    Main function.
    Keeps showing the menu until the user decides to quit.
    """
    welcome_screen()

    while True:
        print_banner()

        print("1. 🌍 African Capitals Quiz")
        print("2. 🦁 Wildlife Quiz")
        print("3. 📚 Africa Fun Facts")
        print("4. 📊 Statistics Dashboard")
        print("5. 🏆 Achievement Certificate")
        print("6. 📖 Instructions")
        print("7. 🚪 Exit")

        choice = input("Choose an option (1-7): ")

        print()

        if choice == "1":
            capitals_quiz()

        elif choice == "2":
            wildlife_quiz()

        elif choice == "3":
            facts_quiz()

        elif choice == "4":
            show_statistics()
        
        elif choice == "5":
            show_certificate()
        
        elif choice== "6":
            show_instructions()
        

        elif choice == "7":
            print()
            print("=" * 60)
            print(f"🌍 Thank you for playing, {player_name}!")
            print("We hope you enjoyed exploring Africa.")
            print("Safe travels and keep learning!")
            print()
            print("Project created by AbdulRahman Masamba")
            print("=" * 60)
            break

        else:
            print("Invalid choice. Please try again.\n")


# ------------------------------------------------
# Prints the title of the project
# ------------------------------------------------
def print_banner():

    global player_name

    print("=" * 60)
    print("🌍 EXPLORE AFRICA: The Ultimate Quiz Adventure 🌍")
    print("=" * 60)

    print(f"Explorer: {player_name}")
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

# ----------------------------
# Show statistics dashboard
# ----------------------------

def show_statistics():

    global player_name
    global quizzes_played
    global total_questions
    global total_correct

    print("=" * 60)
    print("📊 PLAYER DASHBOARD")
    print("=" * 60)

    print(f"Explorer: {player_name}")
    print(f"Quizzes Played: {quizzes_played}")
    print(f"Questions Answered: {total_questions}")
    print(f"Correct Answers: {total_correct}")

    if total_questions > 0:
        accuracy = (total_correct / total_questions) * 100
    else:
        accuracy = 0

    print(f"Accuracy: {accuracy:.1f}%")

    if accuracy >= 90:
        print("🏆 Badge: Africa Legend")
    elif accuracy >= 75:
        print("🥇 Badge: Gold Explorer")
    elif accuracy >= 50:
        print("🥈 Badge: Silver Explorer")
    else:
        print("🥉 Badge: Rising Explorer")

    print()

    input("Press Enter to continue...")

# ----------------------------------------------
# This is a personlized certificate for the player
# ------------------------------------------------
def show_certificate():

    global player_name
    global total_questions
    global total_correct
    global quizzes_played

    print("\n")

    print("=" * 75)
    print("🏆 CERTIFICATE OF ACHIEVEMENT 🏆")
    print("=" * 75)
    print()

    print("            EXPLORE AFRICA")
    print("        Code in Place Final Project")
    print()

    print(f"This certifies that")
    print()

    print(f"          {player_name.upper()}")
    print()

    print("has successfully completed the")
    print("Explore Africa Learning Challenge.")
    print()

    print(f"Quizzes Completed : {quizzes_played}")
    print(f"Questions Answered: {total_questions}")
    print(f"Correct Answers   : {total_correct}")

    if total_questions > 0:
        accuracy = (total_correct / total_questions) * 100
    else:
        accuracy = 0

    print(f"Overall Accuracy  : {accuracy:.1f}%")

    print()

    if accuracy == 100:
        badge = "🏆 AFRICA LEGEND"

    elif accuracy >= 90:
        badge = "🥇 GOLD EXPLORER"

    elif accuracy >= 75:
        badge = "🥈 SILVER EXPLORER"

    elif accuracy >= 50:
        badge = "🥉 BRONZE EXPLORER"

    else:
        badge = "🌱 RISING EXPLORER"

    print(f"Achievement Badge : {badge}")

    print()
    print("Congratulations on your learning journey!")
    print()

    print("=" * 75)

    input("\nPress Enter to continue...")
# Capitals Quiz
# ------------------------------------------------
def capitals_quiz():
    """
    Quiz the user on African capitals.
    Questions are shuffled so the quiz
    is different each time.
    """
    global total_questions
    global total_correct
    global quizzes_played
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

    print(f"🎉 {player_name}, you scored {score}/{len(capitals)}!")

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
    total_questions += len(capitals)
    total_correct += score
    quizzes_played += 1
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
    global total_questions
    global total_correct
    global quizzes_played
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

    print(f"🎉 {player_name}, your score is {score}/{len(questions)}!")

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
    total_questions += len(questions)
    total_correct += score
    quizzes_played += 1
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
    global total_questions
    global total_correct
    global quizzes_played
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

            print(f"Incorrect! The correct answer is {answer.title()}.")
            print()

    # -----------------------------
    # Display Final Results
    # -----------------------------
    print("=" * 45)
    print("Quiz Finished!")
    print("=" * 45)

    print(f"🎉 {player_name}, you scored {score}/{len(facts)}!")

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
    total_questions += len(facts)
    total_correct += score
    quizzes_played += 1

    input("Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()
