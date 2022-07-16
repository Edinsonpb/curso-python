def run():
    my_dict = {}

    for i in range(1, 1000):
        my_dict[i] = pow(i, 1/2)
    print(my_dict)

if __name__ == '__main__':
    run()