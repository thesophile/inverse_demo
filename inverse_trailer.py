

from manim import *

class LT(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            background_plane_kwargs={"x_range": [-10,10,1],"y_range": [-10,10,1]},
            *kwargs
        )

    def construct(self):
        
        self.camera.frame_center = [2, 2, 0] 

        matrix1 = [[2, 1], [3, 4]]
        matrix2 = [[1, -1/4], [-3/2, 1]]
        matrix3 = [[4, 0], [0, 2]]
        matrix4 = [[1/5, 0], [0, 1/5]]
        
        equation1 = MathTex(r"Matrix A",color=YELLOW).shift(UP * 3 + RIGHT * 3)
        equation2 = MathTex(r"adj(A)",color=YELLOW).shift(UP * 3 + RIGHT * 3)
        equation3 = MathTex(r"\frac{1}{det(A)}",color=YELLOW).shift(UP * 3 + RIGHT * 3)
        
        self.play(Write(equation1))
        
        self.apply_matrix(matrix1)
        self.wait(0)
        self.moving_mobjects = []
        
        self.play(Transform(equation1, equation2))
        self.moving_mobjects = []
        
        self.apply_matrix(matrix2)
        self.wait(0)
        self.moving_mobjects = []
        
        self.apply_matrix(matrix3)
        self.wait(0)
        self.moving_mobjects = []
        
        self.play(Transform(equation1, equation3))
        self.moving_mobjects = []
        
        self.apply_matrix(matrix4)
        self.wait(0)
        self.moving_mobjects = []
        
