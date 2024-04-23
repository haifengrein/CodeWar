"""
Task

Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.

Example

For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.
"""
def growing_plant(up_speed, down_speed, desired_height):
    current_height = 0
    days = 0
    while current_height <= desired_height:
        current_height += up_speed
        days +=1
        if current_height >= desired_height:
            return days
        current_height -= down_speed
    return days