from manim import *

class Functions(Scene):
        def construct(self):
            napis = Tex("Jejich grafy jsou:").shift(UP*3.5,LEFT*0.1)
            self.play(FadeIn(napis))


            ax = Axes(x_range=[-2,4],y_range=[-3,6]).add_coordinates()

            c=ValueTracker(0)
            d=4
            first = ax.plot(lambda x: 5*x-3,x_range=[-0.3,2],color = BLUE_D)
            label1 = (MathTex(r"f(x):y=5x-3",color = BLUE_D).next_to(first,DOWN,buff=-2)).shift(RIGHT*0.7)

            second = ax.plot(lambda x: -3*x+5,x_range=[-0.3,3.5],color=GREEN_D)
            label2 =  (MathTex(r"g(x):y=-3x+5",color=GREEN_D).next_to(second,RIGHT,buff=-3.6)).shift(UP*0.2)

            
            third = ax.plot(lambda x: 2*x+c.get_value(),x_range=[-1.5,3.5],color=RED_D)
            third.add_updater(
                  lambda mob: mob.become(
                        ax.plot(lambda x: 2*x+c.get_value(),color=RED_D)
                  )
            )
            label3 = (MathTex(f"h(x):y=2x+{c.get_value()}",color=RED_D).next_to(third,RIGHT,buff=-4))

            def label3_updater(mob):
                  if c.get_value()>0:
                        mob.become(MathTex(f"h(x):y=2x+{np.round(c.get_value(),decimals=2)}",color=RED_D))
                  else:
                        mob.become(MathTex(f"h(x):y=2x{np.round(c.get_value(),decimals=2)}",color=RED_D))
                  mob.next_to(third,RIGHT,buff=-5)
                                 

            dot_axes = Dot(ax.coords_to_point(1, 2), color=YELLOW)
            lines = ax.get_lines_to_point(ax.c2p(1,2))


            self.play(Write(ax))
            self.play(Write(first),Write(label1))
            self.play(Write(second),Write(label2))
            self.play(Write(third),Write(label3))
            self.wait(2)

            reseni = Tex(r"Řešením je $x$\\ takové, že\\ $f(x)=g(x)=h(x)$.").shift(UP*1,LEFT*4.7)
            reseni[0][24:28].set_color(BLUE_D)
            reseni[0][29:33].set_color(GREEN_D)
            reseni[0][34:38].set_color(RED_D)
            self.wait(2)
            self.play(Write(reseni))
            self.wait(4)

            self.play(Write(dot_axes),Write(lines))

            prusecik = Tex(r"Musíme tedy\\najít průsečík\\těchto tří funkcí.").shift(UP*1,LEFT*4.6)
            self.play(FadeOut(reseni,shift=UP*0.5))
            self.play(FadeIn(prusecik,shift=UP*0.5))
            self.play(FocusOn(dot_axes))
            self.wait(4)

            overte = Tex(r"V tomto případě\\ je řešením $x=1$.\\ Řešení ověřte!").shift(UP*1,LEFT*4.6)
            self.play(FadeOut(prusecik,shift=UP*0.5))
            self.play(FadeIn(overte),shift=UP*0.5)
            self.wait(4)
            self.play(FadeOut(overte))

            label3.add_updater(label3_updater)
            self.play(c.animate.set_value(2))
            self.play(c.animate.set_value(-1))
            self.play(c.animate.set_value(-0.5))


            neresitelnost = Tex(r"Jestliže neexistuje\\ jeden průsečík,\\ neexistuje ani řešení.").shift(UP*1,LEFT*4.7)
            self.play(FadeIn(neresitelnost,shift=UP*0.5))
            self.wait(2)

            self.play(FadeOut(dot_axes),FadeOut(lines))



class EquationSystem(Scene):
      def construct(self):
            intro = Tex(r"\centering \section{Grafické řešení soustavy\\ lineárních rovnic}")
            self.play(Write(intro))
            self.wait()
            self.play(FadeOut(intro))

            problem = Tex("Řešme soustavu:").shift(UP*2)

            rimske  = VGroup(
                  Tex("I.",color=BLUE_D).shift(UP),
                  Tex("II.",color=GREEN_D).shift(UP*0.3),
                  Tex("III.",color=RED_D).shift(DOWN*0.4)
                  )
            rimske = rimske.shift(LEFT*1.7)

            funkce = VGroup(
                  MathTex("f(x):",color=BLUE_D).shift(UP),
                  MathTex("g(x):",color=GREEN_D).shift(UP*0.3),
                  MathTex("h(x):",color=RED_D).shift(DOWN*0.4)
                  )
            funkce = funkce.shift(LEFT*2.1)



            jedna = (MathTex("y=5x-3",color=BLUE_D)).shift(UP)
            dva = (MathTex("y=-3x+5",color=GREEN_D))
            tri = (MathTex("y=2x",color=RED_D)).shift(DOWN)

            soustava = VGroup(jedna,dva,tri)
            soustava.arrange(DOWN, center=False, aligned_edge=LEFT)  
            # rimske.arrange(DOWN, center=False, aligned_edge=LEFT) 
            # funkce.arrange(DOWN, center=False, aligned_edge=LEFT) 
            
            self.play(Write(problem))
            self.play(Write(rimske),Write(soustava))
            self.wait(2)
            reseni = Tex("Každá lineární rovnice definuje lineární funkci:").shift(UP*2)


            self.play(FadeOut(problem,shift=UP*0.5))
            self.play(FadeIn(reseni,shift=UP*0.5))
            self.wait()
            self.play(Transform(rimske,funkce))

            bottom_text = Tex("Tyto funkce můžeme graficky znázornit.").shift(DOWN*1.7)
            self.play(FadeIn(bottom_text,shift=UP*0.5))
            self.wait(2)

