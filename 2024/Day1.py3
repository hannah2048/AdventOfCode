
def reader(filename='locationIDs.txt'):
    ''' reads in location IDs file'''
    with open(filename) as file:
        return file.readlines()

def parse():
    ''' parses file into two lists '''
    file = reader()
    left_list,right_list = [],[]

    for i in range(len(file)):
        file[i] = file[i].strip('\n')

        left,right = file[i].split("   ")

        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    return left_list,right_list


def part_one():
    ''' find the difference score between two lists by summing absolute value of differences'''
    left_list,right_list = parse()

    difference_score = sum([abs(left_list[i]-right_list[i]) for i in range(len(left_list))])

    print(difference_score)
    return difference_score

def part_two():
    ''' find similarity score between two lists by summing up the # occurences of an item in the other list times by the items value'''

    left_list,right_list = parse()
    
    similarity_score = 0
    for i in range(len(left_list)):
        cur = left_list[i]
        similarity_score += right_list.count(cur) * cur

    print(similarity_score)
    return similarity_score

part_one()
part_two()

