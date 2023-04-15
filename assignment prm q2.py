#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Triangle:
    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def validate_triangle(self):
        # check if the sum of any two sides is greater than the third side
        if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            print("Valid Triangle")
        else:
            print("Invalid triangle")

class Rectangle:
    def _init_(self, l, b, l1, b1):
        self.l = l
        self.b = b
        self.l1 = l1
        self.b1 = b1
        
    def validate_rectangle(self):
        # check if two pairs of sides are equal and they are input in correct order
        if self.l == self.l1 and self.b == self.b1:
            print("Valid Rectangle")
        elif self.l == self.b1 and self.b == self.l1:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")
            

# take input
t = list(map(int, input().strip().split()))
r = list(map(int, input().strip().split()))

# create objects and validate
tri = Triangle(*t)
tri.validate_triangle()

rect = Rectangle(*r)
rect.validate_rectangle()

