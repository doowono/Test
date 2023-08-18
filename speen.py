import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

cubeVertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))

pyramidVertices = ((-1, -1, -1), (1, -1, -1), (0, 1, 0), (0, -1, 1))

dodecahedronVertices = (
    (-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1),
    (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1),
    (0, -1.618, -1.618), (-1.618, -1.618, 0), (-1.618, 0, -1.618),
    (0, -1.618, 1.618), (-1.618, 1.618, 0), (1.618, 0, -1.618),
    (0, 1.618, -1.618), (1.618, -1.618, 0), (-1.618, 0, 1.618),
    (0, 1.618, 1.618), (1.618, 1.618, 0), (1.618, 0, 1.618)
)

triangularPrismVertices = ((1, -1, -1), (0, 1, -1), (-1, -1, -1), (1, -1, 1), (0, 1, 1), (-1, -1, 1))

cubeEdges = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))

pyramidEdges = ((0, 1), (1, 2), (2, 0), (3, 0), (3, 1), (3, 2))

dodecahedronEdges = (
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),  # Face 1
    (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),  # Face 2
    (10, 11), (11, 12), (12, 13), (13, 14), (14, 10),  # Face 3
    (15, 16), (16, 17), (17, 18), (18, 19), (19, 15),  # Face 4
    (0, 5), (1, 16), (2, 11), (3, 6), (4, 10),  # Face 5
    (7, 17), (8, 12), (9, 18), (13, 19), (14, 15)  # Face 6
)

triangularPrismEdges = ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4), (2, 5))

shapes = {
    'pyramid': (pyramidVertices, pyramidEdges),
    'cube': (cubeVertices, cubeEdges),
    'dodecahedron': (dodecahedronVertices, dodecahedronEdges),
    'triangular_prism': (triangularPrismVertices, triangularPrismEdges),
}

current_shape = 'cube'

def Shape(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    global current_shape
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_shape = 'pyramid'
                elif event.key == pygame.K_2:
                    current_shape = 'cube'
                elif event.key == pygame.K_3:
                    current_shape = 'dodecahedron'
                elif event.key == pygame.K_4:
                    current_shape = 'triangular_prism'

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Shape(*shapes[current_shape])
        pygame.display.flip()
        pygame.time.wait(10)

main()
