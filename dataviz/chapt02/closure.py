def get_counter(inc):
    count = 0
    def add():
        nonlocal count
        count += inc
        print('Current count: ' + str(count))
        return add
cntr = get_counter(2)
cntr()
