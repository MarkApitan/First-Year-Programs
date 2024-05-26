from performer import Performer
from singer import Singer
from dancer import Dancer
singer = Singer("Alice", 25, "soprano")
print(singer.get_name())  # Alice
print(singer.get_age())   # 25
print(singer.get_vocal_range())  # soprano
singer.sing()  # Alice is singing with a soprano range.

# Creating a dancer
dancer = Dancer("Bob", 22, "ballet")
print(dancer.get_name())  # Bob
print(dancer.get_age())   # 22
print(dancer.get_dance_style())  # ballet
dancer.dance()  # Bob is performing ballet dance.

performer = Performer("Charlie", 30)
print(performer.get_name())  # Charlie
print(performer.get_age())   # 30