def create_phone_number(n):
    form = "($$$) $$$ $$$$"

    for index in range(0, len(n)):
        form = form.replace('$', str(n[index]), 1)
        print(form)

    return form


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
