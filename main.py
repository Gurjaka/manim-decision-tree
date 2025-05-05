from manim import *

fs = 32


class DecisionTree(Scene):

    def intro(self) -> VGroup:
        rr = RoundedRectangle(height=1)
        text = Text("Decision Tree", font_size=fs)
        text.move_to(rr.get_center())

        self.play(Create(rr))
        self.play(Write(text))
        self.wait(2)
        self.play(rr.animate.shift(UP * 3), text.animate.shift(UP * 3))

        return VGroup(rr, text)

    def explanation(self) -> Text:
        cfs = fs - 8

        text = Text("make decisions by asking questions step-by-step.", font_size=cfs)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(text.animate.shift(UP * 2))

        return text

    def maketreebase(self) -> VGroup:
        """
        Create tree node visual
        """

        # Custom font size for this screen
        cfs = fs - 8

        # Root Node
        root = RoundedRectangle(height=1, width=2, color="#81a1c1").shift(UP)
        root_text = Text("Root Node", font_size=cfs)
        root_text.move_to(root.get_center())

        # Internal Node 1
        node1 = RoundedRectangle(height=1, width=3, color="#81a1c1").shift(
            LEFT * 3 + DOWN * 2
        )
        node1_text = Text("Internal Node", font_size=cfs)
        node1_text.move_to(node1.get_center())

        # Internal Node 2
        node2 = RoundedRectangle(height=1, width=3, color="#81a1c1").shift(
            RIGHT * 3 + DOWN * 2
        )
        node2_text = Text("Internal Node", font_size=cfs)
        node2_text.move_to(node2.get_center())

        # Create branches (lines)
        branch1 = Line(root.get_bottom(), node1.get_top())
        branch2 = Line(root.get_bottom(), node2.get_top())

        # Create a tree group
        tree = VGroup(root, node1, node2, branch1, branch2)
        text = VGroup(root_text, node1_text, node2_text)

        self.play(Create(tree), FadeIn(text))
        self.wait(2)

        return VGroup(tree, text)

    def addtreenodes(self, root) -> tuple[VGroup, AnimationGroup]:
        cfs = fs - 12

        # Internal Node 1 - Left
        leftnode = RoundedRectangle(height=1, width=2, color="#81a1c1")
        leftnode.move_to(root.get_center() + DOWN * 2 + LEFT * 1.8)
        leftnode_text = Text("Left Node", font_size=cfs).move_to(leftnode.get_center())

        # Internal Node 2 - Right
        rightnode = RoundedRectangle(height=1, width=2, color="#81a1c1")
        rightnode.move_to(root.get_center() + DOWN * 2 + RIGHT * 1.8)
        rightnode_text = Text("Right Node", font_size=cfs).move_to(
            rightnode.get_center()
        )

        # Create branches (lines)
        branch1 = Line(root.get_bottom(), leftnode.get_top())
        branch2 = Line(root.get_bottom(), rightnode.get_top())

        # Group shapes and text
        tree = VGroup(leftnode, rightnode, branch1, branch2)
        text = VGroup(leftnode_text, rightnode_text)

        animations = AnimationGroup(Create(tree), FadeIn(text))

        return VGroup(tree, text), animations

    def display_example(self) -> Text:
        text = Text("Lets see an example", font_size=fs)
        self.play(Write(text))

        return text

    def display_hotel(self) -> VGroup:
        cfs = fs - 12
        rr = RoundedRectangle(height=1, width=4.2)
        text = Text("Should I Book This Hotel?", font_size=cfs)
        text.move_to(rr.get_center())
        self.play(Create(rr), Write(text))

        return VGroup(rr, text)

    def construct(self):
        # Introduction
        intro = self.intro()
        explaination = self.explanation()
        treebase = self.maketreebase()

        # Remove unnecessary elements
        self.play(FadeOut(VGroup(intro, explaination)))
        self.play(treebase.animate.shift(UP * 2))

        # Add nodes to tree
        leftnode, anim_left_n = self.addtreenodes(treebase[0][1])
        rightnode, anim_right_n = self.addtreenodes(treebase[0][2])
        self.play(anim_left_n, anim_right_n)

        # Delay before removing text
        self.wait(2)

        # Remove bloat
        self.play(FadeOut(treebase), FadeOut(leftnode), FadeOut(rightnode))

        # Display example screen
        example = self.display_example()
        self.wait(2)
        self.play(FadeOut(example))

        # Display actual exmaple (hotel)
        hotel = self.display_hotel()
        self.wait(2)
        self.play(hotel.animate.shift(UP * 3))

        self.wait(1)
