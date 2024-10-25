from manim import *
import constants

LEVA = constants.LEVA
NAHORU = constants.NAHORU
DOLU = constants.DOLU
PRAVA = constants.PRAVA

class Vectors(Scene):
    def calculate_dot(self,c,k,teta):
        uu = 3
        vx = c*2
        vy = k*4
        vv = np.sqrt(vx**2 + vy**2)
        cos = np.cos(teta)
        return [teta, cos, vv*uu*cos]


    def construct(self):

        #--------- Definování ----------------
        self.next_section(skip_animations=True)
        #region
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
            faded_line_ratio=2,  # To make the lines less dominant
            z_index=-1
        )

        # Shift grid and axes to the left to make space for text on the right
        axes.shift(LEFT * 2)

        
        # Add thin grid lines
        axes.add_coordinates()
        axes.get_lines_to_point([0, 0,0])  # Add lines through the origin

        # Shift axes to the right to leave space for text
        axes.shift(RIGHT * 2)

        # Add some text to the left side
        def1 = Tex(r"Vektor je šipka\\ z počátku souřadnic\\ do nějakého bodu.")
        def1.move_to(LEFT*3.5+UP*2.5)  # Position the text on the left side


        # Add everything to the scene

        self.play(FadeIn(axes))
        self.play(Write(def1))
        self.wait(2)

        vector = Vector(axes.c2p(2,3),color=RED_D,z_index=2)
        self.play(FadeIn(vector))
        self.wait(2)

        dot = Dot(axes.c2p(2,3),z_index=3)
        dot_label = Tex(r"(2,3)").next_to(dot,UP)

        def2 = Tex(r"Protože začátek je pro\\ každý vektor stejný,\\ budeme si pamatovat\\ hlavně jeho konec."
                   ).move_to(LEFT*LEVA+DOWN*DOLU)
        self.play(Write(def2))

        self.play(FadeIn(dot),Write(dot_label))
        self.wait(2)
        

        vec = Tex("Vektor značíme šipkou.").move_to(RIGHT*PRAVA+DOWN*DOLU)
        
        znaceni = MathTex("=",r"\vec{v}").move_to(dot_label).shift(RIGHT*0.5)
        znaceni[1].set_color(RED_D)
        self.play(Write(vec))
        self.play(dot_label.animate.shift(LEFT*0.5),FadeIn(znaceni,shift=RIGHT*0.5))
        self.wait()
        self.play(Circumscribe(znaceni[1]))
        self.wait(2)
        

        self.play(FadeOut(def1,def2,znaceni,dot,dot_label,vec))

        velikost = Tex(r"Co nás u vektorů bude\\ zajímat, je například\\ jejich Velikost."
                       ).move_to(LEFT*LEVA+UP*NAHORU)

        general = Vector(axes.c2p(4,4),color=RED_D,z_index=2)
        self.play(Transform(vector,general))
        obecne= MathTex(r"\vec{v}=(v_x,v_y)").next_to(general,UP).shift(RIGHT*2)
        obecne[0][0:2].set_color(RED_D)

        self.play(Write(obecne))
        self.wait()
        self.play(Write(velikost))
        self.wait(2)

        delka = Tex(r"Velikost vektoru značíme $| \vec{v} |$\\ a z pytágorovi věty\\ spočítáme jako:"
                    ).move_to(LEFT*LEVA+DOWN*DOLU)
        delka[0][23:25].set_color(RED_D)
        vzorec = MathTex(r"| \vec{v} | = \sqrt{v_x^2 + v_y^2}").next_to(delka,RIGHT).shift(RIGHT*3)
        vzorec[0][1:3].set_color(RED_D)

        vzorec[0][7:10].set_color(YELLOW)
        vzorec[0][11:15].set_color(YELLOW)

        v_box = SurroundingRectangle(
            vzorec, color=WHITE, fill_color=BLACK, fill_opacity=1, z_index=0,buff=0.2
        )


        self.play(Write(delka))
        self.wait(3)
        self.play(AnimationGroup(DrawBorderThenFill(v_box),Write(vzorec)))
        self.wait(3)

        x = DashedLine(axes.c2p(4,4),axes.c2p(4,0),color=YELLOW)
        x_lab = MathTex(r"v_y",color=YELLOW).next_to(x.get_last_handle(),RIGHT).shift(UP)
        y = DashedLine(axes.c2p(4,0),axes.c2p(0,0),color=YELLOW,z_index=1)
        y_lab = MathTex(r"v_x",color=YELLOW).next_to(y.get_last_handle(),DOWN).shift(RIGHT*3)

        self.play(Write(x),Write(y))
        self.play(Write(x_lab),Write(y_lab))
        self.wait()
        self.play(Indicate(obecne[0][4:6]),Indicate(obecne[0][7:9]))
        self.wait(5)

        self.play(FadeOut(x,y,y_lab,x_lab,delka,velikost,vzorec,vector,obecne,axes,v_box))
        #endregion
        
        #--------- Škálování ------
        self.next_section(skip_animations=True)
        #region

        intro = Tex(
            r"\centering \section*{2.~Sčítání vektorů a násobení skalárem.}"
        ) 
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))

        axes.x_axis.numbers.set_opacity(0)
        axes.y_axis.numbers.set_opacity(0)

        self.play(FadeIn(axes))

        skalovani = Tex(r"Násobení vektoru číslem,\\ neboli škálování, je intuitivní:"
                        ).move_to(LEFT*LEVA+UP*NAHORU)
        gen = MathTex(r"\alpha", r"\vec{v}",r" = (\alpha ",r"v_x",r",\alpha",r"v_y",")"
                        ).move_to(LEFT*LEVA+UP*1)
        gen[1].set_color(RED_D)
        gen[3].set_color(RED_D)
        gen[5].set_color(RED_D)

        gen[0].set_color(GOLD_C)
        gen[2][2:].set_color(GOLD_C)
        gen[4][1:].set_color(GOLD_C)

        g_box = SurroundingRectangle(
            gen, color=WHITE, fill_color=BLACK, fill_opacity=1, z_index=0,buff=0.2
        )

        popis = Tex("Kde", r"~$v_x$~", r"značí $x$-ovou\\ složku vektoru",r"~$\vec{v}$~",r"a $\alpha \in \mathbb{R}$."
                    ).move_to(DOWN*DOLU+RIGHT*PRAVA)
        popis[1].set_color(RED_D)
        popis[3].set_color(RED_D)
        popis[4][1].set_color(GOLD_C)

        c=ValueTracker(1)
        normal = Vector(axes.c2p(c.get_value()*2,c.get_value()*2),color=RED_D)
        normal.add_updater(
            lambda m: m.become(Vector(axes.c2p(c.get_value()*2,c.get_value()*2),color=RED_D))
            )
        
        def nl_updater(m):
            if c.get_value()>0:
                m.become(
                    MathTex(f"{c.get_value():.2f}",r"\vec{v}").next_to(normal,RIGHT)
                )
            else:
                m.become(
                    MathTex(f"{c.get_value():.2f}",r"\vec{v}").next_to(normal,LEFT)
                )
            m[1].set_color(RED_D)

        nl = MathTex(f"{c.get_value()}",r"\vec{v}").next_to(normal,RIGHT)
        nl.add_updater(nl_updater)
        
        self.play(Write(skalovani))
        self.wait(1)
        self.play(FadeIn(normal),Write(nl))
        self.wait(2)
        self.play(AnimationGroup(DrawBorderThenFill(g_box),Write(gen)))
        self.wait(2)
        self.play(Write(popis))
        self.wait(6)
        self.play(c.animate.set_value(2),run_time=3.5)
        self.play(c.animate.set_value(-2),run_time=3.5)
        self.wait()

        self.play(FadeOut(nl,normal,skalovani,gen,popis,g_box))
        #endregion

        #----------- Sčítání ----------------
        self.next_section(skip_animations=True)
        #region
        scitani = Tex(r"Jestliže chceme sečíst\\ vektory $\vec{v}$ a $\vec{u}$,\\ položíme konec jednoho z nich\\ na začátek toho druhého. "
                      ).move_to(LEFT*LEVA+UP*NAHORU)
        scitani[0][30:32].set_color(RED_D)
        scitani[0][33:35].set_color(GREEN_D)
        
        vec1 = Vector(axes.c2p(3,5),color=RED_D)
        v_lab = MathTex(r"\vec{v}",color=RED_D,z_index=1
                        ).next_to(vec1,LEFT).shift(RIGHT)
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
        self.wait(4)

        self.play(FadeOut(w,w_lab,vzorec,scitani,w_box,))

        #endregion

        #------------- Odčítání --------------
        self.next_section(skip_animations=True)
        #region

        u_lab.clear_updaters()
        u_lab.add_updater(lambda m: m.next_to(vec2,LEFT))
        self.play(
            Transform(vec2,Vector(axes.c2p(2,-1),color=GREEN_D))
            )

        self.play(Transform(vec1,Vector(axes.c2p(2,2),color=RED_D)))

        odcitani = Tex("Rozdíl",r"~$\vec{v}~$","a",r"~$\vec{u}$~",r"\\je součet menšence s mínus\\ jedna násobkem menšitelem"
                       ).move_to(LEFT*(LEVA+0.3)+UP*(NAHORU+0.2))
        odcitani[1].set_color(RED_D)
        odcitani[3].set_color(GREEN_D)



        mu = MathTex("-",r"\vec{u}").next_to(vec2,LEFT)
        mu[1].set_color(GREEN_D)

        self.play(Write(odcitani))
        self.wait(4)
        self.play(AnimationGroup(
            Transform(vec2,Vector(axes.c2p(-2,1),color=GREEN_D)),
            u_lab.animate.become(mu),
            ),lag_ratio=0.5)
        self.wait()
        self.play(Flash(u_lab[0]))
        self.wait(3)
        self.play(vec1.animate.move_to(axes.c2p(-1,2)))
        self.wait(3)

        w2=Vector(axes.c2p(0,3),color=BLUE_D)
        w_l = MathTex(r"\vec{w}","=",r"\vec{v}","+ (-",r"\vec{u}",")",z_index=2
                      ).next_to(w2,RIGHT*0.1)
        w_l[0].set_color(BLUE_D)
        w_l[2].set_color(RED_D)
        w_l[4].set_color(GREEN_D)

        self.play(FadeIn(w2,w_l))
        self.wait(3)

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
        self.wait(5)
        self.play([FadeOut(mob) for mob in self.mobjects])
        #endregion

        #---------- Skalární součin ----------
        self.next_section(skip_animations=False)
        #region
        intro_ssoucin = Tex(
            r"\centering \section*{3.~Skalární součin.}"
        ) 
        self.play(Write(intro_ssoucin))
        self.wait(1)
        self.play(FadeOut(intro_ssoucin))
        self.play(FadeIn(axes))

        c = ValueTracker(1)
        k = ValueTracker(1)
        v = Vector(axes.c2p(c.get_value()*2,k.get_value()*4),color=RED_D)
        u = Vector(axes.c2p(3,0),color=GREEN_D)

        v.add_updater(
            lambda mob: mob.become(Vector(axes.c2p(c.get_value()*2,k.get_value()*4),color=RED_D))
        )


        vl = MathTex(r"\vec{v}",color=RED_D).next_to(v,LEFT).shift(UP)
        ul = MathTex(r"\vec{u}",color=GREEN_D).next_to(u,DOWN)

        ul.add_updater(lambda m: m.next_to(u,DOWN))
        vl.add_updater(lambda m: m.next_to(v,LEFT).shift(UP))
        teta = Angle(u,v,radius=0.8,color=BLUE_D)
        tl = MathTex(r"\theta",color=BLUE_D).next_to(teta,RIGHT)

        self.play(FadeIn(u),FadeIn(v),FadeIn(vl),FadeIn(ul),FadeIn(teta),FadeIn(tl))



        sdef1 = Tex(r"Geometrická definice \\ skalárního součinu je:"
                    ).move_to(LEFT*LEVA+UP*NAHORU)
        
       
        svzor = MathTex(r"\vec{v}",r"~\cdot~",
                    r"\vec{u}",r"~=~",
                    r"|\vec{v}|",r"|\vec{u}|",r"\cos \theta"
                    ).move_to(LEFT*LEVA+UP*(NAHORU-1.5))
        
        svzor[0].set_color(RED_D)
        svzor[4][1:3].set_color(RED_D)

        svzor[2].set_color(GREEN_D)
        svzor[5][1:3].set_color(GREEN_D)

        svzor[6][3].set_color(BLUE_D)


        scal_box = SurroundingRectangle(
            svzor, color=WHITE, fill_color=BLACK, fill_opacity=1, z_index=0,buff=0.2
        )
        self.play(AnimationGroup(
            Write(sdef1),
            DrawBorderThenFill(scal_box),
            Write(svzor),
            lag_ratio=0.5
        ))


        skalar = Tex(r"Výsledkem skalárního součinu\\ je skalár, neboli číslo."
                     ).move_to(LEFT*LEVA+DOWN*DOLU)
        self.play(Write(skalar))

        proc = Tex(r"Proč zrovna~",r"$\cos \theta$","?!"
                   ).move_to(LEFT*LEVA+UP*NAHORU)
        proc[1][3].set_color(BLUE_D)

        self.play(AnimationGroup(
            FadeOut(sdef1,shift=UP*0.5),
            FadeIn(proc,shift=UP*0.5))
            )

        self.play(FadeOut(skalar))

        projekce = Tex(r"Abychom mohli pouze\\ vynásobit velikosti vektorů\\ musí být tyto velikosti\\ ve ", "stejném"," směru."
                       ).move_to(LEFT*LEVA+DOWN*DOLU)
        

        stejny_smer = Tex(r"Funkce cosinus tedy\\ promítá jeden vektor\\ do směru toho druhého"
                          ).move_to(RIGHT*PRAVA+DOWN*DOLU)
    
        self.play(Write(projekce))
        self.play(Circumscribe(projekce[1]))
        self.play(Write(stejny_smer))

        balls = v.copy()
        self.play(ReplacementTransform(
            balls,Vector(axes.c2p(2,0),color=PURPLE)
        ))

        self.play(FadeOut(balls, stejny_smer,projekce))


        gen_dot = MathTex(r"\vec{v}",r"~\cdot~",
                    r"\vec{u}",r"~=~",f"{round(self.calculate_dot(c.get_value(),k.get_value(),teta.get_value())[2],2)}"
                    )
        gen_dot[0].set_color(RED_D)
        gen_dot[2].set_color(GREEN_D)

        def gen_dot_updater(mob):
            final = MathTex(r"\vec{v}",r"~\cdot~",
                    r"\vec{u}",r"~=~",f"{round(self.calculate_dot(c.get_value(),k.get_value(),teta.get_value())[2],2)}"
                    )
            final[0].set_color(RED_D)
            final[2].set_color(GREEN_D)
            return mob.become(final)
        gen_dot.add_updater(gen_dot_updater)

        
        cosinus = MathTex(r"\cos",r"\theta","~=~",
                          f"{round(self.calculate_dot(c.get_value(),k.get_value(),teta.get_value())[1],2)}"
                          ).next_to(gen_dot,DOWN)
        cosinus[1].set_color(BLUE_D)

        def cos_updater(mob):
            final = MathTex(r"\cos",r"\theta","~=~",
                          f"{round(self.calculate_dot(c.get_value(),k.get_value(),teta.get_value())[1],2)}"
                          )
            final[1].set_color(BLUE_D)
            mob.become(final)
        cosinus.add_updater(cos_updater)

        theta = MathTex(r"\theta","~=~",
                        f"{round(self.calculate_dot(c.get_value(),k.get_value(),teta.get_value())[0],2)}"
                        ).next_to(cosinus,DOWN)
        theta[0].set_color(BLUE_D)

        def theta_updater(mob):
            final = MathTex(r"\theta","~=~",
                        f"{round(self.calculate_dot(c.get_value(),k.get_value(),teta.get_value())[0],2)}"
                        ).next_to(cosinus,DOWN)
            final[0].set_color(BLUE_D)
            mob.become(final)
        theta.add_updater(theta_updater)

        text = VGroup(gen_dot,cosinus,theta)
        text.arrange(DOWN,aligned_edge = LEFT)
        text.shift(LEFT*LEVA+DOWN*DOLU)
        gen_lab = SurroundingRectangle(
            text, color=WHITE, fill_color=BLACK, fill_opacity=1, z_index=0,buff=0.2
        )

        self.play(AnimationGroup(DrawBorderThenFill(gen_lab),Write(text)))

        self.play(c.animate.set_value(2))
        self.play(k.animate.set_value(3))




        #pro výpočet skalárního součinu ze souřadnic vektorů vyplatí se použít vztah:
        svzor = MathTex(r"\vec{v}",r"~\cdot~",
                    r"\vec{u}",r"~=~",
                    r"v_x",r"u_x",r"~+~",
                    r"v_y",r"u_y"
                    ).move_to(LEFT*LEVA+UP*(NAHORU-1.5))
        svzor[0].set_color(RED_D)
        svzor[4].set_color(RED_D)
        svzor[7].set_color(RED_D)

        svzor[2].set_color(GREEN_D)
        svzor[5].set_color(GREEN_D)
        svzor[8].set_color(GREEN_D)


        #endregion
