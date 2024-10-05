from manim import *
import constants

LEVA = constants.LEVA
NAHORU = constants.NAHORU
DOLU = constants.DOLU
PRAVA = constants.PRAVA

class Vectors(Scene):
    def construct(self):
        self.next_section(skip_animations=False)
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

        global axes
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
        self.wait(2)

        dot = Dot(axes.c2p(2,3))
        dot_label = Tex(r"(2,3)").next_to(dot,UP)

        self.play(FadeIn(dot),Write(dot_label))
        self.wait(2)
        

        def2 = Tex(r"Do tohoto bodu udělejme \\ šipku z počátku souřadnic.\\Šipka tedy indikuje vektor.").move_to(LEFT*LEVA+DOWN*DOLU)
        self.play(Write(def2))

        vector = Vector(axes.c2p(2,3),color=RED_D)
        self.play(FadeIn(vector))
        self.wait(2)

        znaceni = MathTex(r"(2,3)=\vec{v}").move_to(dot_label).shift(LEFT*0.3)
        znaceni[0][6:8].set_color(RED_D)
        self.play(TransformMatchingTex(dot_label,znaceni))
        self.wait(2)
        

        self.play(FadeOut(def1,def2,znaceni,dot))

        velikost = Tex(r"Co nás u vektorů bude\\ zajímat je například\\ jejich délka.").move_to(LEFT*LEVA+UP*NAHORU)

        general = Vector(axes.c2p(4,4),color=RED_D)
        self.play(Transform(vector,general))
        obecne= MathTex(r"\vec{v}=(x,y)").next_to(general,UP).shift(RIGHT)
        obecne[0][0:2].set_color(RED_D)

        self.play(Write(obecne))
        self.wait()
        self.play(Write(velikost))
        self.wait(2)

        delka = Tex(r"Délku vektoru značíme $\|\vec{v}\|$\\ a z pytágorovi věty\\ spočítáme jako:").move_to(LEFT*LEVA+DOWN*DOLU)
        delka[0][23:25].set_color(RED_D)
        vzorec = MathTex(r"\|\vec{v}\| = \sqrt{x^2 + y^2}").next_to(delka,RIGHT).shift(RIGHT*2)
        vzorec[0][1:3].set_color(RED_D)

        vzorec[0][7:9].set_color(YELLOW)
        vzorec[0][10:14].set_color(YELLOW)

        self.play(Write(delka))
        self.wait(3)
        self.play(Write(vzorec))
        self.wait(3)

        x = DashedLine(axes.c2p(4,4),axes.c2p(4,0),color=YELLOW)
        x_lab = MathTex(r"y",color=YELLOW).next_to(x.get_last_handle(),RIGHT).shift(UP)
        y = DashedLine(axes.c2p(4,4),axes.c2p(0,4),color=YELLOW)
        y_lab = MathTex(r"x",color=YELLOW).next_to(y.get_last_handle(),UP).shift(RIGHT)

        self.play(Write(x),Write(y))
        self.play(Write(x_lab),Write(y_lab))
        self.wait()
        self.play(Indicate(obecne[0][4]),Indicate(obecne[0][6]))
        self.wait(5)

        self.play(FadeOut(x,y,y_lab,x_lab,delka,velikost,vzorec,vector,obecne))

        global scene
        scene = VGroup(axes)
        self.play(FadeOut(scene))


    def section2(self):
        intro = Tex(
            r"\centering \section*{2.~Sčítání vektorů a násobení skalárem.}"
        ) 
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))

        self.play(FadeIn(scene))

        skalovani = Tex(r"Násobení vektoru číslem\\ neboli škálování je intuitivní:"
                        ).move_to(LEFT*LEVA+UP*NAHORU)
        gen = MathTex(r"\alpha", r"\vec{v}",r" = (\alpha ",r"v_x",r",\alpha",r"v_y",")"
                        ).move_to(LEFT*LEVA+UP*1.5)
        gen[1].set_color(RED_D)
        gen[3].set_color(RED_D)
        gen[5].set_color(RED_D)

        popis = Tex("Kde", r"~$v_x$~", r"značí $x$-ovou\\ složku vektoru",r"~$\vec{v}$~",r"a $\alpha \in \mathbb{R}$."
                    ).move_to(DOWN*DOLU+RIGHT*PRAVA)
        popis[1].set_color(RED_D)
        popis[3].set_color(RED_D)

        c=ValueTracker(1)
        normal = Vector(axes.c2p(c.get_value()*2,c.get_value()*2),color=RED_D)
        normal.add_updater(
            lambda m: m.become(Vector(axes.c2p(c.get_value()*2,c.get_value()*2),color=RED_D))
            )
        
        def nl_updater(m):
            if c.get_value()>0:
                m.become(
                    MathTex(f"{np.round(c.get_value(),decimals=2)}",r"\vec{v}").next_to(normal,RIGHT)
                )
            else:
                m.become(
                    MathTex(f"{np.round(c.get_value(),decimals=2)}",r"\vec{v}").next_to(normal,LEFT)
                )
            m[1].set_color(RED_D)

        nl = MathTex(f"{c.get_value()}",r"\vec{v}").next_to(normal,RIGHT)
        nl.add_updater(nl_updater)
        
        self.play(Write(skalovani))
        self.wait()
        self.play(FadeIn(normal),FadeIn(nl))
        self.wait(2)
        self.play(Write(gen))
        self.wait(2)
        self.play(Write(popis))
        self.wait(6)
        self.play(c.animate.set_value(2),run_time=3)
        self.play(c.animate.set_value(-2),run_time=3)
        self.wait()

        self.play(FadeOut(nl,normal,skalovani,gen,popis))


        self.next_section(skip_animations=False)
        #---------------------------------------Sčítání--------------------


        scitani = Tex(r"Jestliže chceme sečíst\\ vektory $\vec{v}$ a $\vec{u}$,\\ položíme konec jednoho z nich\\ na začátek toho druhého. "
                      ).move_to(LEFT*LEVA+UP*NAHORU)
        scitani[0][30:32].set_color(RED_D)
        scitani[0][33:35].set_color(GREEN_D)
        
        vec1 = Vector(axes.c2p(3,5),color=RED_D)
        v_lab = MathTex(r"\vec{v}",color=RED_D).next_to(vec1,LEFT).shift(RIGHT)
        vec2 = Vector(axes.c2p(1,-3),color=GREEN_D)
        u_lab = MathTex(r"\vec{u}",color=GREEN_D).next_to(vec2,RIGHT)

        u_lab.add_updater(lambda m: m.next_to(vec2,RIGHT))
        v_lab.add_updater(lambda m: m.next_to(vec1,LEFT).shift(RIGHT))
        

        self.play(Write(scitani))
        self.play(FadeIn(v_lab,vec1,u_lab,vec2))
        self.wait(5)
        self.play(vec2.animate.move_to(axes.c2p(3.5,3.5)))
        self.wait(3)

        vzorec = MathTex(r"\vec{w}=(v_x+u_x , v_y+u_y)",z_index=2
                         ).move_to(DOWN*DOLU+RIGHT*PRAVA)
        vzorec[0][0:2].set_color(BLUE_D)

        vzorec[0][4:6].set_color(RED_D)
        vzorec[0][10:12].set_color(RED_D)

        vzorec[0][7:9].set_color(GREEN_D)
        vzorec[0][13:15].set_color(GREEN_D)

        w = Vector(axes.c2p(4,2),color=BLUE_D)
        w_lab = MathTex(r"\vec{w}","=",r"\vec{v}","+",r"\vec{u}",z_index=2
                      ).next_to(w,RIGHT*0.1)
        w_lab[0].set_color(BLUE_D)
        w_lab[2].set_color(RED_D)
        w_lab[4].set_color(GREEN_D)


        #What if i want to change the way w is writen later?!

        # wd = MathTex(r"\vec{w}","=",r"\vec{v}","+",r"\vec{u}",z_index=2
        #              ).move_to(DOWN*(DOLU-1)+RIGHT*PRAVA)
        # wd[0].set_color(BLUE_D)
        # wd[2].set_color(RED_D)
        # wd[4].set_color(GREEN_D)

        # wx = MathTex(r"w_x","=",r"v_x","+",r"u_x",z_index=2
        #              ).move_to(DOWN*(DOLU)+RIGHT*PRAVA)
        # wx[0].set_color(BLUE_D)
        # wx[2].set_color(RED_D)
        # wx[4].set_color(GREEN_D)

        # wy = MathTex(r"w_y","=",r"v_y","+",r"u_y",z_index=2
        #              ).move_to(DOWN*(DOLU+1)+RIGHT*PRAVA)
        # wy[0].set_color(BLUE_D)
        # wy[2].set_color(RED_D)
        # wy[4].set_color(GREEN_D)

        # wgroup = VGroup(wd,wx,wy)
        w_box = SurroundingRectangle(
            vzorec, color=WHITE, fill_color=BLACK, fill_opacity=1, z_index=0,buff=0.2
        )

        self.wait(2)
        self.play(FadeIn(w,w_lab))
        self.wait(3)
        self.play(AnimationGroup(DrawBorderThenFill(w_box),Write(vzorec)))
        self.wait(2)

        self.play(FadeOut(w,w_lab,vzorec,scitani,w_box,))

        #-------------------- Odčítání -------------------
        u_lab.clear_updaters()
        u_lab.add_updater(lambda m: m.next_to(vec2,LEFT))
        self.play(
            Transform(vec2,Vector(axes.c2p(2,-1),color=GREEN_D))
            )

        self.play(Transform(vec1,Vector(axes.c2p(2,2),color=RED_D)))

        odcitani = Tex("Rozdíl",r"~$\vec{v}~$","a",r"~$\vec{u}$~",r"\\je součet prvního\\ odčítance s inverzem\\ toho druhého"
                       ).move_to(LEFT*(LEVA+0.3)+UP*NAHORU)
        odcitani[1].set_color(RED_D)
        odcitani[3].set_color(GREEN_D)



        mu = MathTex("-",r"\vec{u}").next_to(vec2,LEFT)
        mu[1].set_color(GREEN_D)

        self.play(Write(odcitani))
        self.wait(3)
        self.play(AnimationGroup(
            Transform(vec2,Vector(axes.c2p(-1,2),color=GREEN_D)),
            u_lab.animate.become(mu),
            ),lag_ratio=0.5)
        self.wait()
        self.play(Flash(u_lab[0]))
        self.wait(2)
        self.play(vec1.animate.move_to(axes.c2p(0,3)))
        self.wait(3)

        w2=Vector(axes.c2p(1,4),color=BLUE_D)
        w_l = MathTex(r"\vec{w}","=",r"\vec{v}","+ (-",r"\vec{u}",")",z_index=2
                      ).next_to(w2,RIGHT*0.1)
        w_l[0].set_color(BLUE_D)
        w_l[2].set_color(RED_D)
        w_l[4].set_color(GREEN_D)

        self.play(FadeIn(w2,w_l))
        self.wait(2)

        aaaaa= Tex("Obecný vzorec je tedy:").move_to(DOWN*DOLU+LEFT*LEVA)
        self.play(Write(aaaaa))
        self.wait()

        vzor = MathTex(r"\vec{w}=(v_x-u_x , v_y-u_y)",z_index=2
                         ).move_to(DOWN*DOLU+RIGHT*PRAVA)
        vzor[0][0:2].set_color(BLUE_D)

        vzor[0][4:6].set_color(RED_D)
        vzor[0][10:12].set_color(RED_D)

        vzor[0][7:9].set_color(GREEN_D)
        vzor[0][13:15].set_color(GREEN_D)

        v_box = SurroundingRectangle(
            vzorec, color=WHITE, fill_color=BLACK, fill_opacity=1, z_index=0,buff=0.2
        )
        self.play(AnimationGroup(DrawBorderThenFill(v_box),Write(vzor)))
        self.wait(4)



