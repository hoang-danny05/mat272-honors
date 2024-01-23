from manim import *

#requires that you activate the manim venv
#amimate with "manim render quickstart.py FirstScene"
class FirstScene(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=.5)
        # a certain animation
        self.play(Create(circle))
        self.play(FadeOut(circle))


class StandardPerceptron(Scene):
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
                "color": BLUE
            }
        }

        graph = DiGraph(
            vertices,
            edges,
            labels=True,
            layout="circular",
            vertex_config=vertex_config,
        )

        self.add(graph)
        self.play(Create(graph))
        self.play(
            graph["x_0"].animate.move_to([-2, -2, 0]),
            graph["x_1"].animate.move_to([-2, 0, 0]),
            graph["x_2"].animate.move_to([-2, 2, 0]),
            graph["out_0"].animate.move_to([2, 0, 0]),
        )
        self.wait()

    # def construct(self):
    #     TESTCOORD = [2, 2, 0]
    #     # the nodes needed for the actual animation
    #     output = Circle().shift(2 * LEFT)
    #     inputs = [Circle().shift(2 * RIGHT) for _ in range(3)]
    #     print(LEFT)

    #     output.set_fill(RED, opacity=.5)
    #     # output.show()
    #     self.add(output)
    #     for input in inputs:
    #         input.set_fill(BLUE, opacity=.5)
    #         # input.show()
    #         # input.next_to(output)
    #         self.add(input)

    #     inputs[0].shift(TESTCOORD)
    #     # inputs[0].shift(-2 * RIGHT)
    #     inputs[0].set_color(GREEN)
    

        
        