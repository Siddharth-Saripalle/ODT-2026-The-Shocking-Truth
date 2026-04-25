# Open Design and Technology  
## Final Project README

# 1. Team Identity

## 1.1 Studio / Group Name
43 V IN THE V (volts, vegas nerve)

## 1.2 Team Members

| Name                | Primary Role                      | Secondary Role          | Strengths Brought to the Project                             |
| ------------------- | --------------------------------- | ----------------------- | ------------------------------------------------------------ |
| Rudraksh Uniyal     | Electronics / Coding / Testing            | Mechanics | Circuit building,code, debugging        |
| Siddharth Saripalle | Fabrication / Mechanics / Product | Electronics             | Physical prototyping, form development, interaction build |

## 1.3 Project Title
The Shocking Truth

## 1.4 One-Line Pitch
A wearable interactive system that allows one user to influence another user’s balance by electrically stimulating their vestibular system.

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
This project is a Galvanic Vestibular Stimulation (GVS) device, a non-invasive system that applies small, controlled electrical currents through electrodes placed near the mastoid region to stimulate the vestibular system, which is responsible for balance.

The project is structured as a two-user interactive experience:

One user (dependent variable) wears the device.
Another user (independent/controlled variable) operates a controller that influences the stimulation.

The experience creates a visible physical response—subtle shifts in balance (left/right) in the wearer.

What makes this engaging is the realization that the human body behaves like a responsive system, where external electrical input can influence internal sensory perception. This principle is already used in medical and research contexts, but here it is translated into a playful, controlled interaction.

The project aims to evoke:

curiosity,
controlled experimentation,
surprise,
and a sense of awe at the interface between technology and the human body.

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
This is an interactive, two-person control experience.

The experience involves one person actively controlling and another responding involuntarily.
The participant wearing the device experiences externally induced shifts in balance, creating a sensation of controlled movement.
The controlling user experiences agency and experimentation, adjusting inputs and observing outcomes.

The system encourages repeated interaction because:

users want to test different inputs,
observe different responses,
and understand the limits of control.

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
We are designing this project as a technological interactive experience for classmates and an informed audience interested in experimental interfaces and human-machine interaction.

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
The originality lies in gamifying Galvanic Vestibular Stimulation by introducing a second user as an active controller.

Instead of a passive medical or research setup, the system becomes:

a real-time human control interface,
where one user dynamically influences another’s physical response.

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
Controller input → electrical stimulation → vestibular response → physical shift → observation → adjustment → repeat

## 4.2 Intended Player / Audience

| Question                            | Response                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Who is this for?                    | Educated users, including those interested in neuroscience, human-machine interaction, and controlled stimulation systems |
| Age range                           | 18–28                                                                                                                     |
| Solo or multiplayer                 | Two-person interaction                                                                                                    |
| Expected duration of one round      | No fixed duration; interaction-based                                                                                      |
| What should the player feel?        | User 1: controlled (in a safe and stable manner) <br> User 2: sense of control, curiosity, experimentation                |
| Is explanation required before use? | Yes                                                                                                                       |


## 4.3 Player Journey
Describe exactly how a player will use the project.

Approach: The user encounters a wearable setup and a separate control interface.
Start: User 1 wears the device with electrodes positioned correctly.
First Action: User 2 activates the controller.
Main Interaction: User 2 varies inputs to control stimulation direction/intensity.
System Response: User 1 experiences a shift in balance (left/right deviation).
End Condition: Interaction pauses or stops when control input ceases.
Reset: System returns to neutral state, ready for the next interaction.

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

User 1 must remain in a stable standing position.
User 2 controls the system using defined input controls.
Stimulation must remain within safe, predefined limits.
Interaction stops immediately if discomfort occurs.
---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] User 1 experiences a noticeable vestibular shift (directional tilt)
- [ ]  No unsafe sensations (pain, sharp shocks, instability spikes) occur
- [ ] User 2 can reliably influence User 1’s movement
- [ ] System response is consistent and repeatable
- [ ] Interaction feels seamless between control and response

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
The smallest working version is:

a functional electrode setup,
delivering controlled electrical signals,
producing a detectable response in the user.
- Bluetooth-based remote control

## 5.3 Stretch Features
What features are nice to have but not essential?

- Neopixel-based visual feedback indicators
- Adjustable intensity modes
- Directional presets for controlled movement patterns

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [ ] Electronics-based
- [ ] Game logic based
- [ ] Installation / tabletop experience

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
The system works as a multi-stage control pipeline:

Controller Input → 2.4 GHz Dongle → Laptop → Terminal Relay Application → Mobile Hotspot Network → ESP32 IP Connection

The laptop reads controller inputs (Left / None / Right + Intensity) and sends these values over the network to the ESP32.

The ESP32 processes this input:

Determines direction (left/right)
Adjusts intensity using PWM

A 9V battery is stepped up to ~12V using a boost converter.
This controlled voltage is applied through an H-Bridge, which:

switches polarity (left/right),
controls output direction,
and delivers current to electrodes placed on the user.

Simultaneously:

A NeoPixel system provides visual feedback
Static → Rainbow
Left → Clockwise animation
Right → Anticlockwise animation

The final output is a controlled vestibular response, affecting the user’s balance.

## 6.3 Input / Output Map

