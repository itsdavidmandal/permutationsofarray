import itertools

def permutations(array):
  #To run the program, you can save it as a Python file and then run it from the command line

  if len(array) == 0:
    return []
  else:
    permutations_list = []
    for i in range(len(array)):
      new_array = array[:]
      new_array.remove(array[i])
      permutations_list.extend(permutations(new_array) + [[array[i]] + perm for perm in permutations(new_array)]) # The permutations() function works by recursively generating all possible permutations of the iterable. The first step is to remove one element from the iterable. This element is then placed at the end of all possible permutations of the remaining elements of the iterable. The second step is to repeat the first step for each of the remaining elements of the iterable.
    return permutations_list


def main():
  array = [1, 2, 3]
  print(permutations(array))


if __name__ == "__main__":
  main()
