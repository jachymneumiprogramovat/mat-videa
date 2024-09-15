from manim import *


class Functions(Scene):
    def construct(self):
        napis = Tex("Jejich grafy jsou:").shift(UP * 3.5, LEFT * 0.1)
        self.play(FadeIn(napis))

        ax = Axes(x_range=[-2, 4], y_range=[-3, 6]).add_coordinates()

        c = ValueTracker(0)

        first = ax.plot(lambda x: 5 * x - 3, x_range=[-0.3, 2], color=BLUE_D)
        label1 = (
            MathTex(r"f(x):y=5x-3", color=BLUE_D).next_to(first, DOWN, buff=-2)
        ).shift(RIGHT * 0.7)

        second = ax.plot(lambda x: -3 * x + 5, x_range=[-0.3, 3.5], color=GREEN_D)
        label2 = (
            MathTex(r"g(x):y=-3x+5", color=GREEN_D).next_to(second, RIGHT, buff=-3.6)
        ).shift(UP * 0.2)

        third = ax.plot(
            lambda x: 2 * x + c.get_value(), x_range=[-1.5, 3.5], color=RED_D
        )
        third.add_updater(
            lambda mob: mob.become(
                ax.plot(lambda x: 2 * x + c.get_value(), color=RED_D)
            )
        )
        label3 = MathTex(f"h(x):y=2x+{c.get_value()}", color=RED_D).next_to(
            third, RIGHT, buff=-4
        )

        def label3_updater(mob):
            if c.get_value() > 0:
                mob.become(
                    MathTex(
                        f"h(x):y=2x+{np.round(c.get_value(),decimals=2)}", color=RED_D
                    )
                )
            else:
                mob.become(
                    MathTex(
                        f"h(x):y=2x{np.round(c.get_value(),decimals=2)}", color=RED_D
                    )
                )
            mob.next_to(third, RIGHT, buff=-5)

        dot_axes = Dot(ax.coords_to_point(1, 2), color=YELLOW)
        lines = ax.get_lines_to_point(ax.c2p(1, 2))

        self.play(Write(ax))
        self.play(Write(first), Write(label1))
        self.play(Write(second), Write(label2))
        self.play(Write(third), Write(label3))
        self.wait(2)

        reseni = Tex(r"Řešením je $x$\\ takové, že\\ $f(x)=g(x)=h(x)$.").shift(
            UP * 1, LEFT * 4.7
        )
        reseni[0][24:28].set_color(BLUE_D)
        reseni[0][29:33].set_color(GREEN_D)
        reseni[0][34:38].set_color(RED_D)
        self.wait(2)
        self.play(Write(reseni))
        self.wait(4)

        self.play(Write(dot_axes), Write(lines))

        prusecik = Tex(r"Musíme tedy\\najít průsečík\\těchto tří funkcí.").shift(
            UP * 1, LEFT * 4.6
        )
        self.play(FadeOut(reseni, shift=UP * 0.5))
        self.play(FadeIn(prusecik, shift=UP * 0.5))
        self.play(FocusOn(dot_axes))
        self.wait(4)

        overte = Tex(r"V tomto případě\\ je řešením $x=1$.\\ Řešení ověřte!").shift(
            UP * 1, LEFT * 4.6
        )
        self.play(FadeOut(prusecik, shift=UP * 0.5))
        self.play(FadeIn(overte), shift=UP * 0.5)
        self.wait(4)
        self.play(FadeOut(overte))

        label3.add_updater(label3_updater)
        self.play(c.animate.set_value(2))
        self.play(c.animate.set_value(-1))
        self.play(c.animate.set_value(-0.5))

        neresitelnost = Tex(
            r"Jestliže neexistuje\\ jeden průsečík,\\ neexistuje ani řešení."
        ).shift(UP * 1, LEFT * 4.7)
        self.play(FadeIn(neresitelnost, shift=UP * 0.5))
        self.wait(2)

        self.play(FadeOut(dot_axes), FadeOut(lines))


class EquationSystem(Scene):
    def construct(self):
        intro = Tex(
            r"\centering \section{Grafické řešení soustavy\\ lineárních rovnic}"
        )
        self.play(Write(intro))
        self.wait()
        self.play(FadeOut(intro))

        problem = Tex("Řešme soustavu:").shift(UP * 2)

        rimske = VGroup(
            Tex("I.", color=BLUE_D).shift(UP),
            Tex("II.", color=GREEN_D).shift(UP * 0.3),
            Tex("III.", color=RED_D).shift(DOWN * 0.4),
        )
        rimske = rimske.shift(LEFT * 1.7)

        funkce = VGroup(
            MathTex("f(x):", color=BLUE_D).shift(UP),
            MathTex("g(x):", color=GREEN_D).shift(UP * 0.3),
            MathTex("h(x):", color=RED_D).shift(DOWN * 0.4),
        )
        funkce = funkce.shift(LEFT * 2.1)

        jedna = (MathTex("y=5x-3", color=BLUE_D)).shift(UP)
        dva = MathTex("y=-3x+5", color=GREEN_D)
        tri = (MathTex("y=2x", color=RED_D)).shift(DOWN)

        soustava = VGroup(jedna, dva, tri)
        soustava.arrange(DOWN, center=False, aligned_edge=LEFT)
        # rimske.arrange(DOWN, center=False, aligned_edge=LEFT)
        # funkce.arrange(DOWN, center=False, aligned_edge=LEFT)

        self.play(Write(problem))
        self.play(Write(rimske), Write(soustava))
        self.wait(2)
        reseni = Tex("Každá lineární rovnice definuje lineární funkci:").shift(UP * 2)

        self.play(FadeOut(problem, shift=UP * 0.5))
        self.play(FadeIn(reseni, shift=UP * 0.5))
        self.wait()
        self.play(Transform(rimske, funkce))

        bottom_text = Tex("Tyto funkce můžeme graficky znázornit.").shift(DOWN * 1.7)
        self.play(FadeIn(bottom_text, shift=UP * 0.5))
        self.wait(2)

    def func1(x):
        return -3 * x + 5

    def func2(x):
        return 5 * x - 5

    def func3(x):
        return 2 * x + 0.5


