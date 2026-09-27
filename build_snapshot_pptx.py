"""
Build pixel-perfect snapshot PowerPoint presentations (.pptx)
for both Dark and Light themes using high-resolution live slide snapshots.
Embeds full-bleed 16:9 snapshots and attaches comprehensive speaker notes to every slide.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Speaker Notes Registry
SPEAKER_NOTES = [
    # Slide 1
    """EXECUTIVE CORE TAKEAWAY:
Set the executive tone: stakeholder engagement is not political people-pleasing, but a rigorous public-sector administrative discipline.

FACILITATOR TALKING POINTS:
- Facilitator & Lead Speaker: Mr Abayomi Oladipupo Lateef.
- Welcome delegates to this National Leadership Masterclass. Establish executive authority immediately.
- Emphasize the core thesis: Good policy fails when administrators focus solely on technical brilliance while ignoring the human and institutional ecosystem.
- Highlight the 4 foundational pillars: Administrative Procedures + Stakeholder Engagement + Emotional Intelligence + Decision Making.
- Frame the conference objective: equipping directors, permanent secretaries, and administrators with a repeatable playbook for durable governance.
- Suggested time: 2-3 mins.""",

    # Slide 2
    """EXECUTIVE CORE TAKEAWAY:
A technically sound policy without stakeholder alignment collapses at the point of execution.

FACILITATOR TALKING POINTS:
- Walk the audience through the 5 cascading failure points: Wrong people consulted → Concerns ignored → Expectations unmanaged → Communication delayed → Implementation failure.
- Give a relatable civil service example: A digital attendance or ERP rollout launched without engaging labour unions or departmental desk officers.
- Stress the bottom callout: 'Decision ≠ Implementation'. Approval in council or internal memo is just 10% of the journey; 90% is managing the human transition.
- Suggested time: 3 mins.""",

    # Slide 3
    """EXECUTIVE CORE TAKEAWAY:
Expand the mental map beyond immediate hierarchical superiors to all 4 distinct quadrants of public value.

FACILITATOR TALKING POINTS:
- Challenge the traditional narrow view: A stakeholder is anyone who can affect the outcome OR who will be affected by the outcome.
- Break down the 4 groups: Internal (civil servants/managers), Government (sister MDAs/regulators/legislators), External (citizens/communities/CSOs), and Implementers (contractors/partners).
- Point out the dangerous blindspot: Ignoring internal implementers often leads to quiet departmental sabotage.
- Suggested time: 3-4 mins.""",

    # Slide 4
    """EXECUTIVE CORE TAKEAWAY:
Engagement is not one-size-fits-all. Calibrate engagement levels to avoid either superficial communication or bureaucratic paralysis.

FACILITATOR TALKING POINTS:
- Explain the 4 levels: Inform (one-way announcements), Consult (seeking feedback), Involve (working together on options), Collaborate (joint partnership and co-design).
- Quote: 'Not every stakeholder needs the same level of engagement.'
- Trying to collaborate with everyone causes endless committee gridlock; only informing critical power players causes revolt.
- Suggested time: 3 mins.""",

    # Slide 5
    """EXECUTIVE CORE TAKEAWAY:
Map stakeholders systematically before committing time, political capital, and public resources.

FACILITATOR TALKING POINTS:
- Explain the 2x2 grid: Y-axis represents Power/Influence; X-axis represents Interest/Vulnerability.
- Quadrant 1 (High Power / High Interest): Manage Closely. Key ministers, permanent secretaries.
- Quadrant 2 (High Power / Low Interest): Keep Satisfied. Central regulators, Treasury.
- Quadrant 3 (Low Power / High Interest): Keep Informed. Frontline staff, affected citizens.
- Quadrant 4 (Low Power / Low Interest): Monitor. Low overhead.
- Golden rule before engaging: Who matters? Why do they matter? What do they need?
- Suggested time: 4 mins.""",

    # Slide 6
    """EXECUTIVE CORE TAKEAWAY:
