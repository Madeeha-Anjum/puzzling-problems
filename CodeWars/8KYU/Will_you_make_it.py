def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    #  nearest pump is _ miles away
    #  runs on about _ mpg.
    # There are _ gallons left.
    """

    car_can_travel = mpg * fuel_left
    if car_can_travel >= distance_to_pump:
        return True
    else:
        return False


if __name__ == "__main__":
    assert zero_fuel(50, 25, 2) == True
    assert zero_fuel(100, 50, 1) == False
