def BMI():
    height=input("input user height (m):")
    weight=input("input user weight (kg):")
    BMI=weight/(height*height)
    print BMI
    if BMI<=18.5:
        res='Underweight'
    elif 18.5<BMI<=23:
        res='nomarlweight'
    elif 23<BMI<=25:
        res='ove weight'
    elif 25<BMI<=30:
        res='obesity'
    elif 30<BMI<=35:
        res='very obesity'
    else:
        res='extremly obesity'
    return res
print BMI()