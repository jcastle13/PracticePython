
print("List Remove Duplicates")

def list_remove_dup_set(orig_list):
    result = []

    result = list(set(orig_list))

    return result


def list_remove_dup_loop(orig_list):
    result = []

    for i in orig_list:
        if i not in result:
            result.append(i)

    return result





temp_list = [23, 4, 5, 5, 1, 2, 33, 4, 5]

print("temp_list:", temp_list)

update_list = list_remove_dup_set(temp_list)

print("update list through set:", update_list)

update_list02 = list_remove_dup_loop(temp_list)

print("update list through loop:", update_list02)

