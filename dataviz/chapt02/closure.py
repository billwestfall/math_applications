def get_counter(inc):
    count = 0
    def add():
        count += inc
        print('Current count: ' + str(count))
        return add
