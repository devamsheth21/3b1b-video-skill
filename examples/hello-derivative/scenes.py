from manim import *

config.background_color = "#1E1E1E"


class Beat1Question(Scene):
    def construct(self):
        # Beat 1 (~7s audio)
        # Say: "The derivative of x squared is two x. But why? Let's watch it happen."
        title = Text("The derivative of x² is 2x.", font_size=42)
        sub = Text("But why? Let's watch it happen.", font_size=28, color=GREY_B)
        sub.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(sub), run_time=1)
        self.wait(4)


class Beat2Square(Scene):
    def construct(self):
        # Beat 2 (~16s audio)
        # Say: "Start with a square of side x. Its area is x squared. Now let the side
        #       grow by a tiny amount. The new area is two thin strips, each x by the
        #       tiny growth, plus a negligible corner. So the growth of the area is
        #       two x times the tiny growth. That is why the derivative is two x."
        side = 2.0
        grown = 3.0
        ds = grown - side  # 1.0, exaggerated so it's visible

        # Anchor the bottom-left corner so growth extends right and up;
        # then the added region is exactly: right strip + top strip + corner.
        anchor = LEFT * 2.5 + DOWN * 1.5

        def anchored_square(s):
            return Square(side_length=s, color=BLUE, fill_opacity=0.35).move_to(
                anchor + RIGHT * (s / 2) + UP * (s / 2)
            )

        square = anchored_square(side)
        side_label = Text("side = x", font_size=28, color=GREY_B)
        side_label.next_to(square, DOWN, buff=0.3)
        area_label = Text("area = x²", font_size=28, color=BLUE_B)
        area_label.next_to(square, UP, buff=0.3)

        self.play(FadeIn(square), FadeIn(side_label), FadeIn(area_label), run_time=2)
        self.wait(2)

        big = anchored_square(grown)
        self.play(
            FadeOut(side_label),
            FadeOut(area_label),
            Transform(square, big),
            run_time=2.5,
        )

        # The added L-region: right strip + top strip (yellow), corner (red)
        right_strip = Rectangle(
            width=ds, height=grown, color=YELLOW, fill_opacity=0.6, stroke_width=0
        ).move_to(anchor + RIGHT * (side + ds / 2) + UP * (grown / 2))
        top_strip = Rectangle(
            width=side, height=ds, color=YELLOW, fill_opacity=0.6, stroke_width=0
        ).move_to(anchor + RIGHT * (side / 2) + UP * (side + ds / 2))
        corner = Square(
            side_length=ds, color=RED, fill_opacity=0.8, stroke_width=0
        ).move_to(anchor + RIGHT * (side + ds / 2) + UP * (side + ds / 2))

        extra_label = Text(
            "new area ≈ 2·x·(tiny growth)", font_size=30, color=YELLOW
        ).to_edge(DOWN, buff=0.6)

        self.play(FadeIn(right_strip), FadeIn(top_strip), run_time=1.5)
        self.play(FadeIn(corner), FadeIn(extra_label), run_time=1.5)
        self.wait(4)
