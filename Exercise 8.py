players = {}

with open("players.txt") as f:
    # for line_number, line in enumerate(f):
    for line in f:
        line = line.split()

        # if len(line) < 2:
        #     print "I'm crashing here: " + str(line)
        #     print "This is line number: " + str(line_number)

        name = line[0] + ' ' + line[1]
        position = line[-1]
        players[name] = position

my_players =  sorted(players.items())
for name,position in my_players:

    print name + ' => ' + position

# for name, position in players.items():
#     print name + ' => ' + position