class Inequalities(Scene):

    def fronting(self, list):
        for vgroup in list:
            for group in vgroup:
                try:
                    group
                except:
                    pass

    def label_area(self, axes, pos, label):
        frame = SurroundingRectangle(
            label, color=WHITE, fill_color=BLACK, fill_opacity=1
        )

        group = VGroup(frame, label)
        group.set_z_index(5)
        label.set_z_index(10)
        group.move_to(axes.coords_to_point(*pos))
        self.play(
            AnimationGroup(DrawBorderThenFill(frame), Write(label), lag_ratio=0.6)
        )
        return group

    def highlight_area(self, axes, graph, x_min, x_max, color, below=False):
        if below:
            bound = axes.plot(lambda x: -3.1)
            area = axes.get_area(
                bound,
                x_range=[x_min, x_max],
                bounded_graph=graph,
                color=color,
                opacity=0.2,
            )
        else:
            bound = axes.plot(lambda x: 5)
            area = axes.get_area(
                graph,
                x_range=[x_min, x_max],
                bounded_graph=bound,
                color=color,
                opacity=0.2,
            )
        self.play(FadeIn(area))
        self.wait(1)


    def construct(self):
        #   intro = Tex(r"\centering \section{Grafické řešení soustavy\\ lineárních nerovnic",substrings_to_isolate="ne")
        #   intro.set_color_by_tex("ne",RED)
        #   self.play(Write(intro))
        #   self.wait()

        intro = Tex(
            r"\centering \section*{2.~Grafické řešení soustavy\\ lineárních nerovnic}"
        )
        self.play(Write(intro))
        frame = SurroundingRectangle(
            intro[0][38:40],
            buff=0.1,
            color=YELLOW,
        )

        self.play(intro[0][39:41].animate.set_color(RED))
        self.wait(2)
        self.play(FadeOut(intro))

        axes = Axes(x_range=[-2, 4], y_range=[-3, 6]).add_coordinates()
        obrys = SurroundingRectangle(axes, color=WHITE, buff=-0.1)

        self.add(axes)

        first = axes.plot(lambda x: 5 * x - 3, x_range=[0, 1.75], color=BLUE_D)
        second = axes.plot(lambda x: -3 * x + 5, x_range=[-0.3, 2.7], color=GREEN_D)
        third = axes.plot(lambda x: 2 * x - 0.5, x_range=[-1.35, 3.1], color=RED_D)

        self.play(Create(first), Create(second), Create(third))

        label3 = self.label_area(
            axes, (2.55, 3), MathTex("h(x):y", "{=}", "2x-0.5", color=RED_D)
        )
        label2 = self.label_area(
            axes, (2.55, 1), MathTex("g(x):y", "{=}", "-3x+5", color=GREEN_D)
        )
        label1 = self.label_area(
            axes, (1.25, -2), MathTex("f(x):y", "{=}", "5x-3", color=BLUE_D)
        )
        labels = VGroup(label1, label2, label3)

        nerovnice = Tex(r"Nyní řešme \\ soustavu nerovnic").shift(UP * 1, LEFT * 4.6)

        self.play(FadeIn(nerovnice, shift=UP * 0.5))
        self.wait(2)
        self.play(FadeOut(nerovnice, shift=UP * 0.5))

        # self.play(self.set_gray(first,second,label1,label2))

        ineq3 = MathTex("h(x):y", "{<}", "2x-0.5", color=RED_D).move_to(
            label3[1].get_center()
        )
        self.play(TransformMatchingTex(label3[1], ineq3))
        self.play(Indicate(ineq3[1][0]))
        self.highlight_area(axes, third, -1.35, 3.1, RED_D, False)
        self.fronting(labels)
        self.wait(2)

        ineq2 = MathTex("g(x):y", "{<}", "-3x+5", color=GREEN_D).move_to(
            label2[1].get_center()
        )
        self.play(TransformMatchingTex(label2[1], ineq2))
        self.play(Indicate(ineq2[1][0]))
        self.highlight_area(axes, second, -0.3, 2.7, GREEN_D, True)
        self.fronting(labels)
        self.wait(2)

        ineq1 = MathTex("f(x):y", "{<}", "5x-3", color=BLUE_D).move_to(
            label1[1].get_center()
        )
        self.play(TransformMatchingTex(label1[1], ineq1))
        self.play(Indicate(ineq1[1][0]))
        self.highlight_area(axes, first, -1.35, 3.1, BLUE_D, True)
        self.fronting(labels)
        self.wait(2)

        # řešením nerovnice je vždy poloplocha
        # řešením celé soustavy je region kde se všechny překrývají

        overlap = Polygon(
            axes.c2p(0.83, 1.16, 0),
            axes.c2p(1.1, 1.7, 0),
            axes.c2p(1, 2, 0),
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1,
        )
        self.add(overlap)
        self.play(Circumscribe(overlap))
        self.wait()

        minimum = Dot(axes.c2p(0.83, 1.16, 0), color=YELLOW)
        maximu = Dot(axes.c2p(1.1, 1.7, 0), color=YELLOW)

        self.add(maximu, minimum)
        self.play(Indicate(minimum), Indicate(maximu))

        mline = DashedLine(minimum, axes.c2p(0.83, 0))
        Mline = DashedLine(maximu, axes.c2p(1.1, 0))
        self.play(Write(mline), Write(Mline))