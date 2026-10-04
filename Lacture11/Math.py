class Calculate_area:

    def rectengle_area(self, w, h):
        return w * h
    @classmethod
    def triangle_area(cls, b, h):
        return 0.5 * b * h
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r
cal = Calculate_area()
cal_rec = cal.rectengle_area(5, 6)
cal_tri = cal.triangle_area(4, 6)
cal_cir = cal.circle_area(5)

print("Area of rectangle is: ", cal_rec)
print("Area of triangle is: ", cal_tri)
print("Area of circle is: ", cal_cir)