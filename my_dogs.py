"""Create dogs."""
import dog


my_dog = dog.Dog("Tahoe", "Australian Shepherd")
print(my_dog)
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()

my_other_dog = dog.Dog("Nova", "Mixed Breed")
print(my_other_dog.name)
my_other_dog.bark()
