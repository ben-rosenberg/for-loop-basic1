# Print integers from 1 to 150 (I assume inclusive)
def print1to150():
    for x in range(151):
        print(x)

# Print integers from 5 to 1000 that are even multiples of 5 (again, based on laters questions, I assume inclusive)
def mult_of_5():
    for x in range(5, 1001, 5):
        print(x)

# Print integers 1 to 100, but for multiples of 5 print "Coding", for multiples of 10 print "Coding Dojo"
def coding_dojo_1_to_100():
    for x in range(1, 101):
        if x % 10 == 0:
            print('Coding Dojo')
        elif x % 5 == 0:
            print('Coding')
        else:
            print(x)

# Print the sum of all odd numbers from 0 to 500,000
def sigma_odd_500k():
    sum = 0
    for x in range(500000):
        if x % 2 == 1:
            sum += x
    print(sum)

# Print all numbers from 2018 to 0, decrementing by 4
def countdown_by_fours():
    for x in range(2018, 0, -4):
        print(x)

# Print all numbers from lowNum to highNum that are multiples of mult
def mult_in_range(lowNum, highNum, mult):
    for x in range(lowNum, highNum + 1, 1):
        if x % mult == 0:
            print(x)

# Same as mult_in_range but swaps lowNum and highNum if lowNum is greater than highNum. This might be 
# desirable behavior in some cases, but probably not usually
def mult_in_range_fancy(lowNum, highNum, mult):
    if lowNum > highNum:
        temp = lowNum
        lowNum = highNum
        highNum = temp
    for x in range(lowNum, highNum + 1):
        if x % mult == 0:
            print(x)

print1to150()
mult_of_5()
coding_dojo_1_to_100()
sigma_odd_500k()
countdown_by_fours()
mult_in_range(2, 9, 3)

mult_in_range_fancy(9, 2, 3)
