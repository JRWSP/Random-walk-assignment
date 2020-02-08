# randomwalk_the1

Computational simulation for 1-D classical random walk. The walker's position is determined by tossing a coin; a walker move to the left for tail outcome and vice versa. The coin is sampling from the uniform probability distribution.


From the theoretical derivation, a walker average position should keep stay at the initial position as the walkstep increases. On the other hand, its variance among individual trajectories will proportional to a square root of walksteps. These results were shown in the figures below. 

Here we run the code to simulate the random walk process up to 400 walksteps. 1000 realizations of random walk were plotted in order to demonstrade how our code works.  

![RANDOM](/RANDOM.png)

The mean position among all trajectories is 3.062 ≈ 0 which is very small compared to its fluctuation.
![AVG](/avg.png)

Finally we calculate its (average) variance and show that our result well-fitted to the square root of walksteps.
![VAR](/var.png)
