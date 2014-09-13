name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = round(height / 0.39370)
weight = 180 # lbs
weight_kilo = round(weight /2.2046)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d cm tall." % height_cm
print "He's %d pounds heavy." % weight
print "He's %d kilos heavy." % weight_kilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
