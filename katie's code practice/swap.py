from __init__ import app
def swapnumbers(age1, age2):
    if age1 > age2:
        temp = age1
        age1 = age2
        age2 = temp
    return age1, age2


if __name__ == "__main__":
    app.run(debug=True)