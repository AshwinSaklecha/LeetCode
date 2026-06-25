class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        mass = mass
        for i in range(len(asteroids)):
            if asteroids[i] <= mass:
                mass += asteroids[i]
            else:
                return False
        return True