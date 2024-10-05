from manim import *

class Vectors(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        self.section1()
        self.next_section(skip_animations=False)
        self.section2()

    def section1(self):
        intro = Tex(
            r"\centering \section*{1.~Co je to vektor?}"
        ) 
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))

        axes = NumberPlane(
            x_range=[-6, 6,1],  # Range for x-axis (Only second and third quadrants)
            y_range=[-6, 6,1],   # Range for y-axis
            x_length=config.frame_width,
            y_length=config.frame_height,
            background_line_style={
                "stroke_color": BLUE,   # Color of the grid lines
                "stroke_width": 1.5,    # Thickness of the grid lines
                "stroke_opacity": 0.5   # Opacity of the grid lines
            },
            axis_config={"color": WHITE, "stroke_width": 2},  # Customize axis appearance
            faded_line_ratio=2  # To make the lines less dominant
        )

        # Shift grid and axes to the left to make space for text on the right
        axes.shift(LEFT * 2)

        
        # Add thin grid lines
        axes.add_coordinates()
        axes.get_lines_to_point([0, 0,0])  # Add lines through the origin

        # Shift axes to the right to leave space for text
        axes.shift(RIGHT * 2)

        # Add some text to the left side
        def1 = Tex(r"Vektor je dvojice čísel\\nakresleme si ho tedy\\ jako bod v rovině.")
        def1.move_to(LEFT*3.5+UP*2.5)  # Position the text on the left side

        # Add everything to the scene

        self.play(FadeIn(axes))
        self.play(Write(def1))

        dot = Dot(axes.c2p(2,3))
        dot_label = Tex(r"(2,3)").next_to(dot,UP)

        self.play(FadeIn(dot),Write(dot_label))
        

        def2 = Tex(r"Do tohoto bodu udělejme \\ šipku z počátku souřadnic.\\Šipka tedy indikuje vektor.").move_to(LEFT*3.5+DOWN*2)
        self.play(Write(def2))

        vector = Vector(axes.c2p(2,3),color=RED_D)
        self.play(FadeIn(vector))

        znaceni = MathTex(r"(2,3)=\vec{v}").move_to(dot_label).shift(LEFT*0.3)
        znaceni[0][6:8].set_color(RED_D)
        self.play(TransformMatchingTex(dot_label,znaceni))
        

        self.play(FadeOut(def1,def2,znaceni,dot))

        velikost = Tex(r"Co nás u vektorů bude\\ zajímat je například\\ jejich délka.").move_to(LEFT*3.5+UP*2.5)

        general = Vector(axes.c2p(4,4),color=RED_D)
        self.play(Transform(vector,general))
        obecne= MathTex(r"\vec{v}=(x,y)").next_to(general,UP).shift(RIGHT)
        obecne[0][0:2].set_color(RED_D)

        self.play(Write(obecne))

        self.play(Write(velikost))

        delka = Tex(r"Délku vektoru značíme $\|\vec{v}\|$\\ a z pytágorovi věty\\ spočítáme jako:").move_to(LEFT*3.5+DOWN*2)
        delka[0][23:25].set_color(RED_D)
        vzorec = MathTex(r"\|\vec{v}\| = \sqrt{x^2 + y^2}").next_to(delka,RIGHT).shift(RIGHT*2)
        vzorec[0][1:3].set_color(RED_D)

        vzorec[0][7:9].set_color(YELLOW)
        vzorec[0][10:14].set_color(YELLOW)

        self.play(Write(delka),Write(vzorec))

        x = DashedLine(axes.c2p(4,4),axes.c2p(4,0),color=YELLOW)
        x_lab = MathTex(r"y",color=YELLOW).next_to(x.get_last_handle(),RIGHT).shift(UP)
        y = DashedLine(axes.c2p(4,4),axes.c2p(0,4),color=YELLOW)
        y_lab = MathTex(r"x",color=YELLOW).next_to(y.get_last_handle(),UP).shift(RIGHT)

        self.play(Write(x),Write(y))
        self.play(Write(x_lab),Write(y_lab))

        self.play(FadeOut(x,y,y_lab,x_lab,delka,velikost,vzorec))


    def section2(self):
        intro = Tex(
            r"\centering \section*{2.~Sčítání vektorů a násobení skalárem.}"
        ) 
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))