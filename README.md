# [Probability Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

You can run this [here](https://replit.com/@malikmmusa/boilerplate-probability-calculator#main.py)

This program determines the approximate probability of drawing certain balls randomly from a hat

Example usage:
<pre>
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
# Returns: Probability: 0.17066666666666666
</pre>
