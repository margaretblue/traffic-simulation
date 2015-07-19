import numpy as np
import matplotlib
import statistics
import math
import random

class Road:
    """has length, type, chance of random slowing down, Tracks where cars are
        Road looks like this:
        |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ... | <= end
        0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20    999
        c3 c3 c3 c3 c3    c2 c2 c2 c2 c2          c1 c1 c1 c1 c1
                                                   ^           ^
        c1 is car.car_number 1                     |           |
                                                c1's rear   c1's front
        """

    def __init__(self, road_length=1000, road_type='straight', slowdown_percent=1):
        self.road_length = road_length
        self.road_type = road_type
        self.slowdown_percent = slowdown_percent
        # self.position_tracker = []
        self.road_positions_array = None


class Car:

    def __init__(self, car_name, current_position = 0, current_speed = 0, car_size=5, car_type='normal',
                 acceleration=2, max_speed=33.333, spacing_multiplier=1, chance_of_deceleration=.10,
                 percent_of_population=1):
        self.car_name = car_name    # car's initial place in line
        self.car_size = car_size        # car length in meters
        self.current_speed = current_speed
        self.type = car_type            # normal, aggressive or commercial
        self.acceleration = acceleration #  meters/s of acelleration until reach their max_speed if they haveve room
        self.max_speed = max_speed      # desired speed
        self.spacing_multiplier = spacing_multiplier #want at least a number of meters equal to their speed in meters/s
        self.chance_of_deceleration = chance_of_deceleration  #percent chance that driver will randomly slow down by 2ms
        self.percent_of_population = percent_of_population #percent representation of population of drivers on road
        self.current_position = current_position    #current position of TAIL of car in road
        # self.next_position = next.position

        def __str__(self):
            return "car[{car_name}]'s object".format(self.car_name)

        def move_own_car(self):
            """Just update position of self"""
            self.current_position = (self.current_position + self.current_speed) % 1000
            return self.current_position

class Simulation:
    """ONE 60-second trial"""
    def __init__(self, number_of_cars_on_road=30, duration=60, time_interval=1,
                 car_objects_dict = {}, speed_snapshots_array=[],
                 position_snapshots_array=[], second=0 ):
        self.number_of_cars_on_road = number_of_cars_on_road
        self.duration = duration                  #duration of 1 simulation in seconds, currently 60 seconds
        self.time_interval = time_interval                #snapshot/step point of speed, currently 1 second
        self.car_objects_dict  = car_objects_dict # {[0: <carobject>, 1: <carobject>}
        self.speed_snapshots_array = speed_snapshots_array
        self.position_snapshots_array = position_snapshots_array
        self.second = second

    def make_cars(self):
        """Instantiates 30 cars & puts their objects in car_objects_dict"""
        for i, car_obj in enumerate((range(self.number_of_cars_on_road))):
            # TODO: need to pass it current_position
            self.car_objects_dict[i] = Car(i)

    def get_car_object_by_name(self, car_name):
        """Given a car's name return the car object"""
        return self.car_objects_dict[car_name]

    def layout_cars(self):
        """Updates each car's current_position and creates initial layout list"""
        distances_of_cars_array = np.round(np.linspace(0,1000,31)) #for 30 car, have 31 spaces
        layout_list = []
        for i in range(30):
            x = -1 * (i+2)
            tail_position = distances_of_cars_array[x]
            layout_list.append(tail_position)
            #update car object's current_position
            self.get_car_object_by_name(i).current_position = tail_position
        print("tail of car 0 is:")
        print(self.get_car_object_by_name(0).current_position)
        print("tail of car 1 is:")
        print(self.get_car_object_by_name(1).current_position)
        print("tail of car 28 is:")
        print(self.get_car_object_by_name(28).current_position)
        print("tail of car 29   is:")
        print(self.get_car_object_by_name(29).current_position)
        """car in front of car0 is car29
            car in front of car1 is car0
            car in front of car2 is car1 """
        return layout_list

    def move_all_cars(self):
        """Move car ONE second. Uses speed rules to determine speed
        updates car's current_position in car object
        reports speed to speed_snapshots_array
        reports position to position_snapshots_array"""
        for i in range(30):
            # 1. Update speed
            my_car = self.car_objects_dict[i]
            print("*****")
            print(my_car.max_speed)
            if i == 0:
                car_in_front = self.car_objects_dict[29]
                print("car in front of car{} is car{} ".format(i, 29))
            else:
                car_in_front = self.car_objects_dict[i-1]
            # collision occurs when car_in_front == my_front
            speed = self.determine_speed(my_car, car_in_front)
            # update speed on car in self.speed_snapshots_array
            self.speed_snapshots_array[self.second,i] = speed
            my_car.current_speed = speed
            # 2. have the car move itself and update position
            # TODO ERROR! AttributeError: 'Car' object has no attribute 'move_own_car'
            # like hell it doesnt.
            # new_position = my_car.move_own_car()
            my_car.current_position = (my_car.current_position + my_car.current_speed) % 1000
            self.position_snapshots_array[self.second,i] = my_car.current_position

    def determine_speed(self, my_car, car_in_front):
        my_front = my_car.current_position + my_car.car_size
        current_speed = self.speed_snapshots_array[(self.second-1),my_car.car_name]
        print("current speed for car{} is {}".format(my_car.car_name, current_speed))
        if current_speed < (my_car.max_speed ):
        #     #will car collide?
        #     speed = current_speed + my_car.acceleration
        #     if car_in_front.current_position <= my_front + speed:
        #         speed =
        # TODO below is just a test of accellerating the cars 2ms each second
        # no rules
            speed = current_speed + my_car.acceleration
        speed = current_speed + my_car.acceleration
        return speed



    def run(self):
        """This runs ONE simulation or ONE 60-second trial"""
        # generate 2 empty np arrays for car speeds & car positions at each second
        self.speed_snapshots_array = np.zeros((self.duration, self.number_of_cars_on_road)) #(60,30)
        self.position_snapshots_array = np.zeros((self.duration, self.number_of_cars_on_road))
        self.make_cars()
        initial_layout_position_list = self.layout_cars()
        while self.second < 60:
        # TODO uncomment this code block if minute loop doesnt work
        # # layout where each car needs to be on the road and store in car.current_position
            self.move_all_cars()
            self.second += 1

        print(self.speed_snapshots_array)
        print(self.position_snapshots_array)

if __name__ == '__main__':
    simulation = Simulation()
    road = Road()
    simulation.run()
    print(simulation.speed_snapshots_array)
    print(simulation.position_snapshots_array)

