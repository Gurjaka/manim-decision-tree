from manim import *

fs = 32
fn = "JetBrainsMono Nerd Font Medium"


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

        text = Text(
            "make decisions by asking questions step-by-step.", font=fn, font_size=cfs
        )
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
        root_text = Text("Root Node", font_size=cfs, font=fn)
        root_text.move_to(root.get_center())

        # Internal Node 1
        node1 = RoundedRectangle(height=1, width=3, color="#81a1c1").shift(
            LEFT * 3 + DOWN * 2
        )
        node1_text = Text("Internal Node", font_size=cfs, font=fn)
        node1_text.move_to(node1.get_center())

        # Internal Node 2
        node2 = RoundedRectangle(height=1, width=3, color="#81a1c1").shift(
            RIGHT * 3 + DOWN * 2
        )
        node2_text = Text("Internal Node", font_size=cfs, font=fn)
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
        leftnode_text = Text("Left Node", font_size=cfs, font=fn).move_to(
            leftnode.get_center()
        )

        # Internal Node 2 - Right
        rightnode = RoundedRectangle(height=1, width=2, color="#81a1c1")
        rightnode.move_to(root.get_center() + DOWN * 2 + RIGHT * 1.8)
        rightnode_text = Text("Right Node", font_size=cfs, font=fn).move_to(
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
        text = Text("Lets see an example", font_size=fs, font=fn)
        self.play(Write(text))

        return text

    def display_hotel(self) -> Text:
        cfs = fs - 12
        text = Text("Should I Book This Hotel?", font_size=cfs, font=fn)
        self.play(Write(text))

        return text

    def make_hotel_base(self) -> VGroup:
        cfs = fs - 16

        root = Text("Is the price within budget?", font_size=cfs, font=fn)

        node1 = Text("Yes", font_size=cfs, font=fn).move_to(
            root.get_center() + DOWN + LEFT * 2
        )
        node2 = Text("No", font_size=cfs, font=fn).move_to(
            root.get_center() + DOWN + RIGHT * 2
        )

        branch1 = Line(
            root.get_bottom() + DOWN * 0.1, node1.get_top() + UP * 0.1, stroke_width=1
        )
        branch2 = Line(
            root.get_bottom() + DOWN * 0.1, node2.get_top() + UP * 0.1, stroke_width=1
        )

        self.play(FadeIn(root))
        self.play(Write(node1), Write(node2))
        self.play(Create(branch1), Create(branch2))

        return VGroup(root, node1, node2, branch1, branch2)

    def add_right_node(self, root, text) -> VGroup:
        cfs = fs - 16

        # Internal Node 2 - Right
        rightnode = Text(text, font_size=cfs, font=fn)
        rightnode.move_to(root.get_center() + DOWN * 0.8)

        # Create branches (lines)
        branch = Line(
            root.get_bottom() + DOWN * 0.1,
            rightnode.get_top() + UP * 0.1,
            stroke_width=1,
        )

        # Group shapes and text
        tree = VGroup(rightnode, branch)

        self.play(FadeIn(rightnode))
        self.play(Create(branch))

        return tree

    def add_left_node(self, root, text) -> VGroup:
        cfs = fs - 16

        # Main question node
        leftroot = Text(text, font_size=cfs)
        leftroot.move_to(root.get_center() + DOWN * 0.8)

        # Child options with smaller horizontal spacing
        node1 = Text("Yes", font_size=cfs).move_to(
            leftroot.get_center() + DOWN * 0.8 + LEFT * 1.3
        )
        node2 = Text("No", font_size=cfs).move_to(
            leftroot.get_center() + DOWN * 0.8 + RIGHT * 1.3
        )

        # Branches: shorter and more proportional
        branch = Line(
            root.get_bottom() + DOWN * 0.1,
            leftroot.get_top() + UP * 0.1,
            stroke_width=1,
        )
        branch1 = Line(
            leftroot.get_bottom() + DOWN * 0.1 + LEFT * 0.5,
            node1.get_top() + UP * 0.1,
            stroke_width=1,
        )
        branch2 = Line(
            leftroot.get_bottom() + DOWN * 0.1 + RIGHT * 0.5,
            node2.get_top() + UP * 0.1,
            stroke_width=1,
        )

        tree = VGroup(leftroot, node1, node2, branch, branch1, branch2)

        self.play(FadeIn(leftroot))
        self.play(Create(branch))
        self.play(Write(node1), Write(node2))
        self.play(Create(branch1), Create(branch2))

        return tree

    def book_it(self, root) -> VGroup:
        cfs = fs - 16

        # Internal Node 2 - Right
        rightnode = Text("Book it", font_size=cfs, font=fn)
        rightnode.move_to(root.get_center() + DOWN * 0.8)

        # Create branches (lines)
        branch = Line(
            root.get_bottom() + DOWN * 0.1,
            rightnode.get_top() + UP * 0.1,
            stroke_width=1,
        )

        # Group shapes and text
        tree = VGroup(rightnode, branch)

        self.play(FadeIn(rightnode))
        self.play(Create(branch))

        return tree

    def display_text(self, text) -> Text:
        cfs = fs - 12
        text = Text(text, font_size=cfs, font=fn)

        return text

    def outro(self) -> VGroup:
        rr = RoundedRectangle(height=1, width=5)
        text = Text("Thanks for watching", font_size=fs)
        text.move_to(rr.get_center())

        self.play(Create(rr))
        self.play(Write(text))
        self.wait(2)

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

        hotel_tree = self.make_hotel_base()
        self.play(hotel_tree.animate.shift(UP * 2.5))

        right_node = self.add_right_node(hotel_tree[2], "Don't Book")
        oob = self.display_text("If hotel is out of budget, don't book.")
        self.play(Write(oob))

        self.wait(2)
        self.play(FadeOut(oob))

        left_node = self.add_left_node(
            hotel_tree[1], "Does it have good reviews (4★+)?"
        )
        lright_node = self.add_right_node(left_node[2], "Don't Book")

        # Store copies of nodes before fading everything out
        left_node_copy = left_node.copy()
        lright_node_copy = lright_node.copy()

        # Fade out everything
        self.play(
            FadeOut(hotel),
            FadeOut(hotel_tree),
            FadeOut(right_node),
            FadeOut(left_node),
            FadeOut(lright_node),
        )

        # Display the bad review text
        bad_review = self.display_text(
            "If hotel has bad review (less than 4★), don't book."
        )
        self.play(Write(bad_review))

        # Wait 2 seconds
        self.wait(2)

        # Fade out bad review
        self.play(FadeOut(bad_review))

        # Calculate original relative position of lright_node to left_node
        original_offset = lright_node[0].get_center() - left_node[2].get_center()

        # Redisplay the left_node subtree in middle-top location
        left_node_copy.move_to(UP * 2)  # Move to middle-top

        # Position lright_node_copy relative to the new position of left_node[2] in left_node_copy
        node2_new_pos = left_node_copy[2].get_center()
        lright_node_copy.shift(
            node2_new_pos + original_offset - lright_node_copy[0].get_center()
        )

        self.play(FadeIn(left_node_copy), FadeIn(lright_node_copy))

        sub_left_node = self.add_left_node(
            left_node_copy[1], "Is the location convenient?"
        )
        book1 = self.book_it(sub_left_node[1])

        self.wait(1)

        sub_left_node_copy = sub_left_node.copy()
        book1_copy = book1.copy()

        original_offset = book1[0].get_center() - sub_left_node[1].get_center()
        sub_left_node_copy.move_to(UP * 2)

        node2_new_pos = sub_left_node_copy[1].get_center()
        book1_copy.shift(node2_new_pos + original_offset - book1_copy[0].get_center())

        self.play(
            FadeOut(left_node_copy),
            FadeOut(lright_node_copy),
            FadeOut(sub_left_node),
            FadeOut(book1),
        )

        book1_explain1 = self.display_text("If it's in budget and has good reviews:")
        book1_explain2 = self.display_text("If location is convenient, Book it")

        book1_explain2.next_to(book1_explain1, DOWN, buff=0.3)
        self.play(Write(book1_explain1))
        self.play(Write(book1_explain2))

        self.wait(2)
        self.play(FadeOut(book1_explain1), FadeOut(book1_explain2))

        self.play(FadeIn(sub_left_node_copy), FadeIn(book1_copy))

        sub_right_node = self.add_left_node(
            sub_left_node_copy[2], "Is it close to public transport?"
        )

        book2 = self.book_it(sub_right_node[1])
        self.wait(1)

        sub_left_node = sub_left_node_copy.copy()
        book1 = book1_copy.copy()
        sub_right_node_copy = sub_right_node.copy()
        book2_copy = book2.copy()

        self.play(
            FadeOut(sub_left_node_copy),
            FadeOut(book1_copy),
            FadeOut(sub_right_node),
            FadeOut(book2),
        )

        book2_explain1 = self.display_text("If it's in budget and has good reviews:")
        book2_explain2 = self.display_text(
            "If not convenient, but close to transport, Book it"
        )

        book2_explain2.next_to(book2_explain1, DOWN, buff=0.3)
        self.play(Write(book2_explain1))
        self.play(Write(book2_explain2))

        self.wait(2)

        self.play(FadeOut(book2_explain1), FadeOut(book2_explain2))

        self.play(
            FadeIn(sub_left_node),
            FadeIn(book1),
            FadeIn(sub_right_node_copy),
            FadeIn(book2_copy),
        )

        right_node = self.add_right_node(sub_right_node[2], "Don't Book")
        self.wait(1)

        sub_left_node_copy = sub_left_node.copy()
        book1_copy = book1.copy()
        sub_right_node = sub_right_node_copy.copy()
        book2 = book2_copy.copy()

        self.play(
            FadeOut(sub_left_node),
            FadeOut(book1),
            FadeOut(sub_right_node_copy),
            FadeOut(book2_copy),
            FadeOut(right_node),
        )

        book2_explain = self.display_text("Otherwise, Don't book it")

        self.play(Write(book2_explain))
        self.wait(2)
        self.play(FadeOut(book2_explain))

        self.wait(1)
        self.outro()
        self.wait(4)
