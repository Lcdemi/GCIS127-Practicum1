#luke demi practicum 1

def slice(a_list, start, stop, step):
    new_a_list = []
    comparative_list = []
    for i in range(start, stop, step):
        comparative_list.append(i)
    #print(comparative_list) test code
    
    for value in a_list:
        not_found = True
        for i in comparative_list:
            if value == i:
                not_found = False
        if not_found == True:
            new_a_list.append(value)
    return new_a_list

def list_to_string(a_list):
    list_string = ""
    counter = 0
    for character in a_list:
        list_string += str(counter)
        list_string += " - "
        list_string += str(character)
        list_string += "\n"
        counter += 1
    return list_string

def collatz(n):
    if n < 1:
        return "Undefined"
    elif n == 1:
        return str(int(1))
    elif n % 2 == 0:
        return str(int(n/2)) + " " + collatz(n/2)
    elif n % 2 == 1:
        return str(int(3*n+1)) + " " + collatz(3 * n + 1)
    
import re
def count_digits(filename):
    zeroes = 0; ones = 0; twos = 0; threes = 0; fours = 0; fives = 0; sixes = 0; sevens = 0; eights = 0; nines = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            for num in line:
                if re.findall("\D", num):
                    ...
                elif int(num) == 0:
                    zeroes += 1
                elif int(num) == 1:
                    ones += 1
                elif int(num) == 2:
                    twos += 1
                elif int(num) == 3:
                    threes += 1
                elif int(num) == 4:
                    fours += 1
                elif int(num) == 5:
                    fives += 1
                elif int(num) == 6:
                    sixes += 1
                elif int(num) == 7:
                    sevens += 1
                elif int(num) == 8:
                    eights += 1
                elif int(num) == 9:
                    nines += 1
        a_list = [zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights, nines]
    output = filename + "\n" + list_to_string(a_list)
    return output


def main():
    #print(slice([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 10, 2))
    #print(list_to_string(["a", "b", "c", "d"])) done
    #print(collatz(6))
    #print(count_digits("data/digits_100_bad.txt"))
    pass
          
if __name__ == "__main__":
    main()