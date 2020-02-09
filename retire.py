# function for calculating retirement age (or 'Not possible') based on inputted current age, annual salary, percentage saved, and savings goal
def retire(age, salary, percentage, goal):
    yearly = (salary * percentage) * 1.35
    save_time = round(goal / yearly)

    r_age = age + save_time

    if r_age >= 100:
        return ['Not possible', r_age]

    return r_age
