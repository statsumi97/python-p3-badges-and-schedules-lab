def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f'Hello, my name is {name}.')
    return badges

def assign_rooms(names):
    room_assignments = []
    index = 0
    while index < len(names):
        room_assignments.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
        index += 1
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)

    for room_assignment in rooms:
        print(room_assignment)
    return None