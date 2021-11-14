# Insertion Sort


- Reverse this array using insertion sort:

```python
[8,4,23,42,16,15]
```

![insertion_sort_1](whiteboard_process/insertion-sort-1.png)

### Steps:

First, we split the array into 2 parts, the sorted and unsorted arrays and then we compare the first element with the second, if the second element is less than the first element, we replace the first element with the second element, otherwise we are going to assume that its bigger and so move on.

![insertion_sort_1](whiteboard_process/insertion-sort-2.png)

The third array element is already bigger than its previos element so we will ignore that and move on.

![insertion_sort_1](whiteboard_process/insertion-sort-3.png)

Same for the next element, its already bigger.

![insertion_sort_1](whiteboard_process/insertion-sort-4.png)

Now the next element on the list is less than its previous element, so we are going to replace that element with its previous.

![insertion_sort_1](whiteboard_process/insertion-sort-5.png)

We still have the same thing, the previous element is bigger so we will justs replace that aswell

![insertion_sort_1](whiteboard_process/insertion-sort-6.png)

Now thats sorted, we will move on to the next element, but it also appears thats it less than its previous element so we will repeat the same steps

![insertion_sort_1](whiteboard_process/insertion-sort-7.png)

![insertion_sort_1](whiteboard_process/insertion-sort-8.png)

![insertion_sort_1](whiteboard_process/insertion-sort-9.png)


Finally, we got a sorted array that matches our expected outcome;

![insertion_sort_1](whiteboard_process/insertion-sort-10.png)


### Big O

Time = O(n^2)

Space = O(1)
