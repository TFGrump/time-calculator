# times is an array of times that are in a tuple of (day, hrs, mins)
def add_time(times):
    days = 0
    hrs = 0
    mins = 0

    for time in times:
        total_mins = mins + time[2]
        mins = total_mins % 60

        total_hrs = hrs + time[1] + total_mins/60
        hrs = total_hrs % 24

        days = days + time[0] + total_hrs / 60

    return tuple((days, hrs, mins))


def parse_tuple(time):
    return "Days: %d, Hours: %d, Minutes: %d" % (time[0], time[1], time[2])


# Example use
hw_times = [(0, 8, 8), (0, 9, 12), (0, 6, 9), (0, 5, 5), (0, 5, 3), (0, 3, 30), (0, 8, 19), (0, 7, 54)]
print("total hw: " + parse_tuple(add_time(hw_times)))

sleep_times = [(0, 3, 51), (0, 5, 14), (0, 13, 33), (0, 8, 30), (0, 2, 29), (0, 7, 24),
               (0, 11, 6), (0, 8, 24), (0, 9, 34), (0, 10, 19), (0, 9, 12)]
print("Total sleep: " + parse_tuple(add_time(sleep_times)))

warframe_times = [(0, 0, 16), (0, 2, 45), (0, 2, 8), (0, 1, 22), (0, 2, 16),
                  (0, 2, 42), (0, 0, 33), (0, 0, 14), (0, 6, 23)]
print("Total warframe: " + parse_tuple(add_time(warframe_times)))

osu_times = [(0, 0, 45), (0, 1, 22), (0, 0, 50), (0, 0, 48), (0, 2, 8)]
print("Total osu!: " + parse_tuple(add_time(osu_times)))

dbd_times = [(0, 2, 40), (0, 2, 3), (0, 4, 20), (0, 1, 38)]
print("Total DbD: " + parse_tuple(add_time(dbd_times)))

other_games_times = [(0, 1, 45), (0, 1, 30), (0, 9, 10), (0, 0, 45), (0, 8, 55), (0, 3, 48), (0, 0, 28)]
print("total other games: " + parse_tuple(add_time(other_games_times)))

food_times = [(0, 0, 33), (0, 40, 0), (0, 2, 24), (0, 3, 17), (0, 2, 11),
              (0, 1, 6), (0, 1, 55), (0, 2, 15), (0, 0, 23), (0, 0, 57)]
print("Total food: " + parse_tuple(add_time(food_times)))

lecture_times = [(0, 2, 40), (0, 2, 13), (0, 2, 0), (0, 1, 33), (0, 3, 9)]
print("Total lecture: " + parse_tuple(add_time(lecture_times)))

friend_times = [(0, 9, 50), (0, 5, 30)]
print("Total hang out: " + parse_tuple(add_time(friend_times)))

misc_times = [(0, 2, 0), (0, 1, 6), (0, 0, 8), (0, 5, 30)]
print("Total Misc: " + parse_tuple(add_time(misc_times)))
