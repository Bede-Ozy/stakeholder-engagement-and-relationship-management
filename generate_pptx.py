"""
Generate a premium, professional 16-slide PowerPoint presentation (.pptx)
for 'Stakeholder Engagement & Relationship Management in the Civil Service'.
Includes all 16 slides with executive dark navy design, cards, and full speaker notes.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    BG_DARK = RGBColor(8, 13, 26)       # #080D1A Dark Navy
    CARD_BG = RGBColor(14, 23, 42)      # #0E172A Card Navy
    CARD_BORDER = RGBColor(30, 41, 59)  # #1E293B
    TEXT_MAIN = RGBColor(248, 250, 252) # #F8FAFC White/Off-white
    TEXT_SUB = RGBColor(203, 213, 225)  # #CBD5E1 Muted Slate
    TEXT_DIM = RGBColor(148, 163, 184)  # #94A3B8
    ACCENT_BLUE = RGBColor(56, 189, 248) # #38BDF8 Sky Blue
    ACCENT_ROYAL = RGBColor(37, 99, 235) # #2563EB
    ACCENT_GOLD = RGBColor(245, 158, 11) # #F59E0B
    ACCENT_EMERALD = RGBColor(16, 185, 129)
    ACCENT_ROSE = RGBColor(244, 63, 94)

    def apply_base_slide(slide, kicker_text=None, title_text=None):
        # 1. Dark Navy Canvas Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()

        # 2. Top Accent Border (Electric Gradient simulation)
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = ACCENT_BLUE
        top_bar.line.fill.background()

        # 3. Bottom Accent Border
        bot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.42), prs.slide_width, Inches(0.08))
        bot_bar.fill.solid()
        bot_bar.fill.fore_color.rgb = ACCENT_ROYAL
        bot_bar.line.fill.background()

        # 4. Header kicker and title
        if kicker_text and title_text:
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(1.3))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

            p_kicker = tf.paragraphs[0]
            p_kicker.text = kicker_text.upper()
            p_kicker.font.size = Pt(11)
            p_kicker.font.bold = True
            p_kicker.font.color.rgb = ACCENT_BLUE
            p_kicker.space_after = Pt(4)

            p_title = tf.add_paragraph()
            p_title.text = title_text
            p_title.font.size = Pt(26)
            p_title.font.bold = True
            p_title.font.color.rgb = TEXT_MAIN

    def set_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s1)

    # Title Meta Badge
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.66), Inches(1.1), Inches(6.0), Inches(0.4))
    b1.fill.solid()
    b1.fill.fore_color.rgb = CARD_BG
    b1.line.color.rgb = ACCENT_BLUE
    tf_b1 = b1.text_frame
    p_b1 = tf_b1.paragraphs[0]
    p_b1.text = "NATIONAL PUBLIC SERVICE LEADERSHIP CONFERENCE"
    p_b1.font.size = Pt(10)
    p_b1.font.bold = True
    p_b1.font.color.rgb = ACCENT_BLUE
    p_b1.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_t = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.33), Inches(2.2))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Stakeholder Engagement & Relationship Management"
    p_t.font.size = Pt(38)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_MAIN
    p_t.alignment = PP_ALIGN.CENTER

    p_sub = tf_t.add_paragraph()
    p_sub.text = "IN THE CIVIL SERVICE"
    p_sub.font.size = Pt(20)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_BLUE
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.space_before = Pt(8)

    p_val = tf_t.add_paragraph()
    p_val.text = "Building trust. Managing relationships. Making better decisions."
    p_val.font.size = Pt(15)
    p_val.font.color.rgb = TEXT_SUB
    p_val.alignment = PP_ALIGN.CENTER
    p_val.space_before = Pt(10)

    # 4 Pillars Box
    p_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.7), Inches(10.33), Inches(0.85))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = CARD_BG
    p_box.line.color.rgb = CARD_BORDER
    tf_pb = p_box.text_frame
    p_pb = tf_pb.paragraphs[0]
    p_pb.text = "Administrative Procedures  +  Stakeholder Engagement  +  Emotional Intelligence  +  Decision Making"
    p_pb.font.size = Pt(13)
    p_pb.font.bold = True
    p_pb.font.color.rgb = TEXT_MAIN
    p_pb.alignment = PP_ALIGN.CENTER

    # Footer note
    tb_f = s1.shapes.add_textbox(Inches(1.5), Inches(6.2), Inches(10.33), Inches(0.5))
    tf_f = tb_f.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Mastering Administrative Procedures & Emotional Intelligence for Decision Making"
    p_f.font.size = Pt(11)
    p_f.font.color.rgb = TEXT_DIM
    p_f.alignment = PP_ALIGN.CENTER

    set_notes(s1, "EXECUTIVE CORE TAKEAWAY:\nSet the executive tone: stakeholder engagement is not political people-pleasing, but a rigorous public-sector administrative discipline.\n\nFACILITATOR TALKING POINTS:\n- Welcome delegates to this National Leadership Masterclass. Establish executive authority immediately.\n- Emphasize the core thesis: Good policy fails when administrators focus solely on technical brilliance while ignoring the human and institutional ecosystem.\n- Highlight the 4 foundational pillars: Administrative Procedures + Stakeholder Engagement + Emotional Intelligence + Decision Making.\n- Suggested time: 2-3 mins.")

    # ==========================================
    # SLIDE 2: THE REAL CHALLENGE
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s2, "Executive Reality", "A GOOD DECISION CAN STILL FAIL.")

    steps = [
        ("01", "Wrong people consulted"),
        ("02", "Concerns ignored"),
        ("03", "Expectations unmanaged"),
        ("04", "Communication delayed"),
        ("05", "Implementation problems")
    ]
    card_w = Inches(2.1)
    card_gap = Inches(0.3)
    start_x = Inches(0.8)

    for i, (num, text) in enumerate(steps):
        cx = start_x + i * (card_w + card_gap)
        sc = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.1), card_w, Inches(2.4))
        sc.fill.solid()
        sc.fill.fore_color.rgb = CARD_BG
        sc.line.color.rgb = ACCENT_ROSE if i == 4 else CARD_BORDER
        tf_sc = sc.text_frame
        tf_sc.word_wrap = True

        p1 = tf_sc.paragraphs[0]
        p1.text = num
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_ROSE if i == 4 else ACCENT_BLUE

        p2 = tf_sc.add_paragraph()
        p2.text = text
        p2.font.size = Pt(14)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(28)

    # Bottom Callout Box
    c_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.1), Inches(11.7), Inches(1.4))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = CARD_BG
    c_box.line.color.rgb = ACCENT_ROSE
    tf_cb = c_box.text_frame
    tf_cb.word_wrap = True

    p_cb1 = tf_cb.paragraphs[0]
    p_cb1.text = "Decision ≠ Implementation"
    p_cb1.font.size = Pt(18)
    p_cb1.font.bold = True
    p_cb1.font.color.rgb = ACCENT_ROSE

    p_cb2 = tf_cb.add_paragraph()
    p_cb2.text = "Flawless administrative intent collapses when the stakeholders tasked with execution are treated as an afterthought."
    p_cb2.font.size = Pt(12)
    p_cb2.font.color.rgb = TEXT_SUB
    p_cb2.space_before = Pt(4)

    set_notes(s2, "EXECUTIVE CORE TAKEAWAY:\nA technically sound policy without stakeholder alignment collapses at the point of execution.\n\nFACILITATOR TALKING POINTS:\n- Walk delegates through the 5 cascading failure points.\n- Give a relatable civil service example: An ERP or digital attendance policy launched without labour union consultation.\n- Emphasize: Approval in council is 10% of the journey; 90% is managing human implementation.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 3: WHO IS A STAKEHOLDER?
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s3, "Ecosystem Mapping", "Anyone Who Can Affect or Be Affected.")

    groups = [
        ("INTERNAL", "Civil servants\nManagers\nDepartments", Inches(0.8), Inches(2.0)),
        ("GOVERNMENT", "MDAs\nRegulators\nLegislators", Inches(0.8), Inches(4.5)),
        ("EXTERNAL", "Citizens\nCommunities\nBusinesses & CSOs", Inches(7.5), Inches(2.0)),
        ("IMPLEMENTERS", "Contractors\nPartners\nService providers", Inches(7.5), Inches(4.5))
    ]

    for title, items, gx, gy in groups:
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, gx, gy, Inches(5.0), Inches(2.1))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        tf = card.text_frame
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = ACCENT_BLUE

        p_desc = tf.add_paragraph()
        p_desc.text = items
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_SUB
        p_desc.space_before = Pt(6)

    set_notes(s3, "EXECUTIVE CORE TAKEAWAY:\nExpand the mental map beyond immediate hierarchical superiors to all 4 distinct quadrants of public value.\n\nFACILITATOR TALKING POINTS:\n- Challenge the narrow view that stakeholders are only ministers or permanent secretaries.\n- Highlight internal implementers: Ignoring field officers often leads to quiet departmental resistance.\n- Suggested time: 3-4 mins.")

    # ==========================================
    # SLIDE 4: ENGAGEMENT IS A SPECTRUM
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s4, "Engagement Architecture", "INFORM → CONSULT → INVOLVE → COLLABORATE")

    stages = [
        ("LEVEL 1", "INFORM", "“We're doing this.”", "Notices, gazettes, policy circulars, transparent information sharing."),
        ("LEVEL 2", "CONSULT", "“What do you think?”", "Public hearings, memorandums, citizen surveys, structured MDA feedback."),
        ("LEVEL 3", "INVOLVE", "“Let's work through it.”", "Multi-stakeholder roundtables, technical workshops, working groups."),
        ("LEVEL 4", "COLLABORATE", "“Let's build it together.”", "Joint implementation taskforces, shared accountability, co-design.")
    ]

    for i, (lvl, name, quote, desc) in enumerate(stages):
        sx = Inches(0.8) + i * Inches(2.98)
        scard = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, Inches(2.1), Inches(2.78), Inches(3.3))
        scard.fill.solid()
        scard.fill.fore_color.rgb = CARD_BG
        scard.line.color.rgb = CARD_BORDER
        tf = scard.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = lvl
        p1.font.size = Pt(10)
        p1.font.color.rgb = TEXT_DIM

        p2 = tf.add_paragraph()
        p2.text = name
        p2.font.size = Pt(17)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

        p3 = tf.add_paragraph()
        p3.text = quote
        p3.font.size = Pt(13)
        p3.font.bold = True
        p3.font.color.rgb = ACCENT_BLUE
        p3.space_before = Pt(8)

        p4 = tf.add_paragraph()
        p4.text = desc
        p4.font.size = Pt(11)
        p4.font.color.rgb = TEXT_SUB
        p4.space_before = Pt(12)

    # Banner
    b_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.8), Inches(11.7), Inches(0.9))
    b_box.fill.solid()
    b_box.fill.fore_color.rgb = CARD_BG
    b_box.line.color.rgb = ACCENT_BLUE
    tf_bb = b_box.text_frame
    p_bb = tf_bb.paragraphs[0]
    p_bb.text = "“Not every stakeholder needs the same level of engagement.”"
    p_bb.font.size = Pt(15)
    p_bb.font.bold = True
    p_bb.font.color.rgb = TEXT_MAIN
    p_bb.alignment = PP_ALIGN.CENTER

    set_notes(s4, "EXECUTIVE CORE TAKEAWAY:\nEngagement is not one-size-fits-all. Calibrate engagement levels to avoid superficial communication or bureaucratic paralysis.\n\nFACILITATOR TALKING POINTS:\n- Explain the 4 progressive levels.\n- Highlight that trying to collaborate with everybody creates gridlock, while only informing critical stakeholders breeds resistance.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 5: MAP YOUR STAKEHOLDERS (2x2 Matrix)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s5, "Strategic Prioritisation", "POWER × INTEREST MATRIX")

    quads = [
        ("HIGH POWER • LOW INTEREST", "KEEP SATISFIED", "Brief regularly, avoid surprise announcements, protect priorities.", Inches(1.5), Inches(2.0)),
        ("HIGH POWER • HIGH INTEREST", "MANAGE CLOSELY", "Key decision-makers, continuous dialogue, regular joint reviews.", Inches(7.0), Inches(2.0)),
        ("LOW POWER • LOW INTEREST", "MONITOR", "General updates, track sentiment changes, low overhead.", Inches(1.5), Inches(4.3)),
        ("LOW POWER • HIGH INTEREST", "KEEP INFORMED", "Empathetic consultation, clear updates, address operational concerns.", Inches(7.0), Inches(4.3))
    ]

    for badge, title, desc, qx, qy in quads:
        q_shape = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx, qy, Inches(5.1), Inches(1.9))
        q_shape.fill.solid()
        q_shape.fill.fore_color.rgb = CARD_BG
        q_shape.line.color.rgb = ACCENT_BLUE if "CLOSELY" in title else CARD_BORDER
        tf = q_shape.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = badge
        p1.font.size = Pt(10)
        p1.font.color.rgb = ACCENT_BLUE if "CLOSELY" in title else TEXT_DIM

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(18)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_SUB
        p3.space_before = Pt(4)

    set_notes(s5, "EXECUTIVE CORE TAKEAWAY:\nMap stakeholders systematically before committing time, political capital, and public resources.\n\nFACILITATOR TALKING POINTS:\n- Walk delegates through the 4 quadrants: Keep Satisfied, Manage Closely, Monitor, Keep Informed.\n- Golden rule before engaging: Who matters? Why do they matter? What do they need?\n- Suggested time: 4 mins.")

    # ==========================================
    # SLIDE 6: DON'T STOP AT POSITIONS
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s6, "Negotiation & Alignment", "POSITION ≠ INTEREST")

    tiers = [
        ("SURFACE POSITION", "“I DON'T SUPPORT THIS POLICY.”", "What is stated publicly", ACCENT_ROSE, Inches(2.0), Inches(10.0)),
        ("OPERATIONAL CONCERN", "“My department will carry the implementation risk.”", "The anxiety beneath the resistance", ACCENT_GOLD, Inches(3.3), Inches(8.5)),
        ("UNDERLYING NEED", "Clarity  •  Resources  •  Accountability", "Where collaborative solutions are built", ACCENT_EMERALD, Inches(4.6), Inches(7.0))
    ]

    for tag, dialog, note, col, ty, tw in tiers:
        tx = (prs.slide_width - tw) / 2
        f_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, tx, ty, tw, Inches(1.0))
        f_box.fill.solid()
        f_box.fill.fore_color.rgb = CARD_BG
        f_box.line.color.rgb = col
        tf = f_box.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"{tag}: {dialog}"
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN

        p2 = tf.add_paragraph()
        p2.text = note
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_DIM

    # Bottom
    b_fun = s6.shapes.add_textbox(Inches(1.0), Inches(5.9), Inches(11.33), Inches(0.9))
    tf_bf = b_fun.text_frame
    p_bf1 = tf_bf.paragraphs[0]
    p_bf1.text = "Listen beneath the words."
    p_bf1.font.size = Pt(18)
    p_bf1.font.bold = True
    p_bf1.font.color.rgb = ACCENT_BLUE
    p_bf1.alignment = PP_ALIGN.CENTER

    p_bf2 = tf_bf.add_paragraph()
    p_bf2.text = "Positions create deadlock. Understanding underlying interests reveals administrative pathways forward."
    p_bf2.font.size = Pt(12)
    p_bf2.font.color.rgb = TEXT_SUB
    p_bf2.alignment = PP_ALIGN.CENTER

    set_notes(s6, "EXECUTIVE CORE TAKEAWAY:\nPositions polarize; underlying interests create the bridge for lawful administrative compromise.\n\nFACILITATOR TALKING POINTS:\n- Harvard Negotiation Project core insight: Position is what people say; Interest is WHY.\n- When a director objects, probe for the underlying institutional risk.\n- Suggested time: 3-4 mins.")

    # ==========================================
    # SLIDE 7: WHERE EMOTIONAL INTELLIGENCE ENTERS
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s7, "Leadership Maturity", "MANAGE YOURSELF BEFORE MANAGING THE ROOM.")

    ei_steps = [
        ("1", "SELF-AWARENESS", "Recognise personal emotional triggers and defensiveness."),
        ("2", "SELF-CONTROL", "Maintain procedural calm under political tension."),
        ("3", "EMPATHY", "Accurately understand the stakeholder's institutional pressures."),
        ("4", "SOCIAL AWARENESS", "Read power hierarchies and informal networks."),
        ("5", "RELATIONSHIP MGMT", "Steer complex discussions toward lawful public value.")
    ]

    for i, (num, title, desc) in enumerate(ei_steps):
        ex = Inches(0.8) + i * Inches(2.38)
        ec = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ex, Inches(2.2), Inches(2.2), Inches(3.2))
        ec.fill.solid()
        ec.fill.fore_color.rgb = CARD_BG
        ec.line.color.rgb = CARD_BORDER
        tf = ec.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = num
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_BLUE

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_SUB
        p3.space_before = Pt(8)

    # Bottom
    b_ei = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.8), Inches(11.7), Inches(0.8))
    b_ei.fill.solid()
    b_ei.fill.fore_color.rgb = CARD_BG
    b_ei.line.color.rgb = ACCENT_BLUE
    tf_bei = b_ei.text_frame
    p_bei = tf_bei.paragraphs[0]
    p_bei.text = "Emotionally intelligent ≠ agreeing with everyone."
    p_bei.font.size = Pt(16)
    p_bei.font.bold = True
    p_bei.font.color.rgb = TEXT_MAIN
    p_bei.alignment = PP_ALIGN.CENTER

    set_notes(s7, "EXECUTIVE CORE TAKEAWAY:\nEmotional intelligence in the civil service is not weakness—it is strategic self-control and situational mastery.\n\nFACILITATOR TALKING POINTS:\n- Daniel Goleman 5-domain framework: Self-awareness -> Self-control -> Empathy -> Social awareness -> Relationship management.\n- If an administrator reacts defensively to criticism, they lose control of the room.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 8: THE POWER OF ACTIVE LISTENING
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s8, "Administrative Dialogue", "LISTEN → CLARIFY → REFLECT → RESPOND")

    al_stages = [
        ("STEP 1", "LISTEN", "Hear without interrupting or formulating defensive rebuttals."),
        ("STEP 2", "CLARIFY", "Ask diagnostic questions to unpack technical or budgetary ambiguities."),
        ("STEP 3", "REFLECT", "Restate their core concerns to confirm accurate shared understanding."),
        ("STEP 4", "RESPOND", "Present a reasoned administrative position anchored in procedure.")
    ]

    for i, (step, title, desc) in enumerate(al_stages):
        ax = Inches(0.8) + i * Inches(2.98)
        ac = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ax, Inches(2.0), Inches(2.78), Inches(1.8))
        ac.fill.solid()
        ac.fill.fore_color.rgb = CARD_BG
        ac.line.color.rgb = CARD_BORDER
        tf = ac.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = step
        p1.font.size = Pt(10)
        p1.font.color.rgb = ACCENT_BLUE

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(15)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_SUB
        p3.space_before = Pt(4)

    # Contrast box
    c_box8 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.2), Inches(11.7), Inches(1.5))
    c_box8.fill.solid()
    c_box8.fill.fore_color.rgb = CARD_BG
    c_box8.line.color.rgb = CARD_BORDER
    tf_c8 = c_box8.text_frame
    tf_c8.word_wrap = True

    p_w = tf_c8.paragraphs[0]
    p_w.text = "INSTEAD OF: “That's not possible.” (Shuts down dialogue, breeds cynicism)"
    p_w.font.size = Pt(12)
    p_w.font.color.rgb = ACCENT_ROSE

    p_r = tf_c8.add_paragraph()
    p_r.text = "USE: “What specifically concerns you about the proposal?” (Reveals actionable obstacles)"
    p_r.font.size = Pt(13)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_EMERALD
    p_r.space_before = Pt(8)

    # Bottom Triad
    tb_triad = s8.shapes.add_textbox(Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.5))
    tf_tr = tb_triad.text_frame
    p_tr = tf_tr.paragraphs[0]
    p_tr.text = "Listen for: What they say  •  What they mean  •  What they need"
    p_tr.font.size = Pt(14)
    p_tr.font.bold = True
    p_tr.font.color.rgb = ACCENT_BLUE
    p_tr.alignment = PP_ALIGN.CENTER

    set_notes(s8, "EXECUTIVE CORE TAKEAWAY:\nActive listening is an intelligence-gathering tool, not an act of submission.\n\nFACILITATOR TALKING POINTS:\n- Detail the 4-step listening cadence.\n- Train leaders to avoid 'That's not possible' reflex.\n- Listen on 3 frequencies: words, emotion, institutional need.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 9: WHEN STAKEHOLDERS BECOME DIFFICULT
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s9, "Conflict De-escalation", "DON'T LABEL. DIAGNOSE.")

    diff_types = [
        ("ANGRY", "→ De-escalate", "Lower vocal pitch, validate frustration without admitting liability.", ACCENT_ROSE),
        ("RESISTANT", "→ Understand concern", "Probe for past institutional letdowns or loss of departmental turf.", ACCENT_GOLD),
        ("SILENT", "→ Create space", "Invite structured offline input, protect junior officers from pressure.", TEXT_SUB),
        ("DOMINANT", "→ Structure talk", "Enforce meeting standing orders, implement strict time allocations.", ACCENT_ROYAL),
        ("UNREASONABLE", "→ Set boundaries", "Anchor firmly on Public Service Rules, statutory mandates, and legal remits.", ACCENT_ROSE)
    ]

    for i, (badge, action, detail, col) in enumerate(diff_types):
        dx = Inches(0.8) + i * Inches(2.38)
        dc = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, dx, Inches(2.1), Inches(2.2), Inches(3.4))
        dc.fill.solid()
        dc.fill.fore_color.rgb = CARD_BG
        dc.line.color.rgb = CARD_BORDER
        tf = dc.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = badge
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = action
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = detail
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_SUB
        p3.space_before = Pt(8)

    # Bottom
    b_diff = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.8))
    b_diff.fill.solid()
    b_diff.fill.fore_color.rgb = CARD_BG
    b_diff.line.color.rgb = ACCENT_BLUE
    tf_bd = b_diff.text_frame
    p_bd = tf_bd.paragraphs[0]
    p_bd.text = "Don't match emotional intensity with emotional intensity."
    p_bd.font.size = Pt(16)
    p_bd.font.bold = True
    p_bd.font.color.rgb = TEXT_MAIN
    p_bd.alignment = PP_ALIGN.CENTER

    set_notes(s9, "EXECUTIVE CORE TAKEAWAY:\nDo not personalize friction. Diagnose the archetype and apply the corresponding administrative antidote.\n\nFACILITATOR TALKING POINTS:\n- Walk delegates through the 5 tactical archetypes.\n- Deliver the key rule: Never match emotional intensity with emotional intensity.\n- Suggested time: 4 mins.")

    # ==========================================
    # SLIDE 10: MANAGING DISAGREEMENT
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s10, "Constructive Deliberation", "MOVE FROM POSITIONS → INTERESTS")

    stairs = [
        ("STEP 1", "“NO.”", "Positional Defense"),
        ("STEP 2", "“WHY?”", "Curious Diagnostic Inquiry"),
        ("STEP 3", "“WHAT CONCERNS YOU?”", "Unpacking Underlying Risk"),
        ("STEP 4", "“WHAT WOULD ADDRESS THAT CONCERN?”", "Co-Creating the Administrative Solution")
    ]

    for i, (st, speech, note) in enumerate(stairs):
        sx = Inches(0.8) + i * Inches(2.98)
        sc = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, Inches(2.2), Inches(2.78), Inches(2.8))
        sc.fill.solid()
        sc.fill.fore_color.rgb = CARD_BG
        sc.line.color.rgb = CARD_BORDER
        tf = sc.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = st
        p1.font.size = Pt(10)
        p1.font.color.rgb = ACCENT_BLUE

        p2 = tf.add_paragraph()
        p2.text = speech
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_SUB
        p3.space_before = Pt(8)

    # Bottom
    b_dis = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.1))
    b_dis.fill.solid()
    b_dis.fill.fore_color.rgb = CARD_BG
    b_dis.line.color.rgb = CARD_BORDER
    tf_bdis = b_dis.text_frame
    p_bdis = tf_bdis.paragraphs[0]
    p_bdis.text = "The goal isn't to eliminate disagreement.  |  Make disagreement productive."
    p_bdis.font.size = Pt(16)
    p_bdis.font.bold = True
    p_bdis.font.color.rgb = TEXT_MAIN
    p_bdis.alignment = PP_ALIGN.CENTER

    set_notes(s10, "EXECUTIVE CORE TAKEAWAY:\nDisagreement is evidence of diverse institutional stakes. The goal is to make disagreement productive.\n\nFACILITATOR TALKING POINTS:\n- Demonstrate the inquiry ladder: No -> Why -> What Concerns You -> What Would Address That.\n- Co-created solutions drastically increase implementation compliance.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 11: STAKEHOLDERS & DECISION MAKING
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s11, "Decision-Making Filter", "BEFORE YOU DECIDE, ASK:")

    questions = [
        ("WHO?", "Who will be affected?", "Direct, indirect, and vulnerable groups.", Inches(0.8), Inches(2.0)),
        ("WHY?", "What are their interests?", "Motivations, priorities, citizen stakes.", Inches(4.8), Inches(2.0)),
        ("WHAT?", "What evidence do we have?", "Data, metrics, administrative precedents.", Inches(8.8), Inches(2.0)),
        ("RISK?", "What could go wrong?", "Operational bottlenecks, political fallout.", Inches(0.8), Inches(3.8)),
        ("RULES?", "What does procedure require?", "Public Service Rules, procurement laws.", Inches(4.8), Inches(3.8)),
        ("IMPLEMENTATION?", "Can this actually work?", "Budgetary backing, field-level practicality.", Inches(8.8), Inches(3.8))
    ]

    for tag, q, note, qx, qy in questions:
        card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx, qy, Inches(3.7), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        tf = card.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = tag
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_BLUE

        p2 = tf.add_paragraph()
        p2.text = q
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_DIM

    # Bottom
    b_conv = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.8), Inches(11.7), Inches(0.9))
    b_conv.fill.solid()
    b_conv.fill.fore_color.rgb = CARD_BG
    b_conv.line.color.rgb = ACCENT_BLUE
    tf_bc = b_conv.text_frame
    p_bc = tf_bc.paragraphs[0]
    p_bc.text = "BETTER DECISION: Legitimate • Implementable • Sustainable"
    p_bc.font.size = Pt(16)
    p_bc.font.bold = True
    p_bc.font.color.rgb = ACCENT_BLUE
    p_bc.alignment = PP_ALIGN.CENTER

    set_notes(s11, "EXECUTIVE CORE TAKEAWAY:\nRun every policy, project, and circular through the 6-question diagnostic filter before final approval.\n\nFACILITATOR TALKING POINTS:\n- Review the 6 diagnostic questions.\n- Show how they converge into a sustainable, lawful decision.\n- Suggested time: 3-4 mins.")

    # ==========================================
    # SLIDE 12: THE TRUST EQUATION
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s12, "Institutional Currency", "THE TRUST EQUATION")

    eq_terms = [
        ("COMPETENCE", "Technical delivery"),
        ("FAIRNESS", "Impartiality & equity"),
        ("TRANSPARENCY", "Open rules & rationale"),
        ("RESPONSIVENESS", "Timely action"),
        ("CONSISTENCY", "Reliability over time")
    ]

    for i, (term, sub) in enumerate(eq_terms):
        tx = Inches(0.8) + i * Inches(2.0)
        t_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, tx, Inches(2.4), Inches(1.7), Inches(1.8))
        t_card.fill.solid()
        t_card.fill.fore_color.rgb = CARD_BG
        t_card.line.color.rgb = CARD_BORDER
        tf = t_card.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = term
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.size = Pt(9)
        p2.font.color.rgb = TEXT_DIM
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(6)

    # Equals Trust Box
    eq_res = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.8), Inches(2.3), Inches(1.7), Inches(2.0))
    eq_res.fill.solid()
    eq_res.fill.fore_color.rgb = CARD_BG
    eq_res.line.color.rgb = ACCENT_GOLD
    tf_res = eq_res.text_frame
    p_r1 = tf_res.paragraphs[0]
    p_r1.text = "OUTCOME"
    p_r1.font.size = Pt(10)
    p_r1.font.color.rgb = ACCENT_GOLD
    p_r1.alignment = PP_ALIGN.CENTER

    p_r2 = tf_res.add_paragraph()
    p_r2.text = "TRUST"
    p_r2.font.size = Pt(24)
    p_r2.font.bold = True
    p_r2.font.color.rgb = TEXT_MAIN
    p_r2.alignment = PP_ALIGN.CENTER
    p_r2.space_before = Pt(8)

    # Bottom
    b_tr = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.1))
    b_tr.fill.solid()
    b_tr.fill.fore_color.rgb = CARD_BG
    b_tr.line.color.rgb = CARD_BORDER
    tf_btr = b_tr.text_frame
    p_btr = tf_btr.paragraphs[0]
    p_btr.text = "Every interaction either builds trust or erodes trust."
    p_btr.font.size = Pt(18)
    p_btr.font.bold = True
    p_btr.font.color.rgb = TEXT_MAIN
    p_btr.alignment = PP_ALIGN.CENTER

    set_notes(s12, "EXECUTIVE CORE TAKEAWAY:\nPublic sector trust is a multiplicative equation—if any single component is zero, total trust collapses.\n\nFACILITATOR TALKING POINTS:\n- Explain the mathematical reality: Competence * Fairness * Transparency * Responsiveness * Consistency = TRUST.\n- If transparency or fairness is zero, overall public trust is zero.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 13: THE NIGERIAN CIVIL SERVICE CONTEXT
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s13, "Institutional Foundations", "ENGAGEMENT IS PART OF GOOD PUBLIC SERVICE.")

    # Left: PSR
    psr_box = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.0), Inches(5.6), Inches(3.6))
    psr_box.fill.solid()
    psr_box.fill.fore_color.rgb = CARD_BG
    psr_box.line.color.rgb = CARD_BORDER
    tf_psr = psr_box.text_frame
    tf_psr.word_wrap = True

    p_psr_h = tf_psr.paragraphs[0]
    p_psr_h.text = "PUBLIC SERVICE RULES (OHCSF)"
    p_psr_h.font.size = Pt(15)
    p_psr_h.font.bold = True
    p_psr_h.font.color.rgb = ACCENT_BLUE

    psr_points = [
        "Efficiency — Minimising procedural friction and delay",
        "Effectiveness — Delivering tangible public sector outcomes",
        "Performance — Measuring delivery against national mandates",
        "Due Process — Strict fidelity to legal standards",
        "Probity — Uncompromising ethics and public integrity"
    ]
    for pt in psr_points:
        p_pt = tf_psr.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = TEXT_SUB
        p_pt.space_before = Pt(6)

    # Right: SERVICOM
    ser_box = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(2.0), Inches(5.6), Inches(3.6))
    ser_box.fill.solid()
    ser_box.fill.fore_color.rgb = CARD_BG
    ser_box.line.color.rgb = CARD_BORDER
    tf_ser = ser_box.text_frame
    tf_ser.word_wrap = True

    p_ser_h = tf_ser.paragraphs[0]
    p_ser_h.text = "SERVICOM CITIZEN COMPACT"
    p_ser_h.font.size = Pt(15)
    p_ser_h.font.bold = True
    p_ser_h.font.color.rgb = ACCENT_EMERALD

    ser_points = [
        "Service Standards — Clear published commitments",
        "Citizen Expectations — Aligning delivery to public needs",
        "Complaints — Robust grievance redress mechanisms",
        "Feedback — Systematic data informing reform",
        "Service Improvement — Continuous MDA modernization"
    ]
    for pt in ser_points:
        p_pt = tf_ser.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = TEXT_SUB
        p_pt.space_before = Pt(6)

    # Bottom
    b_psr = s13.shapes.add_textbox(Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.7))
    tf_bpsr = b_psr.text_frame
    p_bpsr = tf_bpsr.paragraphs[0]
    p_bpsr.text = "“Good administration must work for people, not only on paper.”\nSources: OHCSF Public Service Rules; SERVICOM"
    p_bpsr.font.size = Pt(12)
    p_bpsr.font.bold = True
    p_bpsr.font.color.rgb = TEXT_MAIN
    p_bpsr.alignment = PP_ALIGN.CENTER

    set_notes(s13, "EXECUTIVE CORE TAKEAWAY:\nStakeholder engagement is not an imported novelty; it is enshrined in our Public Service Rules and SERVICOM Charters.\n\nFACILITATOR TALKING POINTS:\n- Highlight the OHCSF Public Service Rules pillars on the left.\n- Connect directly to the SERVICOM citizen charter principles on the right.\n- Rules without empathy produce bureaucratic stagnation; empathy without rules produces chaos.\n- Suggested time: 4 mins.")

    # ==========================================
    # SLIDE 14: THE 5R MODEL (SIGNATURE PLAYBOOK)
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s14, "Signature Playbook", "THE 5R MODEL: A Practical Stakeholder Management Playbook")

    r_steps = [
        ("R1", "RECOGNISE", "Who matters?", "Identify statutory authorities, informal power brokers, and silent groups."),
        ("R2", "READ", "What do they need?", "Decode hidden departmental risks and underlying interests."),
        ("R3", "RELATE", "How build trust?", "Deploy emotional intelligence, active listening, and procedural fairness."),
        ("R4", "RESPOND", "How engage & decide?", "Synthesize evidence, adhere to rules, and articulate balanced trade-offs."),
        ("R5", "REVIEW", "What did we learn?", "Assess implementation impact and close the feedback loop.")
    ]

    for i, (r_num, r_name, r_q, r_desc) in enumerate(r_steps):
        rx = Inches(0.8) + i * Inches(2.38)
        rc = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(2.2), Inches(2.2), Inches(3.3))
        rc.fill.solid()
        rc.fill.fore_color.rgb = CARD_BG
        rc.line.color.rgb = ACCENT_GOLD
        tf = rc.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = r_num
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_GOLD

        p2 = tf.add_paragraph()
        p2.text = r_name
        p2.font.size = Pt(15)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

        p3 = tf.add_paragraph()
        p3.text = r_q
        p3.font.size = Pt(11)
        p3.font.bold = True
        p3.font.color.rgb = ACCENT_BLUE
        p3.space_before = Pt(6)

        p4 = tf.add_paragraph()
        p4.text = r_desc
        p4.font.size = Pt(9)
        p4.font.color.rgb = TEXT_SUB
        p4.space_before = Pt(8)

    # Track banner
    b_5r = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.8))
    b_5r.fill.solid()
    b_5r.fill.fore_color.rgb = CARD_BG
    b_5r.line.color.rgb = ACCENT_GOLD
    tf_5r = b_5r.text_frame
    p_5r = tf_5r.paragraphs[0]
    p_5r.text = "RECOGNISE → READ → RELATE → RESPOND → REVIEW"
    p_5r.font.size = Pt(15)
    p_5r.font.bold = True
    p_5r.font.color.rgb = TEXT_MAIN
    p_5r.alignment = PP_ALIGN.CENTER

    set_notes(s14, "EXECUTIVE CORE TAKEAWAY:\nThe 5R Model is your practical, repeatable 5-step operational playbook for every project and reform.\n\nFACILITATOR TALKING POINTS:\n- This is the signature framework of the masterclass.\n- Walk delegates through each R: Recognise, Read, Relate, Respond, Review.\n- Encourage delegates to institutionalize the 5R rhythm in their departments.\n- Suggested time: 4-5 mins.")

    # ==========================================
    # SLIDE 15: FROM ENGAGEMENT TO ACTION
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s15, "Closing The Loop", "AFTER THE MEETING, CLOSE THE LOOP.")

    # 5 Stages
    c_stages = [
        ("01", "LISTEN", "Capture concerns"),
        ("02", "DECIDE", "Apply rules & judgment"),
        ("03", "COMMUNICATE", "Share the reasoning"),
        ("04", "ACT", "Execute agreed steps"),
        ("05", "FOLLOW UP", "Report progress back")
    ]

    for i, (num, name, desc) in enumerate(c_stages):
        cx = Inches(0.8) + i * Inches(2.38)
        cc = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.0), Inches(2.2), Inches(1.6))
        cc.fill.solid()
        cc.fill.fore_color.rgb = CARD_BG
        cc.line.color.rgb = CARD_BORDER
        tf = cc.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = num
        p1.font.size = Pt(10)
        p1.font.color.rgb = ACCENT_BLUE

        p2 = tf.add_paragraph()
        p2.text = name
        p2.font.size = Pt(14)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(9)
        p3.font.color.rgb = TEXT_DIM

    # Core message
    m_box = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.0), Inches(11.7), Inches(1.8))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = CARD_BG
    m_box.line.color.rgb = ACCENT_BLUE
    tf_mb = m_box.text_frame
    tf_mb.word_wrap = True

    p_mbh = tf_mb.paragraphs[0]
    p_mbh.text = "Tell stakeholders:"
    p_mbh.font.size = Pt(13)
    p_mbh.font.bold = True
    p_mbh.font.color.rgb = TEXT_DIM

    p_mb_items = tf_mb.add_paragraph()
    p_mb_items.text = "WHAT was decided    |    WHY it was decided    |    WHAT happens next"
    p_mb_items.font.size = Pt(17)
    p_mb_items.font.bold = True
    p_mb_items.font.color.rgb = ACCENT_BLUE
    p_mb_items.space_before = Pt(8)

    # Bottom
    b_lp = s15.shapes.add_textbox(Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.5))
    tf_lp = b_lp.text_frame
    p_lp = tf_lp.paragraphs[0]
    p_lp.text = "Stakeholder engagement is a continuous institutional discipline, not a one-time meeting."
    p_lp.font.size = Pt(12)
    p_lp.font.color.rgb = TEXT_SUB
    p_lp.alignment = PP_ALIGN.CENTER

    set_notes(s15, "EXECUTIVE CORE TAKEAWAY:\nThe most damaging administrative mistake is holding a consultation and then disappearing into institutional silence.\n\nFACILITATOR TALKING POINTS:\n- Explain the 3 essential communication updates: WHAT, WHY, WHAT NEXT.\n- Explaining the rationale preserves relationships even when an outcome is unfavorable.\n- Engagement is continuous, not episodic.\n- Suggested time: 3 mins.")

    # ==========================================
    # SLIDE 16: CLOSING MANIFESTO
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s16)

    # Hero Quote
    tb_c = s16.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.33), Inches(1.2))
    tf_c = tb_c.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = "PEOPLE SUPPORT WHAT THEY UNDERSTAND."
    p_c.font.size = Pt(30)
    p_c.font.bold = True
    p_c.font.color.rgb = TEXT_MAIN
    p_c.alignment = PP_ALIGN.CENTER

    # 4 Words Row
    w_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.0), Inches(2.2), Inches(9.33), Inches(0.75))
    w_box.fill.solid()
    w_box.fill.fore_color.rgb = CARD_BG
    w_box.line.color.rgb = CARD_BORDER
    tf_w = w_box.text_frame
    p_w = tf_w.paragraphs[0]
    p_w.text = "HEARD   •   RESPECTED   •   FAIRLY TREATED   •   INFORMED"
    p_w.font.size = Pt(13)
    p_w.font.bold = True
    p_w.font.color.rgb = ACCENT_EMERALD
    p_w.alignment = PP_ALIGN.CENTER

    # Manifesto Lines
    tb_m = s16.shapes.add_textbox(Inches(1.0), Inches(3.2), Inches(11.33), Inches(2.5))
    tf_m = tb_m.text_frame
    manifesto = [
        "ENGAGE PEOPLE.",
        "UNDERSTAND INTERESTS.",
        "MANAGE EMOTIONS.",
        "RESPECT PROCEDURE.",
        "MAKE BETTER DECISIONS."
    ]
    for i, line in enumerate(manifesto):
        p_m = tf_m.paragraphs[0] if i == 0 else tf_m.add_paragraph()
        p_m.text = line
        p_m.font.size = Pt(18 if i < 4 else 22)
        p_m.font.bold = True
        p_m.font.color.rgb = ACCENT_BLUE if i == 4 else TEXT_SUB
        p_m.alignment = PP_ALIGN.CENTER
        if i > 0:
            p_m.space_before = Pt(4)

    # Thank you
    tb_th = s16.shapes.add_textbox(Inches(1.0), Inches(6.0), Inches(11.33), Inches(0.8))
    tf_th = tb_th.text_frame
    p_th = tf_th.paragraphs[0]
    p_th.text = "Thank You\nQuestions, Reflections & Leadership Discussion"
    p_th.font.size = Pt(13)
    p_th.font.bold = True
    p_th.font.color.rgb = TEXT_DIM
    p_th.alignment = PP_ALIGN.CENTER

    set_notes(s16, "EXECUTIVE CORE TAKEAWAY:\nSummarize the masterclass into a memorable, inspiring executive leadership charge.\n\nFACILITATOR TALKING POINTS:\n- Reiterate the 4 conditions: Heard, Respected, Fairly Treated, Informed.\n- Deliver the closing manifesto with conviction:\n  • ENGAGE PEOPLE.\n  • UNDERSTAND INTERESTS.\n  • MANAGE EMOTIONS.\n  • RESPECT PROCEDURE.\n  • MAKE BETTER DECISIONS.\n- Open the floor for executive Q&A and discussion.\n- Suggested time: 2-3 mins.")

    output_path = "stakeholder_engagement_masterclass.pptx"
    prs.save(output_path)
    print(f"Successfully generated {output_path} with all 16 slides!")

if __name__ == "__main__":
    create_deck()
