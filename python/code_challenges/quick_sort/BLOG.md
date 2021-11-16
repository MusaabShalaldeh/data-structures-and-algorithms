# Quick Sort

- Input array and the expected output.

![whiteboard_img](whiteboard_process/quick-sort-1.png)

- We first mark the pivot which in our case is the right element.

![whiteboard_img](whiteboard_process/quick-sort-2.png)

- The first two elements are compared with the pivot and they are swapped with them selves if the right condtion is met.

![whiteboard_img](whiteboard_process/quick-sort-3.png)

- The next 2 elements are greater than the pivot so they remain where they aee.

![whiteboard_img](whiteboard_process/quick-sort-4.png)

- The 16 is smaller than the last element is its replaced with the lowest available element.

![whiteboard_img](whiteboard_process/quick-sort-5.png)

- Finally, we reach the pivot, since its less than the previous element, we move it to the right postion.

![whiteboard_img](whiteboard_process/quick-sort-6.png)

- Final Output

![whiteboard_img](whiteboard_process/quick-sort-7.png)




# Big O

- Time = O(log n)

- Space = O(log n)
