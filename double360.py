import random
D = 8
positions = []
for r1 in xrange(D):
    for r2 in xrange(r1+2, D):
        for k in xrange(r1+1, r2):
            for b1 in xrange(0, D, 2):
                if b1 in [r1, r2, k]:
                    continue
                for b2 in xrange(1, D, 2):
                    if b2 in [r1, r2, k]:
                        continue
                    rem_idx = [i for i in xrange(D) if i not in [r1, r2, k, b1, b2]]
                    for q_idx in xrange(len(rem_idx)):
                        pos = [None for _ in xrange(D)]
                        pos[r1] = 'R'
                        pos[r2] = 'R'
                        pos[k] = 'K'
                        pos[b1] = 'B'
                        pos[b2] = 'B'
                        pos[rem_idx[q_idx]] = 'Q'
                        for idx in rem_idx:
                            if idx != rem_idx[q_idx]:
                                pos[idx] = 'N'
                        positions.append(pos)

assert len(positions) == 960

moves = {
    'R': lambda x: [x],
    'B': lambda x: [x-1, x+1],
    'K': lambda x: [x-1, x, x+1],
    'Q': lambda x: [x-1, x, x+1],
    'N': lambda x: [x-2, x+2],
}

defended_positions = []

for pos in positions:
    defended = [False for _ in xrange(D)]
    for x, piece in enumerate(pos):
        for y in filter(lambda y: 0 <= y < D, moves[piece](x)):
            defended[y] = True
    if all(defended):
        defended_positions.append(pos)
print("total where all pawns defended={}".format(len(defended_positions)))
x=random.randrange(1,361,1)
y=random.randrange(1,361,1)
print("White position", x, defended_positions[x])

print("Black position",y,defended_positions[y])
