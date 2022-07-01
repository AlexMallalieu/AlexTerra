
def sort_name():
    companies = [{'name': 'Terra"'}, {'name': 'Scotiabank'}, {'name': 'Sol'}, {'name': 'First Caribbean'} ]
    companies.sort(key = lambda x: x['name'])

    print(companies)

def filter_even_odd():
    num = [1,2,3,4,5,6,7,8,9,10]
    print("Original bumbers: ", num)

    even_num = list(filter(lambda x: x%2 == 0, num))
    print("Even Numbers: ", even_num)

    odd_num = list(filter(lambda x: x%2 != 0, num))
    print("Odd numbers: ", odd_num)

def square_num():
    num = [1,2,3,4,5,6,7,8,9,10]
    print("Original Numbers: ", num)

    result_num_square = list(map(lambda x: x**2,num))
    print(result_num_square)

    result_num_cube = list(map(lambda x: x**3, num))
    print(result_num_cube)

def character_check():
    starts_with = lambda x: True if x.startswith('P') else False
    print(starts_with('Python'))
    print(starts_with('Java'))

def function():
    print("What function would you like to use? (type 'more' to see a full list of available functions)")
    ans = input(print('>>>'))
    if ans == 'more':
        print("character check    sort by name    square numbers    filter odd and even")
        print("")
        function()
    if ans == 'square numbers':
        square_num()
    if ans == 'character check':
        character_check()
    if ans == 'filter odd and even':
        filter_even_odd()
    if ans == 'sort by name':
        sort_name()
    else:
        print("Not a valid option. Please try again")
        function()


function()


