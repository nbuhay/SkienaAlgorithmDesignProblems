# Problem: Movie Scheduling Problem
# Input:   A set I of n intervals on the line.
# Output:  What is the largest subset of mutually non-overlapping intervals which can be selected from I?

import random as Random;
I =[];

# compute the total time movie will take, append it to I
def computeMovieLength(I):
  for x in I:
    x.append(x[1]-x[0]);

# populate the empty list I with n movie data points.  
# Movies have a start and end time where start always occurs before end
# list element form:  [move_start, movie_end, delta_start_end]
def genMovieTimeline(I, n):
  I.clear();
  for i in range(0, n):
    start = int(Random.uniform(0,1) * 100);
    end = Random.randint(start, 100);
    I.append([start, end]);
  computeMovieLength(I);

# custom sort for movie data
# returns ascending sort of list
# usorted_list elements are of the form [move_start, movie_end, delta_start_end]
# sort_element is the index of unsorted_list on which to sort
def buhay_sort(unsorted_list, sort_element):
  sorted_list = [];
  sorted_list.append(unsorted_list.pop(0));
  for x in unsorted_list:
    i = 0;
    while(i < len(sorted_list) and x[sort_element] > sorted_list[i][sort_element]):
      i += 1;
    front = sorted_list[:i];
    back = sorted_list[i:];
    front.append(x);
    front.extend(back);
    sorted_list = front;
  unsorted_list.clear();  # remove original unsorted list elements
  unsorted_list.extend(sorted_list);  # copy sorted elements into original list object
  return sorted_list;

genMovieTimeline(I, 10);
print(I);