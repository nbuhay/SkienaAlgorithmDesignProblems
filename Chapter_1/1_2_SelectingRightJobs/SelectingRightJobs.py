# Problem: Movie Scheduling Problem
# Input:   A set I of n intervals on the line.
# Output:  What is the largest subset of mutually non-overlapping intervals which can be selected from I?

import random as Random;
I=[];
NUM_MOVIES=10;
END_TIME=100;   # max length of movie schedule timeline

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
    start = int(Random.uniform(0,1) * END_TIME);
    end = Random.randint(start, END_TIME);
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

# use to schedule movies based on their start date
# earliest are selected and selections are made so there is no conflict
def schedule_earliest(list):
  cntr=0;
  final_list=[];
  final_list.append(list.pop(0));
  for movie in list:
    if(movie[0] > final_list[cntr][1]): # does this movie start after one already booked?
      final_list.append(movie); # yes it does, schedule this movie
      cntr+=1; # move counter ahead so we now compare using the above scheduled movie
  return final_list;

# select films that take the least time to complete and do not overlap
def schedule_shortest(list):
  final_list=[];
  final_list.append(list.pop(0));
  for movie in list:
    cntr=0;
    flag = True;
    while (cntr < len(final_list)):
      if(not(movie[0] < final_list[cntr][0] and movie[1] > final_list[cntr][0]) and
         not(movie[0] < final_list[cntr][0] and movie[1] > final_list[cntr][1]) and
         not(movie[0] < final_list[cntr][1] and movie[1] > final_list[cntr][1]) and 
         not(movie[0] == final_list[cntr][0] and movie[1] == final_list[cntr][1])):
        pass # does not conflict with this scheduled movie
      else:
        flag = False; # conflicts with this scheduled movie
      cntr+=1;
    if(flag): # if no conflicts existed with any scheduled movie, schedule this movie
      final_list.append(movie);
  return final_list;

# find median value in the list
def median_movie_length(list):
  middle_index = len(list)/2;
  if(len(list) % 2 == 0): # even
    median = (list[middle_index] + list[middle_index-1]) / 2;
  else: # odd
    median = list[middle_index];
  return median

# generate data
genMovieTimeline(I, NUM_MOVIES);

# sort by earliest start day for filming
earliest_start=buhay_sort(I, 0);

# sort by time it will take to complete a movie
shortest_time=buhay_sort(I, 2);
