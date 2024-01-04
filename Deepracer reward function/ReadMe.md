# AWS DeepRacer reward functions

AWS DeepRacer is a fully autonomous 1/18th scale self driving race car driven by reinforcement learning. Users train their DeepRacer models in the AWS service environment and deployed onto the physical DeepRacer car to compete in races autonomously, learning how to navigate tracks efficiently while avoiding obstacles.

In 2022, I won the Deepracer competition (physical track) during the company's internal event and came 2nd in the Australia & New Zealand competition (virtual). This qualified me for the 2022 AWS Re:Invent DeepRacer World Championship, where I eventually placed 15th out of 50 participants. Below are the reward functions that I used during the competitions:

- **2022 Summit Speedway reward function:** Rewarding the car for following the most optimal racing line on the 2022 Summit Speedway track.

- **2022 Re:Invent reward function:** A simple function designed to reward the car for speed on the fast lane and for taking fewer steps on the 2022 Re:Invent track.

- **2022 Re:Invent Object Avoidance reward function:** Designed to avoid obstacles on the 2022 Re:Invent track. It grants a reward when the car approaches an object while positioned on a different lane. This function was crafted for the virtual environment and has not been tested on a physical track.

