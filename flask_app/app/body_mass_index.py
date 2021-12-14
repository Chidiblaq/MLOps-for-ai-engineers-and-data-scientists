def bmi_calculator(weight_kg, height_m):
    """
    A function to calculate the body mass index of an individual using the weight in kilogram and height in metres
    """

    bmi = weight_kg/(height_m*height_m)

    return bmi