print("Calculation of the daily calorie norm is based on the Mifflin-Geor formula")
gender = input("Enter your gender (Male/Female): ")
w = int(input("Enter your weight in kilograms: "))
h = int(input("Enter your height in centimeters: "))
a = int(input("Enter your age: "))

kcal_dict = {
    ('male', '<18', 'weak'): lambda w, h, a: (0.063*w+2.896)*240*1,
    ('male', '18-30', 'weak'): lambda w, h, a: (0.063*w+2.896)*240*1,
    ('male', '31-60', 'weak'): lambda w, h, a: (0.0484*w+3.653)*240*1,
    ('male', '>60', 'weak'): lambda w, h, a: (0.0491*w+2.459)*240*1,
    ('male', '<18', 'moderate'): lambda w, h, a: (0.063*w+2.896)*240*1.3,
    ('male', '18-30', 'moderate'): lambda w, h, a: (0.063*w+2.896)*240*1.3,
    ('male', '31-60', 'moderate'): lambda w, h, a: (0.0484*w+3.653)*240*1.3,
    ('male', '>60', 'moderate'): lambda w, h, a: (0.0491*w+2.459)*240*1.3,
    ('male', '<18', 'intense'): lambda w, h, a: (0.063*w+2.896)*240*1.5,
    ('male', '18-30', 'intense'): lambda w, h, a: (0.063 *w+ 2.896)*240*1.5,
    ('male', '31-60', 'intense'): lambda w, h, a: (0.0484 *w+ 3.653)*240*1.5,
    ('male', '>60', 'intense'): lambda w, h, a: (0.0491*w+2.459)*240*1.5,
    ('female', '<18', 'weak'): lambda w, h, a: (0.062*w+2.036)*240*1,
    ('female', '18-30', 'weak'): lambda w, h, a: (0.062*w+2.036)*240*1,
    ('female', '31-60', 'weak'): lambda w, h, a: (0.034*w+3.538)*240*1,
    ('female', '>60', 'weak'): lambda w, h, a: (0.038*w+2.755)*240*1,
    ('female', '<18', 'moderate'): lambda w, h, a: (0.062*w+2.036)*240*1.3,
    ('female', '18-30', 'moderate'): lambda w, h, a: (0.062*w+2.036)*240*1.3,
    ('female', '31-60', 'moderate'): lambda w, h, a: (0.034*w+3.538) * 240 * 1.3,
    ('female', '>60', 'moderate'): lambda w, h, a: (0.038 * w + 2.755) * 240 * 1.3,
    ('female', '<18', 'intense'): lambda w, h, a: (0.0621*w+2.036)*240*1.5,
    ('female', '18-30', 'intense'): lambda w, h, a: (0.062*w+2.036)*240*1.5,
    ('female', '31-60', 'intense'): lambda w, h, a: (0.034*w+3.538)*240*1.5,
    ('female', '>60', 'intense'): lambda w, h, a: (0.038*w+2.755)*240*1.5,
}
