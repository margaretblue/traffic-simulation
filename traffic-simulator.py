import numpy as np
import matplotlib
import statistics
import math
import random

class Road:
    """has length, type, chance of random slowing down, Tracks where cars are
        Road looks like this:
        |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ... | <= end
        0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20    1000
        c3 c3 c3 c3 c3    c2 c2 c2 c2 c2          c1 c1 c1 c1 c1
                                                   ^           ^
        c1 is car.car_number 1                     |           |
                                                c1's rear   c1's front
        """
    def __init__(self, length=1000, road_type='straight', slowdown_percent=1):
        self.length = length
        self.road_type = road_type
        self.slowdown_percent = slow_down_percent
        self.position_tracker = []

    def is_occupied(self):
        """returns if occupied or maybe car occupying it"""
        pass

    def on_road(self, position)
        """return True if position is on road"""
        return 0 <= x < self.road_type

class Car:
    def __init__(self, car_number, current_position, current_speed = 0, car_size=5, car_type='normal', acceleration=2, max_speed=33.333,
                 spacing_multiplier=1, chance_of_deceleration=.10, percent_of_population=1):
        self.car_number = car_number    # kind of like car name
        self.car_size = car_size        # car length in meters
        self.type = car_type            # normal, aggressive or commercial
        self.acceleration = acceleration #  meters/s of acelleration until reach their max_speed if they haveve room
        self.max_speed = max_speed      # desired speed
        self.spacing_multiplier = spacing_multiplier #want at least a number of meters equal to their speed in meters/s
        self.chance_of_deceleration = chance_of_deceleration  #percent chance that driver will randomly slow down by 2ms
        self.percent_of_population = percent_of_population #percent representation of population of drivers on road
        self.current_position = current_position    #current position where TAIL of car in road
        self.next_position = 0


    def space_requirement(self):
        """The average car is 5 meters long. Drivers want at least a number of meters equal
         to their speed in meters/second between them and the next car."""
        return self.length_of_car + ( self.current_speed * self.spacing_multiplier)

    def move(self):
        self.current_position = self.next_position

    @property
    def next_position(self):
        return simulation.determine_speed(self)


class Simulation:

    def __init__(self, number_of_cars_on_road=30, duration=60, time_interval=1):
        self.number_of_cars_on_road = number_of_cars_on_road
        self.duration = duration                  #duration of 1 simulation in seconds, currently 60 seconds
        self.time_interval = time_interval                #snapshot/step point of speed, currently 1 second
        all_intervals_car_speeds = []               # will be a list of 30 cars and their speed snapshot at each second
        current_interval_car_speeds_list =  []        # that second's list of 30 car speeds

    def determine_speed(self, car):
        """1. If car's current speed is below car.max_speed, it increases speed by car.acceleration until max_speed reached.
        2. it checks the distance to the car in front of it. If that
        distance is d space and the car has speed > distance then it reduces its velocity
        to d − 1 in order to avoid collision.
        3. if car will randomly slow down,  decriment speed by 2m/s.
        4. car moves ahead by v positions to
        complete the stage. These four steps take place in parallel for all N vehicles."""
        speed = car.current_speed
        # sequence of these MATTERS
        if car.current_speed < car.max_speed:
            speed += car.acceleration
        # it checks the distance to the car ahead/in front of it.
        # TODO: find distance to the car ahead of it and code next 2 comments ???
        # If that car.current_speed > distance_to_car_ahead:
            #  then it stops to avoid collision.
        if speed > 2 and self.will_randomly_slow_down(car):
            speed = car.current_speed - 2
            return speed   #get out of function
        if will_match_speed:
            # then speed matches car in front of it
            # speed= car.[car.car_number-1]
            # TODO how do I find the speed of the car in front of me???
            # consult road.position_tracker
            return speed
        return speed    # this is the # of meters car will move ahead

        # will_collide must be LAST statement
        if will_collide(car, road):
            speed = 0;

    def will_match_speed(self, car, road):
        """If another car is too close, drivers will match that car's speed until they have room again."""
        pass

    def will_collide(self, car, road):
        """ # check distance of car in front
        # number_of_meters_ahead = whatever the distance of car in front"""
        pass

    def will_randomly_slow_down(self, car):
        """Drivers will randomly (10% chance each second) slow by 2 m/s """
        return random.choice([True] * (100 * car.chance_of_deceleration) +
                             [False]* (100 * (1 - car.chance_of_deceleration)))






if __name__ == '__main__':
    pass





