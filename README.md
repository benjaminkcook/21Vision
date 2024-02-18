# 21 Vision

# Motivation

This project is done by Ben Cook, Long Nguyen, Malcolm Saltzman, and Viet Ninh during the Spring 2024 Cornhacks. We wanted to create something
that uses object detection so we looked towards the yolo (you only look once) model to detect playing cards and
use that information to analyze whether we should hit or stand, which is down through a metric called Running Count.
This project uses a dataset from roboflow universe. The model was trained on a GTX 3060 with 100 epochs. The link to the dataset can be found here: https://universe.roboflow.com/augmented-startups/playing-cards-ow27d

# Setup

Run pip install on the requirements.txt file. Command listed below
`pip install -r requirements.txt`

# Running the project
There are 3 files that are within the object detection folder. `real_time_capture.py`, `screenshot_capture.py`, and `yolo_capture.py`. <br>
To run the project, the main file to run is real_time_capture.py, and make sure that this is running at the root directory of the project. This allows it to call the correct model when you initally look at our code.

# Methodologies

Running Count is a method for counting cards in blackjack. A positive card count is when you want to make some risks and a negative card count is when you want to play safe. The further along you get into a game the more useful this counting factor is. We decided this would be a good way to "Beat the odds" at blackjack and implemented it into our program. More information can be found here: https://wizardofodds.com/games/blackjack/card-counting/high-low/
