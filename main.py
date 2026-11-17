from pyscript import document, display

# ==========================================
# index.html Python Code (for Seatwork 1)
# ==========================================

# List of Hogwarts students
# retrieved list of members from AI by generating
students = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Draco Malfoy",
    "Luna Lovegood",
    "Neville Longbottom",
    "Ginny Weasley",
    "Fred Weasley",
    "George Weasley",
    "Cedric Diggory",
    "Cho Chang",
    "Seamus Finnigan",
    "Dean Thomas",
    "Parvati Patil",
    "Padma Patil",
    "Lavender Brown",
    "Pansy Parkinson",
    "Gregory Goyle",
    "Vincent Crabbe",
    "Colin Creevey",
    "Jacque Delmudez",
]


def verify(e):
  # Clear the old result
  document.getElementById("result-box").innerHTML = ""

  # Adding input whitespace sanitization before combining name strings
  first_name = document.getElementById("firstname").value.strip()
  last_name = document.getElementById("lastname").value.strip()

  # Put the first and last name together
  full_name = f"{first_name.title()} {last_name.title()}"

  # Check if either input is empty
  is_empty = first_name == "" or last_name == ""

  # Check if the name is in the student list
  is_member = full_name in students

  # Messages depending on whether the student is in the list
  messages = [
      f"Sorry {full_name}, your name is not on the list. Maybe next time?",
      f"Congratulations {full_name}! You are a student at Hogwarts University. 🧹",
  ]

  # Not an empty input = use the membership message
  # One of the inputs is empty = tells user to enter both names
  empty_messages = [
      messages[is_member],
      "Please enter both your first and last name.",
  ]

  # This will get the message to show
  result_message = empty_messages[is_empty]

  # Show the result
  display(result_message, target="result-box")


# ==========================================
# page2.html Python Code (from Drill 2)
# ==========================================

# List of original Hogwarts students
students = {
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Draco Malfoy",
    "Luna Lovegood",
    "Neville Longbottom",
    "Ginny Weasley",
    "Fred Weasley",
    "George Weasley",
    "Cedric Diggory",
    "Cho Chang",
    "Seamus Finnigan",
    "Dean Thomas",
    "Parvati Patil",
    "Padma Patil",
    "Lavender Brown",
    "Pansy Parkinson",
    "Gregory Goyle",
    "Vincent Crabbe",
    "Colin Creevey",
    "Jacque Delmudez",
}

# Set for newly added students
new_students = set()


# Adds a new student to the list
def add(e):
  # Gets the inputted names
  first = document.getElementById("firstname").value.strip()
  last = document.getElementById("lastname").value.strip()

  # Combines the first and last names
  full_name = f"{first} {last}"

  # Adds the new student to the new_students set
  new_students.add(full_name)

  # Combines both sets dynamically
  master_students = students | new_students

  # Counts the total members
  count = len(master_students)

  # Revised from Drill 2 comments:
  # Sorts alphabetically and joins line-by-line using "<br>" so HTML renders each name on its own line
  members_list = "<br>".join(sorted(master_students))

  # Updates the elements directly using innerHTML instead of display()
  document.getElementById("result").innerHTML = members_list
  document.getElementById("total").innerHTML = (
      f"There are {count} official students in Hogwarts School of Witchcraft! ✨"
  )

  # Clears the input fields
  document.getElementById("firstname").value = ""
  document.getElementById("lastname").value = ""


# ==========================================
# page3.html Python Code (from Skills Test)
# ==========================================

nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Se": ("Selenium", 34, 78.96),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.904),
    "He": ("Helium", 2, 4.0026),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.95),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222),
}


def finder(e):
  # Clear the old result box
  document.getElementById("result-box").innerHTML = ""

  # Get the symbol from the input field
  symbol = document.getElementById("symbol").value.strip().capitalize()

  # Use .get() to look up the symbol, and also checks if it doesn't exist (not found)
  result = nonmetals.get(symbol, ("Element not found", "-", "-"))

  output_html = f"""
    <b>Symbol:</b> {symbol.title()} <br>
    <b>Element Name:</b> {result[0]} <br>
    <b>Atomic Number:</b> {result[1]} <br>
    <b>Atomic Mass:</b> {result[2]} <br>
    """

  # Display the result inside the result-box div
  document.getElementById("result-box").innerHTML = output_html