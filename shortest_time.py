# find the shortest time from 6 random digits
# if it is not possible to build shortest time,
# the system will return 'NOT POSSIBLE'
# Args:
#   6 positive integer values
# Returns:
#   Shortest time build from those integer values
# Tested on values:
#   1,8,3,2,6,4 = 12:36:48
#   0,0,0,7,8,9 = 07:08:09
#   1,8,0,7,8,5 = 07:18:58
#   2,4,5,9,5,9 = NOT POSSIBLE
# To Run:
#   python <script_name> <six spaced integers>
#   e.g
#       python shortest_time.py 1 8 3 2 6 4

def values(a, b, c, d, e, f):
    to_list = [a, b, c, d, e, f]
    h = range(0, 24)
    m = range(0, 60)
    possible_hour = []
    possible_min_sec = []
    already_tried = []
    for i in range(len(to_list)):
        v = to_list[i]
        for j in range(len(to_list)):
            if i != j:
                ph = str(v) + str(to_list[j])
                if int(ph) in h:
                    if ph not in possible_hour:
                        possible_hour.append(ph)
                if int(ph) in m:
                    if ph not in possible_min_sec:
                        possible_min_sec.append(ph)
    return find_shortest_time(shortest_time(possible_hour, possible_min_sec, to_list))


def shortest_time(possible_hour, possible_min_sec, acutal_values):
    all_possible_combinations = []
    
    for hour in possible_hour:
        temp_values = acutal_values[:]

        for h in hour:
            temp_values.remove(int(h))
        for index, ms in enumerate(possible_min_sec):
            can_put = False
            b_temp = temp_values[:]
            for s in ms:
                if int(s) in temp_values:
                    can_put = True
                    temp_values.remove(int(s))
                else:
                    can_put = False
                    break
            temp_values = b_temp[:]
            if can_put:
                temp = temp_values[:]
                for m in ms:
                    if int(m) in temp:
                        temp.remove(int(m))
                for index, m_s in enumerate(possible_min_sec):
                    can_put = False
                    a_temp = temp[:]
                    for s in m_s:
                        if int(s) in temp:
                            can_put = True
                            temp.remove(int(s))
                        else:
                            can_put = False
                            break
                    temp = a_temp[:]
                    if can_put:
                        temp_combination = []
                        temp_combination.append(hour)
                        temp_combination.append(ms)
                        temp_combination.append(m_s)
                        all_possible_combinations.append(temp_combination)

    return all_possible_combinations

def find_shortest_time(all_possible_time_values):
    import time
    import datetime
    shortest_time = 'NOT POSSIBLE'
    temp_time = '23:59:59'
    if all_possible_time_values:
        shortest_time = temp_time
        shortest_time = time.strptime(shortest_time, '%H:%M:%S')
        for short_time in all_possible_time_values:
            t = ':'.join(short_time)
            t1 = time.strptime(t, '%H:%M:%S')
            if t1 < shortest_time:
                shortest_time = t1

    if shortest_time != 'NOT POSSIBLE':
        return datetime.datetime(*shortest_time[:6]).time()
    return shortest_time

def main(args):
    if len(args) < 6:
        print('Required 6 integers')
    else:
        a, b, c, d, e, f = (int(e) for e in args)
        print(values(a, b, c, d, e, f))

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

