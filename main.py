# Create a Python code that:
# Takes 4 populations, and assigns them either fast aging or slow aging.
# It then looks at all the possible combinations of the four populations,
# without repeating itself. If a fast aging and a fast aging are compared,
# it should return a certain value, such as 'same'. If a fast aging is
# compared to a slow aging, it should return a value such as 'different'.
import random




def compare_groups(group1, group2):
    if group1 == group2:
        return True
    else:
        return False


# function that takes in the length of the group's dictionary, and looks at the values associated with each
# changing key per iteration
# To make things understandable, it prints each comparison depending on if compare_groups is True or False.
def compare_mult_groups(groups):
    num_groups = len(groups)
    for i in range(1, num_groups):
        for j in range(i):
            group1 = list(groups.keys())[i]  # Assigns group key for ith element of groups,
            group2 = list(groups.keys())[j]
            if compare_groups(groups[group1], groups[group2]):
                print(f"{group1} vs {group2}: Same")
            else:
                print(f'{group1} vs {group2}: Different')


# Function is primarily for testing. Based on the number in amt_of_groups, function randomly assigns each group as fast
# or slow, and saves the format in the groups variable.
def fake_pairing(amt_of_groups):
    groups = {}
    for i in range(amt_of_groups):  # this function creates my dictionary
        group_data = random.choice(["fast", "slow"])
        group_name = f"Group {i+1}"  # this is why we have group 1,2,3,4
        groups[group_name] = group_data  # actually assigns the value to each key
    return groups


compare_mult_groups(fake_pairing(4))
