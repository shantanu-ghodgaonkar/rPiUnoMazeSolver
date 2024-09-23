# Maze Solving Robot

## Project Overview

This project combines the capabilities of Raspberry Pi 4B and Arduino Uno microcontrollers to create an innovative **maze-solving robot**. Using **OpenCV** for image processing and implementing the **breadth-first search (BFS)** algorithm on the Raspberry Pi, the robot intelligently navigates a ball towards the maze’s exit. Servo motors controlled by the Arduino are employed to manipulate the ball's movement through complex mazes.

This project was completed as part of the **Final Project, Spring 2024** at the **New York University, Tandon School of Engineering**.

## Key Features

- **OpenCV for Image Processing**: Processes images to detect the ball's position and maze walls.
- **Breadth-First Search (BFS) Algorithm**: Used to find the optimal path through the maze.
- **Arduino Integration**: Controls servos to execute movements based on navigation commands from the Raspberry Pi.
- **Real-Time Maze Solving**: Continuously tracks the ball’s position and recalculates its path through the maze.

## Project Objectives

1. Develop a reliable ball detection algorithm using **OpenCV** to accurately identify the ball’s position and differentiate maze walls from the base.
2. Implement preprocessing techniques for maze detection.
3. Use contour detection to precisely locate the ball in the maze.
4. Employ the **BFS algorithm** to plan the optimal path through the maze.
5. Use Arduino-controlled servos to physically manipulate the ball based on commands from the Raspberry Pi.
6. Establish a communication protocol between the Raspberry Pi and Arduino for seamless data exchange.

## Key Components

- **Raspberry Pi 4 Model B (4GB)**: Handles image processing and path planning using BFS.
- **Raspberry Pi Camera Module v1.3**: Captures images of the maze for processing.
- **Arduino Uno**: Controls servo motors to manipulate the ball's movement.
- **MG996R Servo Motors**: Precisely control the ball's rotation across two axes.

## Image Processing and Object Detection

A series of image processing techniques are employed using OpenCV:
1. Image calibration and cropping to focus on the maze.
2. Color space conversion and masking to enhance ball detection.
3. Ball localization using the **Hough Circles Algorithm**.

## Breadth-First Search Algorithm

The maze is represented as a graph where each cell is a vertex and passages between cells are edges. The BFS algorithm is used to explore the maze and find the optimal path from the start to the exit.

## Integration of Arduino and Raspberry Pi

- The **Raspberry Pi** captures an image of the maze and processes it to determine the ball’s position and solution path.
- Based on the relative position of the ball, the Raspberry Pi sends movement instructions to the **Arduino**.
- The **Arduino** then controls the servos to manipulate the ball according to the instructions.

## Circuit Schematic

The project involves connecting the Raspberry Pi, Arduino, camera module, and servo motors. The circuit schematic is illustrated below:

![Circuit Schematic](https://github.com/shantanu-ghodgaonkar/rPiUnoMazeSolver/blob/e052fe15d5a39fba4fd2f3ebe7bfc404883de492/images/ckt_schematic.png)

## Results

The system successfully detects the ball and navigates it through the maze using the BFS algorithm. Below are the captured images showing different stages of the process:

<p align="center">
  <img src="https://github.com/shantanu-ghodgaonkar/rPiUnoMazeSolver/blob/e052fe15d5a39fba4fd2f3ebe7bfc404883de492/images/img_rpicam.png" alt="Image from RPi Camera" width="250"/>
  <img src="https://github.com/shantanu-ghodgaonkar/rPiUnoMazeSolver/blob/e052fe15d5a39fba4fd2f3ebe7bfc404883de492/images/ball_highlight.png" alt="Detected Ball" width="250"/>
  <img src="https://github.com/shantanu-ghodgaonkar/rPiUnoMazeSolver/blob/e052fe15d5a39fba4fd2f3ebe7bfc404883de492/images/solution_path.png" alt="Solution Path" width="250"/>
</p>

<p align="center">
  <b>Fig 1:</b> Image captured from RPi Camera &nbsp;&nbsp;
  <b>Fig 2:</b> Image highlighting the detected ball &nbsp;&nbsp;
  <b>Fig 3:</b> Solution path determined by the BFS algorithm
</p>

## Future Enhancements

- **Stewart Platform**: Integrating the robot with a Stewart platform (hexapod) and an improved camera could enhance dynamic positioning.
- **Optimization of Path-Planning Algorithms**: Further refinement of algorithms could allow the robot to adapt to dynamic maze patterns.
- **Machine Learning**: Integrating machine learning techniques could improve image processing and ball detection.

## License

This project currently does not have an associated license.

