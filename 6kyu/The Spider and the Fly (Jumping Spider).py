#Task:

# Background
# A spider web is defined by

# "rings" numbered out from the centre as 0, 1, 2, 3, 4

# "radials" labelled clock-wise from the top as A, B, C, D, E, F, G, H

# Here is a picture to help explain:

# https://i.imgur.com/tGeWQVq.png
# Web Coordinates
# As you can see, each point where the rings and the radials intersect can be described by a "web coordinate".

# So in this example the spider is at H3 and the fly is at E2

# Kata Task
# Our friendly jumping spider is resting and minding his own spidery business at web-coordinate spider.

# An inattentive fly bumbles into the web at web-coordinate fly and gets itself stuck.

# Your task is to calculate and return the distance the spider must jump to get to the fly.

# Example
# The solution to the scenario described by the picture is 4.63522

# Notes
# The centre of the web will always be referred to as A0
# The rings intersect the radials at evenly spaced distances of 1 unit


# my solution:
import math 
def spider_to_fly(spider, fly):
    radials = 'ABCDEFGH'
    angleStep = math.pi / 4
    
    spiderRadial, spiderRing, flyRadial, flyRing = spider[0], int(spider[1]), fly[0], int(fly[1])
    angleSpider, angleFly = radials.index(spiderRadial) * angleStep, radials.index(flyRadial) * angleStep
    
    xSpider, ySpider = spiderRing * math.cos(angleSpider), spiderRing * math.sin(angleSpider)
    xFly, yFly = flyRing * math.cos(angleFly), flyRing * math.sin(angleFly)
    
    return math.sqrt((xSpider - xFly)**2 + (ySpider - yFly)**2)
    