Positions polarize; underlying interests create the bridge for lawful administrative compromise.

FACILITATOR TALKING POINTS:
- Introduce the Harvard Negotiation Project principle: Position is what people say they want; Interest is WHY they want it.
- Walk through the funnel diagram: When a Director objects, don't argue with the statement. Ask WHY.
- Target the true underlying needs: Clarity, Resources, Accountability. When you solve the underlying interest, resistance evaporates.
- Suggested time: 3-4 mins.""",

    # Slide 7
    """EXECUTIVE CORE TAKEAWAY:
Emotional intelligence in the civil service is not weakness—it is strategic self-control and situational mastery.

FACILITATOR TALKING POINTS:
- Present the 5 sequential stages: Self-awareness → Self-control → Empathy → Social awareness → Relationship management.
- Key phrase: 'Manage yourself before managing the room.' If an administrator reacts defensively, they surrender control of the meeting.
- Emphasize: 'Emotionally intelligent ≠ agreeing with everyone.' It means understanding their emotions so you can uphold public interest firmly without creating unnecessary enemies.
- Suggested time: 3 mins.""",

    # Slide 8
    """EXECUTIVE CORE TAKEAWAY:
Active listening is an intelligence-gathering tool, not an act of submission.

FACILITATOR TALKING POINTS:
- Detail the 4-step cadence: Listen without interrupting → Clarify ambiguous terms → Reflect their core fear back → Respond with reasoned procedural facts.
- Highlight the contrast box: Instead of the bureaucratic reflex 'That's not possible!', train teams to say: 'What specifically concerns you about the proposal?'
- Always listen on 3 frequencies: What they say, What they mean, and What they need.
- Suggested time: 3 mins.""",

    # Slide 9
    """EXECUTIVE CORE TAKEAWAY:
Do not personalize friction. Diagnose the archetype and apply the corresponding administrative antidote.

FACILITATOR TALKING POINTS:
- Walk through the 5 tactical cards: Angry (de-escalate), Resistant (uncover past broken promises), Silent (create safe channels), Dominant (enforce meeting standing orders), Unreasonable (anchor on statutory rules).
- Deliver the key rule: 'Don't match emotional intensity with emotional intensity.'
- Suggested time: 4 mins.""",

    # Slide 10
    """EXECUTIVE CORE TAKEAWAY:
Disagreement is evidence of diverse institutional stakes. The goal is to make disagreement productive.

FACILITATOR TALKING POINTS:
- Demonstrate the inquiry ladder: Turn a rigid 'NO' into curiosity by asking 'WHY?', pinpointing 'WHAT CONCERNS YOU?', and concluding with 'WHAT WOULD ADDRESS THAT CONCERN?'.
- When stakeholders participate in crafting the solution, their commitment to implementation skyrockets.
- Groupthink in MDAs leads to disastrous policies. Welcoming constructive pushback protects the government.
- Suggested time: 3 mins.""",

    # Slide 11
    """EXECUTIVE CORE TAKEAWAY:
Run every policy, project, and circular through the 6-question diagnostic filter before final approval.

FACILITATOR TALKING POINTS:
- Review the 6 convergence questions: WHO will be affected? WHY? WHAT evidence? RISK? RULES? IMPLEMENTATION?
- Show how these 6 inputs converge into a 'BETTER DECISION' that is legitimate, lawful, sustainable, and workable.
- Suggested time: 3-4 mins.""",

    # Slide 12
    """EXECUTIVE CORE TAKEAWAY:
Public sector trust is a multiplicative equation—if any single component is zero, total trust collapses.

FACILITATOR TALKING POINTS:
- Explain the formula: Competence x Fairness x Transparency x Responsiveness x Consistency = TRUST.
- Demonstrate the mathematics: You can have high technical competence, but if your transparency is zero, public trust is zero.
- Bottom maxim: 'Every interaction either builds trust or erodes trust.'
- Suggested time: 3 mins.""",

    # Slide 13
    """EXECUTIVE CORE TAKEAWAY:
