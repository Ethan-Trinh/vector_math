import math

class Vector:
    def __init__(self, x, y, z):
        self.x_component = x
        self.y_component = y
        self.z_component = z

    def set_x_component(self, new_x):
        self.x_component = new_x

    def set_y_component(self, new_y):
         self.y_component = new_y
    
    def set_z_component(self, new_z):
        self.z_component = new_z

    def print_vector(self):
        print(f"X: {self.x_component}")
        print(f"Y: {self.y_component}")
        print(f"Z: {self.z_component}")

def dot_product():
        pass

def cross_product(vector_a, vector_b):
        vector_c = Vector(0, 0, 0)
        vector_c.x_component = [(vector_a.y_component * vector_b.z_component) - (vector_a.z_component * vector_b.y_component)]
        vector_c.y_component = [(vector_a.x_component * vector_b.z_component) - (vector_a.z_component * vector_b.x_component)]
        vector_c.z_component = [(vector_a.x_component * vector_b.y_component) - (vector_a.y_component * vector_b.x_component)]
        return vector_c

def get_vector_value():
    user_input_X = input("X component: ")
    user_input_Y = input("Y component: ")
    user_input_Z = input("Z component: ")

    component_x = float(user_input_X)
    component_y = float(user_input_Y)
    component_z = float(user_input_Z)

    return Vector(component_x, component_y, component_z)


def main():
    print(f"Welcome to the Vector Math Program by Ethan Trinh!\n")

    print(f"Vector A:")
    vector_a = get_vector_value()

    print(f"\nVector B:")
    vector_b = get_vector_value()

    print(f"\nDot Product = 1: Cross Product = 2")   
    user_input = input('Please Choose a Vector Mode: ')
    if user_input == "1":
        pass
    elif user_input == "2":
        final_vector = cross_product(vector_a, vector_b)
        print(f"\nCross Product of A and B is: ")
        final_vector.print_vector()
        

if __name__ == '__main__':
    main()