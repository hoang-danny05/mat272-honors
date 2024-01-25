from manim import *

#requires that you activate the manim venv
#amimate with "manim render quickstart.py FirstScene"
#more convenient "manim -pql quickstart.py <SceneName>"
class FirstScene(Scene):
    """standard scene used to learn manim"""
    def construct(self):
        #circle is created at the origin (the middle)
        circle = Circle()
        circle.set_fill(RED, opacity=.5)
        #moves the circle in the +x direction
        circle.set_coord(2, 0)
        #same as .set_x(realnum)
        #moves the circle in the +y direction
        circle.set_coord(2, 1)
        # for i in range(3):
            # print(circle.get_coord(i))
        # a certain animation
        self.play(Create(circle))
        self.play(circle.animate.move_to(ORIGIN))
        self.play(FadeOut(circle))

#the second scene
class StandardPerceptron(Scene):
    """
    A class that models the standard 3in -> 1out matrix 
    """
    def set_position(self, object: Mobject, pos):
        """
        A class for changing the coordinates of the object to pos's coordinates.
        """
        for index, value in enumerate(pos):
            object.set_coord(value, index)
        
    def construct(self):
        vertices = [f"x_{i}" for i in range(3)]
        vertices.append("out_0")
        edges = [
            ("x_0", "out_0"),
            ("x_1", "out_0"),
            ("x_2", "out_0"),
        ]

        vertex_config = {
            "radius": .5,
            "color": RED,
            "stroke_width": 10,
            # "fill_opacity": .5,
            "out_0": {
                "color": BLUE,
                "point" : [-10, -10, 0]
            }
        }

        graph = DiGraph(
            vertices,
            edges,
            labels=True,
            vertex_config=vertex_config,
        )

        self.set_position(graph["x_0"], [-2, -2, 0])
        self.set_position(graph["x_1"], [-2, 0, 0])
        self.set_position(graph["x_2"], [-2, 2, 0])
        self.set_position(graph["out_0"], [2, 0, 0])

        self.add(graph)
        self.play(Create(graph))
        self.wait()
        # self.play(FadeOut(graph["x_0"]))
        self.wait()

# another scene
class PerceptronTwoOutput(Scene):
    """
    class that shows us adding a new 
    """
    def set_position(self, object: Mobject, pos):
        """
        A class for changing the coordinates of the object to pos's coordinates.
        """
        for index, value in enumerate(pos):
            object.set_coord(value, index)
        
    def construct(self):
        vertices = [f"x_{i}" for i in range(3)]
        for i in range(2):
            vertices.append(f"out_{i}")
        print(vertices)
        edges = [
            ("x_0", "out_0"),
            ("x_1", "out_0"),
            ("x_2", "out_0"),
        ]

        other_edges = [
            ("x_0", "out_1"),
            ("x_1", "out_1"),
            ("x_2", "out_1"),
        ]
        edges = edges + other_edges
        
        vertex_config = {
            "radius": .5,
            "color": RED,
            "stroke_width": 10,
            # "fill_opacity": .5,
            "out_0": {
                "color": BLUE,
            },
            "out_1": {
                "color": BLUE,
            },
        }

        lt = {
            "out_0": [2, -1, 0],
            "out_1": [2, 1, 0],
        }

        for i in range(3):
            lt[f"x_{i}"] = [-2, i*2 - 2, 0]

        graph = DiGraph(
            vertices,
            edges,
            labels=True,
            vertex_config=vertex_config,
            layout=lt
        )

        #use layout
        # self.set_position(graph["x_0"], [-2, -2, 0])
        # self.set_position(graph["x_1"], [-2, 0, 0])
        # self.set_position(graph["x_2"], [-2, 2, 0])
        # self.set_position(graph["out_0"], [2, -1, 0])
        # self.set_position(graph["out_1"], [2, 1, 0])

        self.add(graph)
        self.play(Create(graph))
        self.wait()
        # graph.add_vertices("out_1", labels=True, vertex_config=output_v_config)
        # print(graph["out_1"]) # => Labeled Dot
        #graph.add_edges("x_0", "x_1")
        # self.play(FadeIn(graph["out_1"]))
        self.play(graph.animate)
        self.wait()