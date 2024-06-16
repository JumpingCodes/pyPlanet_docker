### README.md

# pyPlanet Simulator

This project is a simple planetary orbit simulator originally written in Python using Pygame, but now rewritten in JavaScript for the web. The simulation runs in an HTML5 canvas and displays the orbits of several planets around the sun.

## Features
- Simulates the orbits of Earth, Mars, Mercury, and Venus around the Sun.
- Uses basic physics equations to calculate gravitational forces and planetary motions.
- Visualizes the orbits and positions of the planets.

## Prerequisites
- Docker: Make sure Docker is installed on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

## Installation and Setup

### Step 1: Clone the Repository
First, clone the repository to your local machine using git:
```sh
git clone https://github.com/JumpingCodes/pyPlanet_Docker.git
cd jsPlanetSimulator
```

### Step 2: Create the Docker Image
Next, you need to build the Docker image using the provided `Dockerfile`.
```sh
docker build -t pyPlanet_Docker .
```

### Step 3: Run the Docker Container
After building the image, you can run the container with the following command:
```sh
docker run -d -p 8080:80 pyPlanet_Docker
```
This will start an Nginx server hosting the jsPlanet simulation on port 8080.

### Step 4: Access the Simulation
Open your web browser and navigate to:
```
http://localhost:8080
```
You should see the planetary orbit simulation running.

## Project Structure
- `index.html`: The main HTML file containing the JavaScript code for the simulation.
- `Dockerfile`: Dockerfile to build the Docker image and set up the Nginx server.

## Dockerfile Contents
The Dockerfile is straightforward, using the Nginx base image to serve the `index.html` file.

```dockerfile
FROM nginx
COPY web/index.html /usr/share/nginx/html
```

## Notes
- Make sure that the path to `index.html` in the Dockerfile matches the actual path in your project directory structure.
- The simulation runs best in modern web browsers that support HTML5 and the Canvas API.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact
For any questions or inquiries, please open an issue on the repository or contact the author at [baier.hendrik@proton.me].

Enjoy simulating planets!

---
