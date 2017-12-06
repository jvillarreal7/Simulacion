from funciones_aleatorias import *
from customer import *
from datetime import *
from collections import *
from random import *

# Variables globales de la simulación.

event_list = []

customer_queue = deque()

clock = 0
event_counter = 0
is_ATM_open = False
arrivals_counter = 0
is_ATM_online = False
customer_counter = 0
is_ATM_occupied = False
unsatisfied_customers_counter = 0
served_customers_counter = 0
supply_ongoing = False
departure_time_total = 0
service_time_total = 0
cash_disposal_total = 0
cash_supply_total = 0
ATM_offline_time = 0
ATM_offline_total = 0
wait_time_total = 0

# ATM_cash_disposal = 30
ATM_cash_disposal = int(input("Introduzca las disposiciones (* 100, pesos):\n"))
# time_between_arrivals = 200
time_between_arrivals = int(input("Introduzca el tiempo entre llegadas (segundos):\n"))
# service_time = 150
service_time = int(input("Introduzca el tiempo de servicio (segundos):\n"))
# supply_time = 600
supply_time = int(input("Introduzca el tiempo de abstecimiento (segundos):\n"))
# resupply_point = 10000
resupply_point = int(input("Introduzca el punto de reorden (pesos):\n"))
# supply_quantity = 300000
supply_quantity = int(input("Introduzca la cantidad fija de abastecimiento del cajero (pesos):\n"))


def init():
    global clock
    global event_list
    global event_counter
    global is_ATM_open
    global is_ATM_online
    clock = 32400
    ATM_opening = (32400, 1)
    ATM_closure = (64800, 2)
    event_list.append(ATM_opening)
    event_counter += 1
    event_list.append(ATM_closure)
    is_ATM_open = True
    is_ATM_online = True

def main():
    global event_list
    global clock

    while clock < 64800:
        event_list = sorted(event_list, key=lambda event: event[0])
        # print(event_list)
        current_event = event_list[0]
        if current_event[1] == 1:
            time = round(current_event[0])
            event_name = 'Apertura de Cajero'
            openATM(time)
            if event_counter < 21:
                print(event_name)
            event_list.pop(0)
        elif current_event[1] == 2:
            time = round(current_event[0])
            event_name = 'Cierre de Cajero'
            closeATM(time)
            if event_counter < 21:
                print(event_name)
            event_list.pop(0)
        elif current_event[1] == 3:
            time = round(current_event[0])
            event_name = 'Llegada de Cliente'
            customerArrival(time)
            if event_counter < 21:
                print(event_name)
            event_list.pop(0)
        elif current_event[1] == 4:
            time = round(current_event[0])
            event_name = 'Inicio de Atencion'
            serveCustomer(time)
            if event_counter < 21:
                print(event_name)
            event_list.pop(0)
        elif current_event[1] == 5:
            time = round(current_event[0])
            event_name = 'Salida de Cliente'
            customerDeparture(time)
            if event_counter < 21:
                print(event_name)
            event_list.pop(0)
        elif current_event[1] == 6:
            time = round(current_event[0])
            event_name = 'Abastecimiento de Efectivo'
            cashSupply(time)
            if event_counter < 21:
                print(event_name)
            event_list.pop(0)


    printFinalResults()



def openATM(current_time):
    global clock
    global event_counter
    global event_list
    global time_between_arrivals
    global supply_quantity

    clock = current_time
    is_ATM_open = True
    event_time = clock + time_between_arrivals
    event_list.append((event_time, 3))
    if event_counter < 21:
        eventPrinter(event_counter, clock, arrivals_counter,
        served_customers_counter, unsatisfied_customers_counter,
        customer_counter, supply_quantity)


def closeATM(current_time):
    global clock
    global event_counter
    global supply_quantity

    clock = current_time
    event_counter += 1
    is_ATM_open = False
    if event_counter < 21:
        eventPrinter(event_counter, clock, arrivals_counter,
        served_customers_counter, unsatisfied_customers_counter,
        customer_counter, supply_quantity)


def customerArrival(current_time):
    global clock
    global event_counter
    global arrivals_counter
    global unsatisfied_customers_counter
    global customer_counter
    global is_ATM_open
    global is_ATM_online
    global is_ATM_occupied
    global event_list
    global customer_queue
    global time_between_arrivals
    clock = current_time
    event_counter += 1
    arrivals_counter += 1
    if is_ATM_open:
        event_time = clock + exponencial(time_between_arrivals)
        event_list.append((event_time, 3))
    if is_ATM_open and is_ATM_online:
        if customer_counter < 8:
            customer = Customer(arrivals_counter, clock, None, None, None,
            None, None)
            customer_queue.append(customer)
            customer_counter += 1
            if is_ATM_occupied == False:
                event_list.append((clock, 4))
        else:
            unsatisfied_customers_counter += 1
    else:
        unsatisfied_customers_counter += 1
    if event_counter < 21:
        eventPrinter(event_counter, clock, arrivals_counter,
        served_customers_counter, unsatisfied_customers_counter,
        customer_counter, supply_quantity)


