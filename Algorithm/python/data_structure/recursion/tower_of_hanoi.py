def move_hanoi_tower(height, from_pole, to_pole, with_pole):
    if height > 0:
        move_hanoi_tower(height - 1, from_pole, with_pole, to_pole)
        print('Move disk from %s to %s' % (from_pole, to_pole))
        move_hanoi_tower(height - 1, with_pole, to_pole, from_pole)

move_hanoi_tower(4, 'a', 'b', 'c')