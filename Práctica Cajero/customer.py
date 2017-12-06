class Customer:

    def __init__(self, arrival_id, arrival_time, amount_requested, amount_recieved,
    service_started_time, wait_time, departure_time):
        self.arrival_id = arrival_id
        self.arrival_time = arrival_time
        self.amount_requested = amount_requested
        self.amount_recieved = amount_recieved
        self.service_started_time = service_started_time
        self.wait_time = wait_time
        self.departure_time = departure_time

    def get_arrival_id(self):
        return self.arrival_id

    def set_arrival_id(self, arrival_id):
        self.arrival_id = arrival_id

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_amount_requested(self):
        return self.amount_requested

    def set_amount_requested(self, amount_requested):
        self.amount_requested = amount_requested

    def get_amount_recieved(self):
        return self.amount_recieved

    def set_amount_recieved(self, amount_recieved):
        self.amount_recieved = amount_recieved

    def get_service_started_time(self):
        return self.service_started_time

    def set_service_started_time(self, service_started_time):
        self.service_started_time = service_started_time

    def get_wait_time(self):
        return self.wait_time

    def set_wait_time(self, wait_time):
        self.wait_time = wait_time

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_info(self):
        info = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.arrival_id, self.arrival_time,
        self.amount_requested, self.amount_recieved, self.service_started_time, self.wait_time,
        self.departure_time)
        return info


'''
customer = Customer(1, 500, 5000, 5000, 510, 515, 530)
print(customer.get_info())
'''
