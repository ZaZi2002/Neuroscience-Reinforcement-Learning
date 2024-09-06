import numpy as np

class MazeEnvironment:
    def __init__(self, dim = 100, maze_path = None):
        if maze_path == None:
            boost = np.random.randint(30, 50, [dim, dim]) * np.eye(dim)
            boost[0,0] = 0
            boost[dim-1, dim-1] = 100
    
            self.maze = np.random.randint(-10, 10, [dim, dim]) + boost
        else:
            self.maze = np.load(maze_path)
            
        self.x = 0
        self.y = 0
        self.dim = dim
        self.target = [dim-1, dim-1]
        self.done = False
        
    def reset(self):
        self.x = 0
        self.y = 0
        self.done = False
        return np.asarray([self.x, self.y], dtype=np.float32)
        
    def step(self, action):
        if self.done == True:
            self.reset()
            
        if action == 0:
            if self.y != 0:
                self.y -= 1
                reward = self.maze[self.x, self.y]
            else:
                reward = 0
        elif action == 1:
            if self.x != (self.dim-1):
                self.x += 1
                reward = self.maze[self.x, self.y]
            else:
                reward = 0
        elif action == 2:
            if self.y != (self.dim-1):
                self.y += 1
                reward = self.maze[self.x, self.y]
            else:
                reward = 0
        else:
            if self.x != 0:
                self.x -= 1
                reward = self.maze[self.x, self.y]
            else:
                reward = 0

        if (self.x == (self.dim-1)) and (self.y == (self.dim-1)):
            self.done = True

        return np.asarray([self.x, self.y], dtype=np.float32), reward, self.done

if __name__ == '__main__':
	env = MazeEnvironment(50, 'mazes/maze1.npy')