from random import sample

if __name__ == "__main__":
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))

    try:
        target = int(input('Pick a number between 0-100: '))
        print(f'List: {rand_list}')
        if target in rand_list:
            print(f'Found {target} in index {rand_list.index(target)}')
        else:
            print(f'Cannot find  {target} in the list')
    except ValueError:
        print('Invalid input')
