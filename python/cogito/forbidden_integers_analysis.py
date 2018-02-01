# I use merge sort, in order to perform better then O(n*n) even in the worst case
# Initially, I was thinking about the quick sort, but it is O(n*n) in worst case
# and the merge sort is O(n*log(n)) in best, average and worst cases

# total_number_of_forbidden_integers according to the file is 10,591,507,799
# it means that there ARE overlappings
# max integer = 4,294,967,295

# Final result: (first_allowed_number=31053880, total_allowed_numbers=116)


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def check_two_ranges(range1,range2):
    res1 = [range1[0],range1[1]]
    res2 = [range2[0],range2[1]]
    if range2[0]==range1[1]+1:
        res1[1] = res2[1]
        return res1, None
    if range1[1]<range2[0]:
        return res1,res2
    if range2[0]<=range1[1] and range2[1]<=range1[1]:
        return res1,None
    if range2[0]<=range1[1] and range2[1]>=range1[1]:
        res1[1]=res2[1]
        return res1,None


def analyze_forbidden_integers(range_min,range_max,forbidden_lists):
    smallest_allowed_integer = range_min-1 # it will remain with this value, if there are no allowed numbers at all
    total_number_of_allowed_integers = 0

    # sort the forbidden list by the first number in each pair
    # the number before the first forbidden range, which is above the range_min
    # will give us the smallest allowed number
    firsts_seconds_map = {}
    for pair in forbidden_lists:
        firsts_seconds_map[pair[0]] = pair[1]

    print(firsts_seconds_map)

    firsts = list(map(lambda p: p[0], forbidden_lists))
    print(firsts)
    mergeSort(firsts)
    print(firsts)
    print(firsts_seconds_map[0])

    # build a new, non-overlapping list of forbiddens
    ranges = []
    for first in firsts:
        ranges.append([first,firsts_seconds_map[first]])

    new_forbidden_list = []
    if len(ranges)>0:
        range = ranges[0]
        new_forbidden_list.append([range[0],range[1]])
        ranges.remove(range)

    while len(ranges)>1:
        first = new_forbidden_list[len(new_forbidden_list)-1]
        second = ranges[0]
        range1, range2 = check_two_ranges(first,second)
        if not range2:
            first[0] = range1[0]
            first[1] = range1[1]
        if range2:
            new_forbidden_list.append([range2[0],range2[1]])
        ranges.remove(second)

    print(new_forbidden_list)
    print(len(new_forbidden_list))

    smallest_allowed_integer = new_forbidden_list[0][0]
    if smallest_allowed_integer==range_min:
        smallest_allowed_integer = new_forbidden_list[0][1]+1
    if smallest_allowed_integer>range_max:
        smallest_allowed_integer = range_min-1

    total_number_of_forbidden_numbers = 0
    for range in new_forbidden_list:
        total_number_of_forbidden_numbers += range[1]-range[0]+1

    total_number_of_allowed_integers = range_max-range_min-total_number_of_forbidden_numbers

    return smallest_allowed_integer,total_number_of_allowed_integers

if __name__ == '__main__':
    forbidden_lists_file = open('forbidden_integers.txt')
    lines = forbidden_lists_file.readlines()
    print(len(lines))
    lists = []
    for line in lines:
        numbers = line.split('-')
        pair = [int(numbers[0]),int(numbers[1].strip('\n'))]
        lists.append(pair)

    print(len(lists))
    print(lists)
    print(analyze_forbidden_integers(range_min=0,range_max=4294967295,forbidden_lists=lists))

    '''
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)
    '''