Stakeholder engagement is not an imported novelty; it is enshrined in our Public Service Rules and SERVICOM Charters.

FACILITATOR TALKING POINTS:
- Left Column: Highlight OHCSF Federal Public Service Rules principles—Efficiency, Effectiveness, Performance, Due Process, and Probity.
- Right Column: Connect directly to the SERVICOM mandate—published Service Standards, Citizen Expectations, Complaints Redress, and Feedback loops.
- Punchline: 'Good administration must work for people, not only on paper.'
- Suggested time: 4 mins.""",

    # Slide 14
    """EXECUTIVE CORE TAKEAWAY:
The 5R Model is your practical, repeatable 5-step operational playbook for every project and reform.

FACILITATOR TALKING POINTS:
- Centerpiece takeaway: 1. RECOGNISE (Who matters?), 2. READ (What do they need?), 3. RELATE (How build trust?), 4. RESPOND (How engage & decide?), 5. REVIEW (What did we learn?).
- Invite delegates to memorize the rhythm: RECOGNISE → READ → RELATE → RESPOND → REVIEW.
- Suggested time: 4-5 mins.""",

    # Slide 15
    """EXECUTIVE CORE TAKEAWAY:
The most damaging administrative mistake is holding a consultation and then disappearing into institutional silence.

FACILITATOR TALKING POINTS:
- Follow the 5-stage loop: Listen → Decide → Communicate → Act → Follow up.
- Emphasize the 3 non-negotiable updates: WHAT was decided, WHY it was decided, and WHAT happens next.
- Explaining the rationale preserves relationships even when an outcome is unfavorable.
- Suggested time: 3 mins.""",

    # Slide 16
    """EXECUTIVE CORE TAKEAWAY:
Summarize the masterclass into a memorable, inspiring executive leadership charge.

FACILITATOR TALKING POINTS:
- Deliver the opening truth: 'People support what they understand.'
- Reiterate the 4 conditions: When people feel HEARD, RESPECTED, FAIRLY TREATED, and INFORMED, resistance turns into collaboration.
- Recite the supporting action commitments leading to the core outcome:
  • 01. Engage People
  • 02. Understand Interests
  • 03. Manage Emotions
  • 04. Respect Procedure
  → MAKE BETTER DECISIONS.
- Open the floor for executive Q&A, reflections, and panel discussion led by Facilitator Mr Abayomi Oladipupo Lateef.
- Suggested time: 2-3 mins."""
]

def build_deck(theme, output_filename):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots")

    for slide_idx in range(1, 17):
        img_name = f"slide_{theme}_{slide_idx:02d}.png"
        img_path = os.path.join(snapshots_dir, img_name)

        if not os.path.exists(img_path):
            print(f"Warning: {img_path} not found! Skipping.")
            continue

        slide = prs.slides.add_slide(blank_layout)

        # Place high-res live screenshot full-bleed across 16:9 canvas
        slide.shapes.add_picture(
            img_path,
            Inches(0),
            Inches(0),
            width=prs.slide_width,
            height=prs.slide_height
        )

        # Attach comprehensive speaker notes to each slide
        notes_text = SPEAKER_NOTES[slide_idx - 1]
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    prs.save(output_filename)
    print(f"Successfully generated {output_filename} with 16 pixel-perfect {theme} slides and speaker notes!")

if __name__ == "__main__":
    build_deck("dark", "stakeholder_engagement_dark.pptx")
    build_deck("light", "stakeholder_engagement_light.pptx")

    # Set client-preferred Light Theme as default masterclass copy
    import shutil
    shutil.copyfile("stakeholder_engagement_light.pptx", "stakeholder_engagement_masterclass.pptx")
    print("Copied preferred light deck to stakeholder_engagement_masterclass.pptx")
