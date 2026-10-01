> **One-shot variant.** The baseline ran this scenario as a conversation. To run it as a single message, send the prompt below followed by this line:
>
> *Work through to the finished deliverables without pausing for my sign-off. Where the brief asks you to agree the approach with me first, decide it yourself and state the decision and its reasons at the top of the deliverable.*

---

Kick-off for Polaris DC-1 — I need the baseline programme.

I'm the scheduling manager at NordBuild. We've won Polaris DC-1 (Aviapolis Data Campus Phase 1, Vantaa) and I need the baseline CPM programme we'll submit to the Engineer.

Start by reading the project properly. It's all in the project folder — Employer's Requirements, site survey and geotechnical, planning permit conditions, grid connection offer, district heating agreement, drawings, specifications, BOQ, and the schedule inputs folder. Our contracts team has already analysed the contract already; read their analysis too and take the programme-relevant terms from it rather than re-deriving them.

Also go through our historical schedules database. This is our first data centre, so I want durations, productivity and sequencing grounded in how we have actually built, not in generic benchmarks. Tell me which past projects you leaned on and why they're the right analogues.

HOW I WANT THE DURATIONS BUILT. Our history is resource and cost loaded — every past activity carries its resource group, crew size, number of crews, BOQ quantity and package cost. So the productivity rates are not handed to you; you calculate them:

    productivity = quantity / (crews x members per crew x duration)

Work them out from the history, then build each duration as quantity / productivity, plus whatever margin you judge necessary — and say what margin you added and why. Where an activity has no measurable quantity (design, approvals, commissioning, management), say so and use the analog duration directly. Give me the productivity rates as their own document — that is the thing I will be challenged on, and I want it standing on its own.

RESOURCE LOADING is part of the schedule, not an afterthought: crew group, members per crew and number of crews on every activity, consistent with the durations above. Then the histogram, so I can see the peaks and gaps and judge whether the profile is buildable.

COST LOADING comes from the BOQ. You need the quantities for the durations anyway, so use them for the money too. Break the totals down properly — if a slab is 2,000 m2 over two floors, that is 1,000 m2 per floor, and the cost follows the same split. Tell me how you got from BOQ items to activity values: what you mapped, what you did with preliminaries and provisional sums, what you excluded, and what does not reconcile. The project BOQ is authoritative for this job — the package costs in the history are a different project and are only a sanity check, never a source. And tell me plainly whether you have loaded cost or sell value, because they are different numbers for different purposes and I need to know which one I am holding.

THE REST OF THE BRIEF:

1. A real CPM baseline — proper logic, no open ends, no constraint dates forcing a result. The critical path must fall out of the network.
2. It has to hit the contract dates: Commencement, Time for Completion, every sectional handover. Don't compress it, and don't run past them. If something genuinely cannot be met on these inputs, say so, show the arithmetic, and tell me what would have to change.
3. Calendars and constraints respected — Finnish working calendar, winter, permit conditions, working-hour restrictions, procurement lead times, third-party dates. Where a document states a lead time or a window, read it; don't infer one. Flag conflicts before we submit.

DELIVERABLES: the productivity-rates document; a Basis of Schedule (assumptions, calendars, the productivity basis and where it came from, sequencing logic, critical path narrative, risks, exclusions); the P6 XER, genuinely cost and resource loaded; and an Excel workbook with the histogram and the S-curve.

Before you hand me anything, run the reviewer — and open your own exports to check they contain what you are claiming.
