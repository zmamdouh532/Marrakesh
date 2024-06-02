
# Create dictionary of course numbers and room numbers
room_dict = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}

# Create dictionary of course numbers and instructors
instructor_dict = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

# Create dictionary of course numbers and meeting times
meeting_dict = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NT110': '11:00 a.m.',
    'CM241': '1:00 p.m.'
}

# Prompt user for course number
course = input("Enter a course number: ")

# Look up room number, instructor, and meeting time based on course number
if course in room_dict:
    room_num = room_dict[course]
    instructor = instructor_dict[course]
    meeting_time = meeting_dict[course]
    print(f"Room number: {room_num}")
    print(f"Instructor: {instructor}")
    print(f"Meeting time: {meeting_time}")
else:
    print("Invalid course number.")