def serveCustomer(current_time):
    global clock
    global event_counter
    global supply_quantity
    global unsatisfied_customers_counter
    global is_ATM_occupied
    global event_list
    global customer_queue
    global service_time
    global ATM_cash_disposal

    clock = current_time
    event_counter += 1
    is_ATM_occupied = True
    customer_queue[0].set_service_started_time(clock)
    arrival = customer_queue[0].get_arrival_time()
    if (clock - arrival) / 60 > 5:
        unsatisfied_customers_counter += 1
    customer_queue[0].set_wait_time(clock - arrival)
    event_time = clock + exponencial(service_time)
    event_list.append((event_time, 5))
    customer_queue[0].set_amount_requested(uniforme(0, ATM_cash_disposal) * 100)
    requested_cash = customer_queue[0].get_amount_requested()
    if requested_cash <= supply_quantity:
        customer_queue[0].set_amount_recieved(requested_cash)
    else:
        unsatisfied_customers_counter += 1
        customer_queue[0].set_amount_recieved(supply_quantity)
        supply_quantity = 0
    if event_counter < 21:
        eventPrinter(event_counter, clock, arrivals_counter,
        served_customers_counter, unsatisfied_customers_counter,
        customer_counter, supply_quantity)


def customerDeparture(current_time):
    global clock
    global event_counter
    global departure_time_total
    global service_time_total
    global customer_queue
    global supply_quantity
    global customer_counter
    global served_customers_counter
    global unsatisfied_customers_counter
    global event_list
    global cash_disposal_total
    global wait_time_total
    global is_ATM_occupied
    global is_ATM_online
    global event_list
    global service_time
    global supply_time
    global resupply_point
    global ATM_offline_time
    global supply_ongoing

    clock = current_time
    event_counter += 1

    departure_time_total += clock - exponencial(service_time)

    service_time_total += exponencial(service_time)

    wait_time_total += customer_queue[0].get_wait_time()

    requested_cash = customer_queue[0].get_amount_requested()
    supply_quantity -= round(requested_cash)
    cash_disposal_total += round(requested_cash)

    customer_counter -= 1
    served_customers_counter += 1
    customer_queue.popleft()
    is_ATM_occupied = False
    if supply_quantity <= resupply_point and supply_ongoing == False:
        event_time = clock + exponencial(supply_time)
        event_list.append((event_time, 6))
        supply_ongoing = True
    if supply_quantity == 0:
        is_ATM_online = False
        ATM_offline_time = clock
        customer_queue = deque()
        del event_list[:]
        ATM_closure = (64800, 2)
        event_list.append(ATM_closure)
        unsatisfied_customers_counter += customer_counter
        customer_counter = 0

    if event_counter < 21:
        eventPrinter(event_counter, clock, arrivals_counter,
        served_customers_counter, unsatisfied_customers_counter,
        customer_counter, supply_quantity)


def cashSupply(current_time):
    global clock
    global event_counter
    global supply_quantity
    global is_ATM_online
    global resupply_point
    global ATM_offline_time
    global supply_ongoing
    global cash_supply_total
    global ATM_offline_total

    clock = current_time
    event_counter += 1
    supply_temp = resupply_point - supply_quantity
    supply_quantity += (resupply_point - supply_quantity)
    cash_supply_total += supply_temp
    if is_ATM_online == False:
        is_ATM_online = True
        ATM_offline_total += clock - ATM_offline_time
    supply_ongoing = False
    if event_counter < 21:
        eventPrinter(event_counter, clock, arrivals_counter,
        served_customers_counter, unsatisfied_customers_counter,
        customer_counter, supply_quantity)


def eventPrinter(event_counter, clock, arrivals_counter, served_customers_counter,
unsatisfied_customers_counter, customer_counter, supply_quantity):
    print("\n----------------------------------------")
    print("Evento {}:\n".format(event_counter))
    converted_time = str(timedelta(seconds=clock))
    print("Hora: {}".format(converted_time))
    print("Llegadas de clientes: {}".format(arrivals_counter))
    print("Clientes atendidos: {}".format(served_customers_counter))
    print("Clientes insatisfechos: {}".format(unsatisfied_customers_counter))
    print("Clientes en este momento: {}".format(customer_counter))
    print("Dinero en el cajero: {}".format(supply_quantity))
    print("----------------------------------------")

def printFinalResults():
    global event_counter
    global arrivals_counter
    global served_customers_counter
    global unsatisfied_customers_counter
    global cash_supply_total
    global cash_disposal_total
    global service_time_total
    global ATM_offline_total
    print("\n----------------------------------------\n")
    print("Resultados finales:\n")
    print("Número de eventos: {}".format(event_counter))
    print("Llegadas de clientes: {}".format(arrivals_counter))
    print("Clientes atendidos: {}".format(served_customers_counter))
    print("Insatisfacciones: {}".format(unsatisfied_customers_counter))
    print("Cantidad reabastecida: {}".format(cash_supply_total))
    print("Cantidad de disposición promedio: {}"
    .format(cash_disposal_total // served_customers_counter))
    print("Tiempo de servicio promedio: {} segundos"
    .format(service_time_total // served_customers_counter))
    print("Tiempo de espera promedio: {} segundos"
    .format((wait_time_total // served_customers_counter)))
    print("Tiempo fuera de servicio del cajero: {} segundos"
    .format(ATM_offline_total))
    print("Dinero en el cajero: {}".format(supply_quantity))
    print("\n----------------------------------------")



if __name__ == '__main__':
    init()
    main()