| System Part | Type          | What It Does                                                |
| ----------- | ------------- | ----------------------------------------------------------- |
| Controller  | Input         | Takes left/right direction and intensity input              |
| Laptop      | Input / Relay | Reads controller input and sends data to ESP32 over network |
| ESP32       | Processing    | Interprets input, generates PWM signals, controls outputs   |
| H-Bridge    | Processing    | Switches polarity (left/right) and controls voltage output  |
| Electrodes  | Output        | Applies controlled electrical stimulation to the user       |
| NeoPixel    | Output        | Visual feedback for direction and system state              |


---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Write here]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[Write here]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[Component]` | `[Qty]` | `[Purpose]` |
| `[Component]` | `[Qty]` | `[Purpose]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Write here]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[Write here]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item                    |          Quantity | In Kit? | Need to Buy? | Estimated Cost (₹) | Material / Spec | Why This Choice?                    |
| ----------------------- | ----------------: | ------- | ------------ | -----------------: | --------------- | ----------------------------------- |
| MT3608 Boost Converter  |                 1 | No      | Yes          |                100 | Step-up module  | To precisely control output voltage |
| PC817 Optocoupler IC    | 1 packet (~3 pcs) | No      | Yes          |                100 | Isolation IC    | Electrical isolation for safety     |
| 50mA Glass Fuse         |                 1 | No      | Yes          |                 20 | 5x20mm          | Current limiting for safety         |
| Fuse Holder             |                 1 | No      | Yes          |                 20 | 5x20mm          | Secure fuse mounting                |
| 10Ω Resistors           |            1 pack | No      | Yes          |                 30 | Standard        | Current limiting                    |
| 47Ω Resistors           |            1 pack | No      | Yes          |                 30 | Standard        | Fine tuning current                 |
| 100Ω Resistors          |            1 pack | No      | Yes          |                 30 | Standard        | Safety + control                    |
| TENS/EMS Electrode Pads |            1 pack | No      | Yes          |                100 | Medical pads    | Safe interface with body            |
| 9V Batteries            |                 6 | No      | Yes          |                180 | 9V              | Portable power source               |
| 18650 Battery           |                 2 | No      | Yes          |               ~200 | Li-ion cell     | Backup power option                 |


## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately

| Item                       | Why Needed                            | Purchase Link | Latest Safe Date to Procure | Status    |
| -------------------------- | ------------------------------------- | ------------- | --------------------------- | --------- |
| Optocoupler (extra)        | Additional safety + isolation testing | Local vendor  | Week 3                      | Purchased |
| Fuse + holder              | Safety control                        | Local vendor  | Week 3                      | Purchased |
| Lower resistance resistors | Fine current tuning                   | Local vendor  | Week 3                      | Purchased |
| Extra batteries            | Backup + testing                      | Local vendor  | Week 4                      | Purchased |


## 12.4 Budget Summary

| Budget Item           |        Estimated Cost (₹) |
| --------------------- | ------------------------: |
| Electronics           |                      ~900 |
| Mechanical parts      | 0 (foam board – provided) |
| Fabrication materials |                         0 |
| Stationary            |                      ~100 |
| Purchased extras      |            Included above |
| Contingency           |                      ~100 |
| **Total**             |                 **~1100** |


## 12.5 Budget Reflection
The cost was kept minimal by:

using available components,
avoiding complex fabrication,
focusing only on essential electronics.

**Response:**  
`[Write here]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
We divided tasks based on our individual strengths and areas of interest.
Rudraksh handled most of the electronics and circuit development, including implementation and debugging.
I (Siddharth) handled component selection, procurement, and product fabrication, especially the wearable structure.
We made key electronics decisions together, but execution was primarily handled by Rudraksh.
The product form, interaction, and documentation were primarily handled by me.
Rudraksh worked on code updates and system logic, while I focused on documentation and tracking progress.
We continuously reviewed progress during build sessions and adjusted tasks as needed.

## 13.2 Task Breakdown

| Task ID | Task                                             | Owner                | Estimated Hours | Deadline | Dependency | Status  |
| ------- | ------------------------------------------------ | -------------------- | --------------: | -------- | ---------- | ------- |
| T1      | Finalize concept (GVS + interaction model)       | Rudraksh, Siddharth|               3 | Week 1   | None       | Done    |
| T2      | Research vestibular system & electrode placement | Siddharth, Rudraksh |               4 | Week 1   | T1         | Done    |
| T3      | Complete BOM & procure components                | Siddharth            |               3 | Week 2   | T1         | Done    |
| T4      | Build initial circuit (basic stimulation)        | Rudraksh             |               5 | Week 2   | T3         | Done    |
| T5      | Add optocoupler + H-Bridge integration           | Rudraksh             |               5 | Week 3   | T4         | Done    |
| T6      | Develop control logic (direction + intensity)    | Rudraksh             |               4 | Week 3   | T5         | Done    |
| T7      | Design and build wearable structure              | Siddharth            |               5 | Week 4   | T1         | Done    |
| T8      | Integrate full system (hardware + control)       | Siddharth + Rudraksh |               4 | Week 4   | T6, T7     | Done    |
| T9      | Testing and calibration                          | Rudraksh |               3 | Week 4   | T8         | Done    |
| T10     | Documentation and final refinement               | Siddharth            |               3 | Week 4   | T9         | Ongoing |


## 13.3 Responsibility Split

| Area                 | Main Owner           | Support Owner |
| -------------------- | -------------------- | ------------- |
| Concept and gameplay | Siddharth + Rudraksh | —             |
| Electronics          | Rudraksh             | Siddharth     |
| Coding               | Rudraksh             | —             |
| Mechanical build     | Siddharth            | Rudraksh      |
| Testing              | Rudraksh             | Siddharth     |
| Documentation        | Siddharth            | —             |


---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
