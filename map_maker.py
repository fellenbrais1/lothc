# This is an experiment to make maps and display them for the player, later /
# more functionality would be added so that the room the player is in means /
# something, this might necessitate a full redesign of this system

# These are the components all rooms are made of, they are not very readable /
# yet but this could be improved in the future
# Tab these out if you need to see how the look next to one another
top_wall = " ---------"
top_wall_open = " ---   ---"
side_wall = "|         |"
side_wall_open_left = "          |"
side_wall_open_both = "           "
side_wall_open_right = "|          "
room_null = "          "

# These are lists of the components each type of room is made out of, all /
# needed possibilities are represented here
closed = [
    top_wall,
    side_wall,
    side_wall,
    side_wall,
    top_wall
]

open_top = [
    top_wall_open,
    side_wall,
    side_wall,
    side_wall,
    top_wall,
]

open_left = [
    top_wall,
    side_wall,
    side_wall_open_left,
    side_wall,
    top_wall
]

open_right = [
    top_wall,
    side_wall,
    side_wall_open_right,
    side_wall,
    top_wall,
]

open_bottom = [
    top_wall,
    side_wall,
    side_wall,
    side_wall,
    top_wall_open,
]

open_top_left = [
    top_wall_open,
    side_wall,
    side_wall_open_left,
    side_wall,
    top_wall,
]

open_top_right = [
    top_wall_open,
    side_wall,
    side_wall_open_right,
    side_wall,
    top_wall,
]

open_top_bottom = [
    top_wall_open,
    side_wall,
    side_wall,
    side_wall,
    top_wall_open
]

open_top_left_right = [
    top_wall_open,
    side_wall,
    side_wall_open_both,
    side_wall,
    top_wall
]

open_top_left_bottom = [
    top_wall_open,
    side_wall,
    side_wall_open_left,
    side_wall,
    top_wall_open
]

open_top_right_bottom = [
    top_wall_open,
    side_wall,
    side_wall_open_right,
    side_wall,
    top_wall_open
]

open_left_right = [
    top_wall,
    side_wall,
    side_wall_open_both,
    side_wall,
    top_wall,
]

open_left_bottom = [
    top_wall,
    side_wall,
    side_wall_open_left,
    side_wall,
    top_wall_open
]

open_left_right_bottom = [
    top_wall,
    side_wall,
    side_wall_open_both,
    side_wall,
    top_wall_open
]

open_right_bottom = [
    top_wall,
    side_wall,
    side_wall_open_right,
    side_wall,
    top_wall_open,
]

open_all = [
    top_wall_open,
    side_wall,
    side_wall_open_both,
    side_wall,
    top_wall_open
]

# 'null_room' is probably not a great as it includes the keyword 'null', a /
# mistake here could easily cause problems
null_room = [
    room_null,
    room_null,
    room_null,
    room_null,
    room_null,
]

# A list of all available room types that could be imported
available_rooms = [
    closed,
    open_top,
    open_left,
    open_right,
    open_bottom,
    open_top_left,
    open_top_right,
    open_top_bottom,
    open_top_left_right,
    open_top_left_bottom,
    open_top_right_bottom,
    open_left_right,
    open_left_bottom,
    open_left_right_bottom,
    open_right_bottom,
    open_all,
    null_room,
]

# The map building process:
# Maps need an id specified, then compositions for their rows, then which /
# rows are present in that map as below

# Added an 'id' variable to print where you are, I think this could be /
# included somewhere else as it just adds something else to worry about as it /
# is now
map_01_id = "understruts"

# Building row components for the map 'understruts':
# Each row has to have the same number of rooms otherwise it stops working /
# correctly, this can be fixed later. For now, pad empty spaces with /
# 'null_room's to make the row lengths equal
map_01_row_1 = open_right_bottom, open_left_right, open_left_bottom, \
               null_room,
map_01_row_2 = open_top, null_room, open_top_bottom, open_bottom,
map_01_row_3 = open_right, open_left_right_bottom, open_top_left, \
               open_top_bottom,
map_01_row_4 = null_room, open_top_right, open_left_right, open_top_left,

# A composite of the rows in 'understreets' for 'map_printer()' to use
map_01_understruts = [
    map_01_row_1,
    map_01_row_2,
    map_01_row_3,
    map_01_row_4,
]

# Playing around building other maps, it might be easier to plan out maps on /
# excel or something, so the grid is more easily visible, bit this isn't too /
# difficult so far

map_02_id = "hat factory"

map_02_row_1 = open_bottom, open_bottom, null_room, open_bottom
map_02_row_2 = open_top_bottom, open_top_bottom, open_bottom, open_top_bottom
map_02_row_3 = open_top_bottom, open_top_bottom, open_top_right, \
               open_top_left_bottom
map_02_row_4 = open_top_bottom, open_top_right, open_left_right, \
               open_top_left_bottom
map_02_row_5 = open_top_right, open_left_right, open_left_right, open_top_left

map_02_hat_factory = [
    map_02_row_1,
    map_02_row_2,
    map_02_row_3,
    map_02_row_4,
    map_02_row_5
]

map_03_id = "snake temple"

map_03_row_1 = open_right, open_left_right, open_left_bottom,
map_03_row_2 = null_room, null_room, open_top_bottom,
map_03_row_3 = null_room, open_right_bottom, open_top_left,
map_03_row_4 = open_right_bottom, open_top_left, null_room,
map_03_row_5 = open_top, null_room, null_room,

map_03_snake_temple = [
    map_03_row_1,
    map_03_row_2,
    map_03_row_3,
    map_03_row_4,
    map_03_row_5,
]

# 'map_printer()' looks at the map provided to it and generates a string to /
# print for each line of all the rooms in a row. Then it prints this and moves /
# on until all parts of the rooms in a row are printed, then it will move on /
# the next row until finished


def map_printer(map_provided, map_id_provided):
    print("\nYou take a look at your map...")
    print("\nYou are in the", map_id_provided.title())
    for row in map_provided:
        room_print = ""
        for i in range(5):
            for room_object in row:
                room_print += room_object[i] + '\t'
            else:
                if i <= 3:
                    room_print = room_print + "\n"
                else:
                    continue
        print(room_print)


# call 'map_printer()' with the specified map you want
map_printer(map_01_understruts, map_01_id)
map_printer(map_02_hat_factory, map_02_id)
map_printer(map_03_snake_temple, map_03_id)