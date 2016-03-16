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

def schedule_shortest(list):
  final_list=[];
  final_list.append(list.pop(0));
  for movie in list:
    for scheduled_movie in final_list:
      if((scheduled_movie[0] < movie[1] and scheduled_movie[0] > movie[0]) or 
        (movie[0] < scheduled_movie[0] and movie[1] < scheduled_movie[1]) or 
        (scheduled_movie[1] > movie[0] and scheduled_movie[1] < movie[1])):
          list.pop(movie);
      else:
        final_list.append(movie);
  return final_list;

# generate data
genMovieTimeline(I, NUM_MOVIES);

# sort by earliest start day for filming
earliest_start=buhay_sort(I, 0);

# sort by time it will take to complete a movie
shortest_time=buhay_sort(I, 2);
